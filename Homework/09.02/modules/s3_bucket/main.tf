resource "aws_s3_bucket" "b" {
  bucket = var.bucket_name
  acl    = var.acl
  versioning {
    enabled = true
  }

  tags = {
    Name        = var.tag
  }
}