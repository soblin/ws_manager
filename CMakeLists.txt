cmake_minimum_required(VERSION 3.10)
project(ws_manager)

find_package(ament_cmake REQUIRED)

# TODO: enable symlink install for this
install(
  PROGRAMS
  scripts/ws_manager
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
