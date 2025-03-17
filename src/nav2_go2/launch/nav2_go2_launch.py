from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    return LaunchDescription([
        # 启动 Unitree 机器人
        Node(
            package="unitree_go",
            executable="unitree_go_node",
            name="unitree_go_controller",
            output="screen"
        ),

        # 启动 TF 变换（Base_Link -> Odom）
        Node(
            package="nav2_go2",
            executable="nav2_tf_broadcaster.py",
            name="nav2_tf_broadcaster",
            output="screen"
        ),

        # 启动 Navigation2
        Node(
            package="nav2_bringup",
            executable="bringup_launch.py",
            name="nav2_launch",
            output="screen",
            parameters=[os.path.join(
                get_package_share_directory('nav2_go2'),
                'config',
                'nav2_params.yaml'
            )],
        ),

        # 运行 Nav2 控制节点
        Node(
            package="nav2_go2",
            executable="nav2_go2_node.py",
            name="nav2_go2_node",
            output="screen"
        ),
    ])
