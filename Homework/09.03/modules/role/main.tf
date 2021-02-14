resource "aws_iam_role_policy" "s3_read_write" {
  name = var.policy_name
  role = aws_iam_role.s3.id
  policy = file (var.policy_file)
}
resource "aws_iam_role" "s3" {
  name = var.role_name
  assume_role_policy = file (var.assume_policy_file)
}
resource "aws_iam_instance_profile" "s3" {
  name = var.role_name
  role = aws_iam_role.s3.name
}
