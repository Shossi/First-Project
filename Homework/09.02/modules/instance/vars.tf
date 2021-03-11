variable "instance_type" {
  default = "t2.micro"
}
variable "sec_group" {
  description = "security group"
}
variable "ami" {
  description = "ami id which determines which os the instance will be created on"
}
variable "subnet_id" {
  description = "subnet id for the instance"
}
variable "tag_name" {
  description = "arbitrary chosen name for the instance"
}
variable "key" {
  description = "key pair which will be paired with the instance"
}
variable "role_name" {
  description = "role which will be paired with the instance to give it certain permissions"
}