# ws_manager

A command line tool especially for cleaning-up environmenet variables related to ROS2 workspace

## target variables

- `LD_LIBRARY_PATH`
- `PYTHONPATH`
- `CMAKE_PREFIX_PATH`
- `COLCON_PREFIX_PATH`
- `AMENT_PREFIX_PATH`
- `GAZEBO_MODEL_PATH`

## usage

### info

Print `COLCON_PREFIX_PATH`.

```
ros2 run ws_manager ws_manager --info
```

### clear

Delete the path to `ws_dir` from the environment variables.

```
source <(ros2 run ws_manager ws_manager --clear <ws_dir>)
```

### reinit

Delete all paths except for system's one (`/opt/ros/~`) from the environment variables, and then `source <ws_dir>/install/local_setup.bash`

```
source <(ros2 run ws_manager ws_manager --reinit <ws_dir>)
```

## context

`ros2 run` is executed in a child process, so running 
