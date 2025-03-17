from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    return LaunchDescription([
        # 启动 Unitree 机器人控制节点
        Node(
            package="unitree_go",
            executable="unitree_go_node",
            name="unitree_go_controller",
            output="screen"
        ),
        
        # 启动 Navigation2
        Node(
            package="nav2_bringup",
            executable="bringup_launch.py",
            name="nav2_launch",
            output="screen",
            parameters=[
                {"use_sim_time": False}
            ]
        ),

        # 启动导航控制节点
        Node(
            package="nav2_go2",
            executable="nav2_go2_node",
            name="nav2_go2_node",
            output="screen"
        ),
    ])
