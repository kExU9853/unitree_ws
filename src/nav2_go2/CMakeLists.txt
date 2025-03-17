
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(nav2_bringup REQUIRED)
find_package(nav2_msgs REQUIRED)
find_package(nav2_util REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(unitree_go REQUIRED)
find_package(unitree_api REQUIRED)
find_package(visualization_msgs REQUIRED)

install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/nav2_go2_node.py
  scripts/read_motion_state.py
  scripts/read_low_state.py
  scripts/read_wireless_controller.py
  scripts/sport_mode_ctrl.py
  scripts/low_level_ctrl.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()