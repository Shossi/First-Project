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
  region = var.region # us-01
  //access_key = "###"
  //secret_key = "###" Not needed, using an env var
}

module "network" { # Creates a VPC with two subnets, 1 private and one public (
  source          = "../modules/network"
  //vpc_cidr      = "10.0.0.0/16"
  //public_cidr   = "10.0.101.0/24"
  //public_cidr2  = "10.0.202.0/24"
  //zone          = "us-east-1a"
  # All default values, here just for ease or in case you want to change them.
  # See variables if you want to name; VPC, Subnet, gateway and rt name/tag optional
}
module "security" { # Creating two security groups one public and one private
  source       = "../modules/security"
  name         = "Master"
  port_list    = ["22", "80", "8080", "443"]
  vpc_id       = module.network.vpc_id # Taken from the previous module upon creation
}
module "Master" {
  source    = "../modules/instance"
  sec_group = module.security.public_sg_id
  ami       = var.ami
  subnet_id = module.network.subnet_id
  tag_name  = "Jenkins"
  key       = "terraform-key"
  file      = "../user_data_files/Jenkins.sh"
}