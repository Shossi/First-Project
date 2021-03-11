resource "aws_network_interface" "server-nic" {
  subnet_id =  var.subnet_id
  security_groups = [ var.sec_group ] # aws_security_group.nginx.id
}

resource "aws_instance" "my-instance" {
  ami                  = var.ami
  instance_type        = var.instance_type
  key_name             = var.key
  iam_instance_profile = var.role_name
  network_interface {
    device_index = 0
    network_interface_id = aws_network_interface.server-nic.id
  }
  tags = {
    "Name" = var.tag_name
  }
}
