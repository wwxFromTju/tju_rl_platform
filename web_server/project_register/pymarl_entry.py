import json
import os

cmd_format = "{python_path} main.py --log-path={logdir} --config={algo_name} --env-config=sc2 with env_args.map_name={map_name}"

def train(project_file_path, python_path, params, logdir="~/.TJU_PLATFORM"):
    
    cmd = cmd_format.format(python_path=python_path, logdir=logdir + '/', algo_name=params['algo_name'], map_name=params['map_name'])

    os.chdir(project_file_path)
    print(cmd)
    os.system(cmd)

    return True


def get_metrics(log_path):
    metrics = {}
    file_names = os.path.join(log_path, 'sacred/1', 'info.json')
    data = json.load(open(file_names, 'r'))
    metrics.update(data)
    return metrics