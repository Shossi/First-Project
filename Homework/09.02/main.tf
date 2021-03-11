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
  region = var.region
}

module "role_creation" {
  source = "./modules/role"
  assume_policy_file = "./modules/role/assume_policy.json"
  policy_file = "./modules/role/policy.json"
  policy_name = "s3-read-write-only"
  role_name = "terraform-first-s3-role-creation"
}

module "s3_bucket" {
  source = "./modules/s3_bucket"
  bucket_name = "badaboom-badabing"
  tag = "terraform_bucket"
}
module "instance_creation" {
  source = "./modules/instance"
  ami = var.ami
  sec_group = "sg-0199ece7a006cf86f"
  subnet_id = "subnet-00caa5a5ff0cb35a4"
  key = "terraform-key"
  role_name = module.role_creation.role_name
  tag_name = "s3_test_instance"
}