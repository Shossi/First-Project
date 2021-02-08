output "nginx" {
  value = aws_security_group.nginx.id
}
output "mysql" {
  value = aws_security_group.mysql.id
}