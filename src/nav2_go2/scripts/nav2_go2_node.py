#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Nav2Go2Node(Node):
    def __init__(self):
        super().__init__('nav2_go2_node')
        
        # 创建 cmd_vel 话题的发布者
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # 设定定时器，每秒发送一次速度指令
        self.timer = self.create_timer(1.0, self.send_command)

    def send_command(self):
        msg = Twist()
        msg.linear.x = 0.5  # 机器人向前移动
        msg.angular.z = 0.0  # 不旋转
        self.get_logger().info(f'Publishing cmd_vel: linear.x={msg.linear.x:.2f}, angular.z={msg.angular.z:.2f}')
        self.cmd_vel_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = Nav2Go2Node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
