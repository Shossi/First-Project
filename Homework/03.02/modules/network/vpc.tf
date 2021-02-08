resource "aws_vpc" "new_vpc" {
  cidr_block = var.vpc_cidr

  tags ={
    Name = "first_vpc"
  } 
}

resource "aws_subnet" "private" {
  vpc_id = aws_vpc.new_vpc.id
  cidr_block = var.private_cidr
  availability_zone = var.zone
  map_public_ip_on_launch = false

  tags = {
    Name = "my_private_subnet"
  }
}

resource "aws_subnet" "public" {
  vpc_id = aws_vpc.new_vpc.id
  cidr_block = var.public_cidr
  availability_zone = var.zone
  map_public_ip_on_launch = true

  tags = {
    Name = "my_public_subnet"
  }
}

resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.new_vpc.id
  tags = {
    Name = "my_gateway"
  }
}

resource "aws_route_table" "private" {
  vpc_id = aws_vpc.new_vpc.id
  tags = {
    Name = "private_rt"
  }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.new_vpc.id
  tags = {
    Name = "public_rt"
  }
}

resource "aws_route" "public_internet_gateway" {
  route_table_id         = aws_route_table.public.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.gw.id
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}
resource "aws_route_table_association" "private" {
  subnet_id      = aws_subnet.private.id
  route_table_id = aws_route_table.private.id
}