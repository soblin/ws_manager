import rclpy
import os
import argparse
import pathlib

def main(args=None):
    # (1) argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--clear", default=None, type=str, help="path to workspace to clear")
    parser.add_argument("--load", default=None, type=str, help="path to workspace to additionally load")
    parser.add_argument("--init", default=None, type=str, help="path to workspace to load and initialize all the variables with this ones")
    parser.add_argument("--info", action='store_true', help="path to workspace to load and initialize all the variables with this ones")
    args = parser.parse_args()

    # (2) check cmd
    cmd = None
    path = None
    if args.clear:
        cmd = "clear"
        path = args.clear
    elif args.load:
        cmd = "load"
        path = args.load
    elif args.init:
        cmd = "init"
        path = args.init
    elif args.info is not None:
        cmd = "info"
    else:
        print("Did you call with {clear|load|init|info} ?")
        exit(1)

    # (3) get abs path to <ws_dir>
    ## regularize '..' in <ws_path>
    ws_path = os.path.abspath(path)
    install_path = os.path.join(ws_path, 'install')

    # (4) do checking
    ## <ws_dir>/install is assumed to exist
    if not os.path.exists(install_path):
        print(f"{path}/install does not exist.")
        exit(1)

    # (5) check ENV_VAR existance
    ENV_VARS_LISTS = ['LD_LIBRARY_PATH',
                'PYTHONPATH',
                'CMAKE_PREFIX_PATH',
                'COLCON_PREFIX_PATH',
                'AMENT_PREFIX_PATH',
                'GAZEBO_MODEL_PATH']
    env_vars = []
    for ENV_VAR in ENV_VARS_LISTS:
        if ENV_VAR in os.environ:
            env_vars.append(ENV_VAR)

    # (6) get the value, and separate by ':
    cur_env_values = {}
    reset_env_var_values = {}
    environ = os.environ
    for env_var in env_vars:
        cur_env_values[env_var] = environ[env_var]
        reset_env_var_values.setdefault(env_var, [])
        # (.1) separate by ':' and store as lists
        env_var_value = str(environ[env_var])
        for item in env_var_value.split(':'):
            # (.2) exclude that contains ws_path
            if ws_path not in item:
                reset_env_var_values[env_var].append(item)

    # (6) process
    for k, v in cur_env_values.items():
        print(f"{k}\t:   {v}")
    print("===")
    for k in reset_env_var_values.keys():
        v = reset_env_var_values[k]
        # (.1) convert back to PATH='path1:path2' style
        v_ = ''
        for cnt, path in enumerate(v):
            if cnt == 0:
                v_ += path
            else:
                v_ += (':' + path)
        reset_env_var_values[k] = v_
    for k, v in reset_env_var_values.items():
        print(f"{k}\t:   {v}")
    print    
