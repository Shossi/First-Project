# terraform commands:

# terraform init
# terraform plan
# terraform destroy


terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
    #   version = "~> 3.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "eu-central-1"  # Frankfurt
  access_key = "AKIAXWJMJ7PVHQ6FTYET"
  secret_key = "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"
}


# 1- Create a VPC
# 10.122.0.0 255.255.0.0 ===> 65,536 = 2^16 
resource "aws_vpc" "new_vpc" {
  cidr_block = "10.122.0.0/16"
}

# 2- Create an internet gateway
resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.new_vpc.id
}

# 3- Create Custom Route Table
resource "aws_route_table" "joey_rt" {
 vpc_id = aws_vpc.new_vpc.id

 route {
     cidr_block = "0.0.0.0/0" # IPv4
     gateway_id = aws_internet_gateway.gw.id
 }

 route {
     ipv6_cidr_block = "::/0" #IPv6
     gateway_id = aws_internet_gateway.gw.id
 }

 tags = {
   "Name" = "joey_int"
 }

}

# 4- Create network Subnet
resource "aws_subnet" "joey_subnet" {
    vpc_id = aws_vpc.new_vpc.id
    cidr_block = "10.122.122.0/24"
    availability_zone = "us-east-1a"
    
    tags = {
      Name = "my_subnet-01"
    }
}

# 5- Associate Route table with subnet
resource "aws_route_table_association" "a" {
 subnet_id = aws_subnet.joey_subnet.id
 route_table_id = aws_route_table.joey_rt.id
}

# 6- Create securiry group
resource "aws_security_group" "allow_web" {
  name = "allow_web_traffic"
  description = "Allow inbound web traffic"
  vpc_id = aws_vpc.new_vpc.id

  ingress {
    cidr_blocks = [ "0.0.0.0/0" ]
    description = "HTTP"
    from_port = 80
    to_port = 80
    protocol = "tcp"
  }

  ingress {
    cidr_blocks = [ "0.0.0.0/0" ]
    description = "HTTPS"
    from_port = 443
    to_port = 443
    protocol = "tcp"
  }
  
  ingress {
    cidr_blocks = [ "0.0.0.0/0" ]
    description = "SSH"
    from_port = 22
    to_port = 22
    protocol = "tcp"
  } 
  
  egress  {
    cidr_blocks = [ "0.0.0.0/0" ]
    description = "All networks allowed"
    from_port = 0
    to_port = 0
    protocol = "-1"
  } 

  tags = {
    "Name" = "DevOps-2020"
  }

}

# 7- Create new network interface
resource "aws_network_interface" "web-server-nic" {
  subnet_id =  aws_subnet.joey_subnet.id
  private_ip = "10.122.122.122"
  security_groups = [ aws_security_group.allow_web.id ]
}

# 8- Create new Elastic IP
resource "aws_eip" "web_eip" {
    vpc = true
    network_interface = aws_network_interface.web-server-nic.id
    # associate_with_private_ip = "10.122.122.122"
    depends_on = [ aws_internet_gateway.gw ]
}

# 9- Printout the server public ip
output "server_public_ip" {
  value = aws_eip.web_eip.public_ip
}

resource "aws_key_pair" "joey-key" {
  key_name   = "terraform-key"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD3F6tyPEFEzV0LX3X8BsXdMsQz1x2cEikKDEY0aIj41qgxMCP/iteneqXSIFZBp5vizPvaoIR3Um9xK7PGoW8giupGn+EPuxIA4cDM4vzOqOkiMPhz5XK0whEjkVzTo4+S0puvDZuwIsdiW9mxhJc7tgBNL0cYlWSYVkz4G/fslNfRPW5mYAM49f4fhtxPb5ok4Q2Lg9dPKVHO/Bgeu5woMc7RY0p1ej6D4CKFE6lymSDJpW0YHX/wqE9+cfEauh7xZcG0q9t2ta6F6fmX0agvpFyZo8aFbXeUBr7osSCJNgvavWbM/06niWrOvYX2xwWdhXmXSrbX8ZbabVohBK41 email@example.com"
}

# 10- Create a new ubuntu instance
resource "aws_instance" "web_server_instance" {
    ami = "ami-0885b1f6bd170450c"
    instance_type = "t2.micro"
    availability_zone = "us-east-1a"
    key_name = "terraform-key"
    
    network_interface {
      device_index = 0
      network_interface_id = aws_network_interface.web-server-nic.id
    }
    user_data = <<-EOF

    sudo apt update 
    sudo apt install docker.io
    mkdir /home/ubuntu/terraform-prod
    git clone https://github.com/yossizxc/api /home/ubuntu/terraform-prod
    cd /home/ubuntu/terraform-prod

    EOF

  tags = {
    "Name" = "joey_terraform"
  }
}