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
  region = "us-east-1"
  access_key = "###"
  secret_key = "###"
}


# 1- Create a VPC
# 10.122.0.0 255.255.0.0 ===> 65,536 = 2^16 
resource "aws_vpc" "new_vpc" {
  cidr_block = "10.0.0.0/16"
  tags ={
    Name = "first_vpc"
  }
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
    cidr_block = "10.0.0.0/24"
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
    "Name" = "joey-2020"
  }

}

# 7- Create new network interface1
resource "aws_network_interface" "web-server-nic" {
  subnet_id =  aws_subnet.joey_subnet.id
  private_ips = ["10.0.0.10"]
  security_groups = [ aws_security_group.allow_web.id ]
}

# 8- Create new Elastic IP
resource "aws_eip" "web_eip" {
  vpc = true
  network_interface = aws_network_interface.web-server-nic.id
  associate_with_private_ip = "10.0.0.10"
}

# 7- Create new network interface2
resource "aws_network_interface" "web-server-nic2" {
  subnet_id =  aws_subnet.joey_subnet.id
  private_ips = ["10.0.0.20"]
  security_groups = [ aws_security_group.allow_web.id ]
}
# 8- Create new Elastic IP
resource "aws_eip" "web_eip2" {
  vpc = true
  network_interface = aws_network_interface.web-server-nic2.id
  associate_with_private_ip = "10.0.0.20"
}

# 9- Printout the server public ip
output "instance_ips" {
  value = aws_eip.web_eip.public_ip
}

resource "time_sleep" "wait_3_mins" {
  depends_on = [aws_instance.web_server_instance]

  create_duration = "180s"
}

# 10- Create a new ubuntu instance
resource "aws_instance" "web_server_instance" {
    ami = "ami-0885b1f6bd170450c"
    instance_type = "t2.micro"
    availability_zone = "us-east-1a"
    key_name = "terraform-joey"
    network_interface {
      device_index = 0
      network_interface_id = aws_network_interface.web-server-nic.id
    }
    user_data = <<-EOF
      #!/bin/bash
      sudo apt update -y
      sudo apt install docker.io -y
      mkdir /home/ubuntu/terraform-project
      sudo git clone https://github.com/yossizxc/api /home/ubuntu/terraform-project/
      sudo systemctl start docker
      cd /home/ubuntu/terraform-project/weather
      sudo docker build -t joeyhd/weatherapi:v0.56 .
      docker login --username joeyhd --password zpqmzpqma
      sudo docker push joeyhd/weatherapi:v0.56
      EOF
    tags = {
     "Name" = "joey_terraform"

  }
}

resource "aws_instance" "web_server_instance2" {
  ami = "ami-0885b1f6bd170450c"
  instance_type = "t2.micro"
  availability_zone = "us-east-1a"
  key_name = "terraform-joey"
  depends_on = [time_sleep.wait_3_mins]
  network_interface {
    device_index = 0
    network_interface_id = aws_network_interface.web-server-nic2.id
  }
  user_data = <<-EOF
      #!/bin/bash
      sudo apt update -y
      sudo apt install docker.io -y
      sudo systemctl start docker
      sudo docker pull joeyhd/weatherapi:v0.56
      sudo docker run -d --restart always -p 5000:5000 joeyhd/weatherapi:v0.56
      EOF

  tags = {
    "Name" = "joey_terraform2"
  }
}

