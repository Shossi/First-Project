output "vpc_id" {
  value = aws_vpc.new_vpc.id
}
output "subnet_id" {
  value = aws_subnet.public.id
}
output "subnet2_id" {
  value = aws_subnet.public2.id
}
