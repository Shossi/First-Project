resource "aws_vpc" "new_vpc" {
  cidr_block = var.vpc_cidr # default = "10.0.0.0/16"

  tags ={
    Name = var.vpc_name
  }
}

resource "aws_subnet" "public" {
  vpc_id = aws_vpc.new_vpc.id
  cidr_block = var.public_cidr # default = "10.0.202.0/24"
  availability_zone = var.zone # default = "us-east-1a"
  map_public_ip_on_launch = true
# map public ip for public subnet to enable outside traffic

  tags = {
    Name = var.subnet_name
  }
}
# allows communication between you VPC and the internet
resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.new_vpc.id
  tags = {
    Name = var.gateway_name
  }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.new_vpc.id
  tags = {
    Name = var.rt_name
  }
}
# Only the public subnet needs the gateway,
# we don't want to enable internet access to the private subnet
resource "aws_route" "public_internet_gateway" {
  route_table_id         = aws_route_table.public.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.gw.id
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

##################################### Second subnet
resource "aws_subnet" "public2" {
  vpc_id = aws_vpc.new_vpc.id
  cidr_block = var.public_cidr2 # default = "10.0.202.0/24"
  availability_zone = var.zone2 # default = "us-east-1b"
  map_public_ip_on_launch = true
  # map public ip for public subnet to enable outside traffic

  tags = {
    Name = var.subnet_name2
  }
}
# allows communication between you VPC and the internet
resource "aws_internet_gateway" "gw2" {
  vpc_id = aws_vpc.new_vpc.id
  tags = {
    Name = var.gateway_name2
  }
}

resource "aws_route_table" "public2" {
  vpc_id = aws_vpc.new_vpc.id
  tags = {
    Name = var.rt_name2
  }
}
# Only the public subnet needs the gateway,
# we don't want to enable internet access to the private subnet
resource "aws_route" "public_internet_gateway2" {
  route_table_id         = aws_route_table.public2.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.gw2.id
}

resource "aws_route_table_association" "public2" {
  subnet_id      = aws_subnet.public2.id
  route_table_id = aws_route_table.public2.id
}
