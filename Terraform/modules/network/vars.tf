variable "vpc_cidr" {
  default = "10.0.0.0/16"
}

variable "public_cidr" {
  default = "10.0.101.0/24"
}

variable "zone" {
  default = "us-east-1a"
}
variable "vpc_name" {
  default = ""
}
variable "subnet_name" {
  default = ""
}
variable "gateway_name" {
  default = ""
}
variable "rt_name" {
  default = ""
}
variable "zone2" {
  default = "us-east-1b"
}

variable "public_cidr2" {
  default = "10.0.202.0/24"
}
variable "subnet_name2" {
  default = ""
}
variable "gateway_name2" {
  default = ""
}
variable "rt_name2" {
  default = ""
}