resource "aws_lb" "lob_dancer" {
  name               = var.lb_name
  internal           = false
  load_balancer_type = "application"
  security_groups    = [var.security_group]
  subnets            = [var.public_subnet, var.public_subnet2]
}

resource "aws_lb_target_group" "tg_up" {
  name     = var.tg_name
  port     = 8080
  protocol = "HTTP"
  vpc_id   = var.vpc_id
}

resource "aws_lb_listener" "lb_listener" {
  load_balancer_arn = aws_lb.lob_dancer.arn
  port = "80"
  protocol = "HTTP"

  default_action {
    type = "forward"
    target_group_arn = aws_lb_target_group.tg_up.arn
  }
}
resource "aws_lb_target_group_attachment" "first_worker" {
  target_group_arn = aws_lb_target_group.tg_up.arn
  target_id        = var.first_instance
  port             = 8080
}
resource "aws_lb_target_group_attachment" "second_worker" {
  target_group_arn = aws_lb_target_group.tg_up.arn
  target_id = var.second_instance
  port = 8080
}