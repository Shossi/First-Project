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
  region     = var.region
  access_key = "###"
  secret_key = "###"
}

module "network" {
  source = "../modules/network"
  vpc_cidr = "10.0.0.0/16"
  private_cidr = "10.0.1.0/24"
  public_cidr  = "10.0.156.0/24"
  zone  = "us-east-1a"
}

# 2 security groups (Nginx and mysql)
module "security-group" {
  source = "../modules/security group"
  vpc_id = module.network.vpc_id
}
# create a instance of NGINX
module "nginx_instance" {
  source        = "../modules/instance"
  sec_group     = module.security-group.nginx # aws_security_group.nginx.id
  subnet_id     = module.network.public
  ami           = var.ami
  tag_name      = "nginx"
  file          = "../user_data_files/nginx.sh"
  key           = "terraform-key"
}
# create a instance of mysql
module "mysql_instance" {
  source        = "../modules/instance"
  sec_group     = module.security-group.mysql
  subnet_id     = module.network.private
  ami           = var.ami
  tag_name      = "mysql"
  file          = "../user_data_files/mysql.sh"
  key           = "terraform-key"
}
