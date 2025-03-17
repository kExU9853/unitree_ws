#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from unitree_go.msg import LowState  # message type should be right

class LowStateSubscriber(Node):
    def __init__(self):
        super().__init__('low_state_subscriber')
        self.subscription = self.create_subscription(
            LowState,
            'lf/lowstate',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Battery Voltage: {msg.power_v}, Motor Temps: {[m.temperature for m in msg.motor_state]}')

def main(args=None):
    rclpy.init(args=args)
    node = LowStateSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
