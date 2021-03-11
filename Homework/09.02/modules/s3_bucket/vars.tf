variable "bucket_name" {
  description = "a unique name for the bucket service"
}
variable "acl" {
  default = "private"
  description = "defaults to private - access control list"
}
variable "tag" {
  description = "give a tag to your created bucket service"
}