#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from unitree_api.msg import Request

class CmdVelToGo2(Node):
    def __init__(self):
        super().__init__('cmd_vel_to_go2')

        # 订阅 Nav2 的速度控制指令
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_vel_callback,
            10)

        # 创建 Go2 高层运动控制发布者
        self.publisher = self.create_publisher(Request, '/api/sport/request', 10)

        self.get_logger().info("CmdVelToGo2 node started, subscribing to /cmd_vel")

    def cmd_vel_callback(self, msg):
        go2_msg = Request()
        go2_msg.command = "Move"
        go2_msg.args = [msg.linear.x, msg.linear.y, msg.angular.z]

        self.get_logger().info(f"Sending Move command: vx={msg.linear.x}, vy={msg.linear.y}, vyaw={msg.angular.z}")
        self.publisher.publish(go2_msg)

def main(args=None):
    rclpy.init(args=args)
    node = CmdVelToGo2()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
