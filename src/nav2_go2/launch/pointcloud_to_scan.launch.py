from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pointcloud_to_laserscan',
            executable='pointcloud_to_laserscan_node',
            name='pointcloud_to_scan',
            output='screen',
            parameters=[{
                "target_frame": "base_link",
                "transform_tolerance": 0.01,
                "min_height": -0.5,
                "max_height": 0.5,
                "angle_min": -1.57,  # -90度
                "angle_max": 1.57,   # 90度
                "angle_increment": 0.01,
                "scan_time": 0.1,
                "range_min": 0.1,
                "range_max": 10.0,
                "use_inf": True,
                "inf_epsilon": 1.0,
                "input_point_cloud": "/utlidar/cloud_deskewed",
                "output_scan": "/scan"
            }]
        )
    ])
