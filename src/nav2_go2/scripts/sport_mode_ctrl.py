#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from unitree_api.msg import Request
from unitree_api.srv import SportClient

class SportModeController(Node):
    def __init__(self):
        super().__init__('sport_mode_controller')
        self.publisher = self.create_publisher(Request, '/api/sport/request', 10)
        self.timer = self.create_timer(2.0, self.send_request)

    def send_request(self):
        req = Request()
        sport_client = SportClient()
        sport_client.Euler(req, 0.0, 0.0, 0.0)  # 控制机器人姿态 (roll, pitch, yaw)
        self.publisher.publish(req)
        self.get_logger().info('Sent sport mode request')

def main(args=None):
    rclpy.init(args=args)
    node = SportModeController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
