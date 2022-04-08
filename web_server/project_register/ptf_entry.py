import json
import os

grid_cmd_format_dict = {
    'a3c': "{python_path} main.py -p {logdir} -a ptf_a3c -c ptf_a3c_conf -g grid -d grid_conf -n 20000 -e 99 -s 37 -o adam ENTROPY_BETA=0.0001 n_layer_a_1=100 n_layer_c_1=100 learning_rate_a=3e-4 learning_rate_c=3e-4 learning_rate_o=1e-3 learning_rate_t=1e-3 e_greedy=0.95 e_greedy_increment=1e-3 replace_target_iter=1000 option_batch_size=32 batch_size=32 reward_decay=0.99 option_model_path=[source_policies/grid/81/81,source_policies/grid/459/459,source_policies/grid/65/65,source_policies/grid/295/295] learning_step=10000 save_per_episodes=1000 save_model=True task=324 c1=0.001 N_WORKERS=8 USE_CPU_COUNT=False 2> null",

    'ppo': "{python_path} main.py -p {logdir} -a ptf_ppo -c ptf_ppo_conf -g grid -d grid_conf -n 20000 -e 99 -s 19 -o adam n_layer_a_1=100 n_layer_c_1=100 c2=0.005 learning_rate_a=3e-4 learning_rate_c=3e-4 learning_rate_o=3e-4 learning_rate_t=3e-4 reward_decay=0.99 clip_value=0.2 e_greedy=0.95 e_greedy_increment=1e-3 replace_target_iter=1000 option_batch_size=32 batch_size=32 option_model_path=[source_policies/grid/81/81,source_policies/grid/459/459,source_policies/grid/65/65,source_policies/grid/295/295] learning_step=10000 save_per_episodes=1000 save_model=True task=324 c3=0.0005 2> null"
}

pinball_cmd_format_dict = {
    'a3c': "{python_path} main.py -p {logdir} -a ptf_a3c -c ptf_a3c_conf -g pinball -d pinball_conf -n 20000 -e 499 -s 1 -o adam ENTROPY_BETA=0.0001 n_layer_a_1=100 n_layer_c_1=100 learning_rate_a=3e-4 learning_rate_c=3e-4 learning_rate_o=3e-4 learning_rate_t=3e-4 e_greedy=0.95 e_greedy_increment=1e-3 replace_target_iter=1000 option_batch_size=32 batch_size=32 reward_decay=0.99 option_model_path=['source_policies/a3c/0.90.9/model','source_policies/a3c/0.90.2/model','source_policies/a3c/0.20.9/model'] learning_step=10000 save_per_episodes=1000 sequential_state=False continuous_action=True configuration=game/pinball_hard_single.cfg random_start=True start_position=[[0.6,0.4]] target_position=[0.1,0.1] c1=0.0005 source_policy=a3c save_model=True action_clip=1 reward_normalize=False 2> null",

    'ppo': "{python_path} main.py -p {logdir} -a ptf_ppo -c ptf_ppo_conf -g pinball -d pinball_conf -n 20000 -e 499 -s 12345 -o adam n_layer_a_1=256 n_layer_c_1=256 c2=0.0001 learning_rate_a=3e-4 learning_rate_c=3e-4 learning_rate_o=1e-3 clip_value=0.2 learning_rate_t=1e-3 e_greedy=0.95 e_greedy_increment=5e-4 replace_target_iter=1000 option_batch_size=16 batch_size=32 reward_decay=0.99 option_model_path=['source_policies/a3c/0.90.9/model','source_policies/a3c/0.90.2/model','source_policies/a3c/0.20.9/model'] learning_step=10000 save_per_episodes=1000 sequential_state=False continuous_action=True configuration=game/pinball_hard_single.cfg start_position=[[0.6,0.4]] random_start=True target_position=[0.1,0.1] c1=0.01 source_policy=a3c save_model=True action_clip=1 reward_normalize=False option_layer_1=32 2> null"
}

cmd_format_dict = {
    'grid': grid_cmd_format_dict,
    'pinball': pinball_cmd_format_dict
}

def train(project_file_path, python_path, params, logdir="~/.TJU_PLATFORM"):
    if params['env_name'] in ['grid', 'pinball']:
        cmd_format = cmd_format_dict[params['env_name']]
    else:
        raise Exception('env support [x]')

    if params['algo_name'] in ['a3c', 'ppo']:
        cmd_format = cmd_format[params['algo_name']]
    else:
        raise Exception('algo support [x]')

    cmd = cmd_format.format(python_path=python_path, logdir=logdir + '/')

    os.chdir(project_file_path)
    os.system(cmd)

    return True


def get_metrics(log_path):
    metrics = {}
    file_names = os.path.join(log_path, 'output', 'out.json')
    data = json.load(open(file_names, 'r'))
    metrics.update(data)
    return metrics