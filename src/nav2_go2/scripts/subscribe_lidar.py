#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2

class LidarSubscriber(Node):
    def __init__(self):
        super().__init__('lidar_subscriber')

        # 订阅 Unitree Go2 LiDAR 话题
        self.subscription = self.create_subscription(
            PointCloud2,
            '/utlidar/cloud_deskewed',
            self.lidar_callback,
            10)
        self.get_logger().info("Subscribed to /utlidar/cloud_deskewed")

    def lidar_callback(self, msg):
        # 解析点云数据
        points = list(pc2.read_points(msg, field_names=("x", "y", "z"), skip_nans=True))
        if points:
            self.get_logger().info(f"Received {len(points)} LiDAR points")

def main(args=None):
    rclpy.init(args=args)
    node = LidarSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()