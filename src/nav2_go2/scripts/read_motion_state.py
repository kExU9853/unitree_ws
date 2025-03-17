#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from unitree_go.msg import SportModeState  # 确保消息类型正确

class MotionStateSubscriber(Node):
    def __init__(self):
        super().__init__('motion_state_subscriber')
        self.subscription = self.create_subscription(
            SportModeState,
            'lf/sportmodestate',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Mode: {msg.mode}, Position: {msg.position}, Velocity: {msg.velocity}')

def main(args=None):
    rclpy.init(args=args)
    node = MotionStateSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
