#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from unitree_go.msg import WirelessController

class WirelessControllerSubscriber(Node):
    def __init__(self):
        super().__init__('wireless_controller_subscriber')
        self.subscription = self.create_subscription(
            WirelessController,
            '/wirelesscontroller',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Joystick: LX={msg.lx}, LY={msg.ly}, RX={msg.rx}, RY={msg.ry}, Keys={msg.keys}')

def main(args=None):
    rclpy.init(args=args)
    node = WirelessControllerSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
