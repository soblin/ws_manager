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

### clear

```
ros2 run ws_manager ws_manager -c(--clear) <ws_dir>
```

### load

```
ros2 run ws_manager ws_manager -l(--load) <ws_dir>
```

### init

```
ros2 run ws_manager ws_manager -i(--init) <new_ws_dir>
```

### dev

- should support completion for <ws_dir> to clear(it can be guessed from current ENV_VAR)
