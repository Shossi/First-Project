resource "aws_security_group" "public" {
  name = var.name
  description = "Allow inbound web traffic"
  vpc_id = var.vpc_id # pulled from vpc module upon creation

  dynamic "ingress" { # Connection to the machine
    for_each = var.port_list # https,http ssh and 8080 just in case I need to change the http port
    content {
      from_port = ingress.value
      to_port = ingress.value
      protocol = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  } # looping through the ports and allowing each one of them.

  egress  { # Connection from the machine
    cidr_blocks = [ "0.0.0.0/0" ]
    description = "All networks allowed"
    from_port = 0
    to_port = 0
    protocol = "-1"
  }

  tags = {
    "Name" = "Public"
  }
}
