#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from unitree_go.msg import LowCmd

class LowLevelController(Node):
    def __init__(self):
        super().__init__('low_level_controller')
        self.publisher = self.create_publisher(LowCmd, '/lowcmd', 10)
        self.timer = self.create_timer(1.0, self.send_command)

    def send_command(self):
        cmd = LowCmd()
        cmd.motor_cmd[0].q = 1.0  # 目标角度
        cmd.motor_cmd[0].dq = 0.0  # 目标速度
        cmd.motor_cmd[0].tau = 0.0  # 力矩
        cmd.motor_cmd[0].kp = 10.0  # 刚度
        cmd.motor_cmd[0].kd = 1.0  # 阻尼
        self.publisher.publish(cmd)
        self.get_logger().info('Sent low-level motor command')

def main(args=None):
    rclpy.init(args=args)
    node = LowLevelController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
