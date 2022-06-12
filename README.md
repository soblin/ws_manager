# ws_manager

A command line tool especially for cleaning-up environmenet variables related to ROS2 workspace.

## target variables

- `COLCON_PREFIX_PATH`
- `AMENT_PREFIX_PATH`
- `CMAKE_PREFIX_PATH`
- `LD_LIBRARY_PATH`
- `PYTHONPATH`
- `GAZEBO_MODEL_PATH`

## usage

### check

```
ros2 run ws_manager ws_manager --check
```

### clear

Delete the path to `ws_dir` from the listed environment variables.

```
source <(ros2 run ws_manager ws_manager --clear <ws_dir>)
```

### reinit

Delete all paths except for system's one (`/opt/ros/~`) from the listed environment variables, and then `source <ws_dir>/install/local_setup.bash`

```
source <(ros2 run ws_manager ws_manager --reinit <ws_dir>)
```

## context

`ros2 run` is executed in a child process, so running shell or python script in this form actually has no effect.
