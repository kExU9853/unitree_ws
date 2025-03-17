#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from unitree_go.msg import SportModeState
import tf2_ros
from geometry_msgs.msg import TransformStamped

class Go2StateToOdom(Node):
    def __init__(self):
        super().__init__('go2_state_to_odom')

        # 订阅 Go2 的高层状态接口
        self.subscription = self.create_subscription(
            SportModeState,
            '/sportmodestate',
            self.state_callback,
            10)

        # 发布 ROS 2 兼容的 /odom 话题
        self.odom_publisher = self.create_publisher(Odometry, '/odom', 10)

        # 发布 TF 变换
        self.tf_broadcaster = tf2_ros.TransformBroadcaster(self)

        self.get_logger().info("Subscribed to /sportmodestate, publishing /odom")

    def state_callback(self, msg):
        odom_msg = Odometry()
        odom_msg.header.stamp = self.get_clock().now().to_msg()
        odom_msg.header.frame_id = "odom"
        odom_msg.child_frame_id = "base_link"

        # 位置
        odom_msg.pose.pose.position.x = msg.position[0]
        odom_msg.pose.pose.position.y = msg.position[1]
        odom_msg.pose.pose.position.z = msg.position[2]

        # 速度
        odom_msg.twist.twist.linear.x = msg.velocity[0]
        odom_msg.twist.twist.linear.y = msg.velocity[1]
        odom_msg.twist.twist.angular.z = msg.yaw_speed

        # 发布 /odom
        self.odom_publisher.publish(odom_msg)

        # 发送 TF 变换
        t = TransformStamped()
        t.header.stamp = odom_msg.header.stamp
        t.header.frame_id = "odom"
        t.child_frame_id = "base_link"
        t.transform.translation.x = msg.position[0]
        t.transform.translation.y = msg.position[1]
        t.transform.translation.z = msg.position[2]
        self.tf_broadcaster.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    node = Go2StateToOdom()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
