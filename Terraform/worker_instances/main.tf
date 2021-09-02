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
//  access_key = "###"
//  secret_key = "###" Not needed, using an env var
}

module "network" { # Creates a VPC with two subnets, 1 private and one public (
  source         = "../modules/network"
//  vpc_cidr     = "10.0.0.0/16"
//  public_cidr  = "10.0.101.0/24"
//  public_cidr2 = "10.0.202.0/24"
//  zone         = "us-east-1a"
  # All default values, here just for ease
  # See variables if you want to name; VPC, Subnet, gateway and rt name/tag optional
}

module "security" { # Creating two security groups one public and one private
  source    = "../modules/security"
  name      = "Worker"
  port_list = ["22", "80", "8080", "443"]
  vpc_id    = module.network.vpc_id # Taken from the previous module upon creation
}

module "First_Worker" {
  source    = "../modules/instance"
  sec_group = module.security.public_sg_id
  ami       = var.ami
  subnet_id = module.network.subnet_id
  tag_name  = "First Worker Instance"
  key       = "terraform-key"
  file      = "../user_data_files/Worker.sh"
}

module "Second_Worker" {
  source    = "../modules/instance"
  sec_group = module.security.public_sg_id
  ami       = var.ami
  subnet_id = module.network.subnet_id
  tag_name  = "Second Worker Instance"
  key       = "terraform-key"
  file      = "../user_data_files/Worker.sh"
}

module "load_balancer" {
  source           = "../modules/load_balancer"
  lb_name          = "worker-lb"
  tg_name          = "worker-tg"
  security_group   = module.security.public_sg_id
  vpc_id           = module.network.vpc_id
  public_subnet    = module.network.subnet_id
  public_subnet2   = module.network.subnet2_id
  first_instance   = module.First_Worker.instance_id
  second_instance  = module.Second_Worker.instance_id
}