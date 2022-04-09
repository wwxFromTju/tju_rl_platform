web服务所需的python版本为3.9，具体依赖为requirements.txt中

此外为了运行所支持的pymarl和ptf，需要安装对应的anaconda环境，环境分别命名为pymarl和ptf，然后具体的依赖见：
https://github.com/oxwhirl/pymarl
https://github.com/tianpeiyang/PTF_code

然后需要将projects移动到home目录下下或者做个软链接

启动方法：
进去web_server目录后`uvicorn main:app --reload`

#### 创建用户

Request URL

http://127.0.0.1:8000/users/

Curl

```
curl -X 'POST' \
  'http://127.0.0.1:8000/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "tju_rl.tju.edu.cn",
  "password": "tju_rl"
}'
```

Response body

```
{
  "email": "tju_rl.tju.edu.cn",
  "id": 1,
  "is_active": true,
  "projects": []
}
```

#### 登陆获取token

Request URL

http://127.0.0.1:8000/token

Curl

```
curl -X 'POST' \
  'http://127.0.0.1:8000/token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=&username=tju_rl.tju.edu.cn&password=tju_rl&scope=&client_id=&client_secret='
```

Response body

```
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0anVfcmwudGp1LmVkdS5jbiIsImV4cCI6MTY0OTQ3ODc2OX0.8BTaJcSKb4rikO2-XnUb1v5xsY5OoSA6FHz94wNtn8c",
  "token_type": "bearer"
}
```

#### 获取所有用户信息

Request URL
http://127.0.0.1:8000/users

Curl

```
curl -X 'GET' \
  'http://127.0.0.1:8000/users' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0anVfcmwudGp1LmVkdS5jbiIsImV4cCI6MTY0OTQ3ODc2OX0.8BTaJcSKb4rikO2-XnUb1v5xsY5OoSA6FHz94wNtn8c'
```

Response body

```
[
  {
    "email": "tju_rl.tju.edu.cn",
    "id": 1,
    "is_active": true,
    "projects": []
  }
]
```

#### 指定用户id获得具体用户信息
Request URL

http://127.0.0.1:8000/users/{user_id}

Curl

```
curl -X 'GET' \
  'http://127.0.0.1:8000/users/1' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0anVfcmwudGp1LmVkdS5jbiIsImV4cCI6MTY0OTQ3ODc2OX0.8BTaJcSKb4rikO2-XnUb1v5xsY5OoSA6FHz94wNtn8c'
```

Response body

```
{
  "email": "tju_rl.tju.edu.cn",
  "id": 1,
  "is_active": true,
  "projects": []
}
```

#### 为具体用户创建项目
Request URL

http://127.0.0.1:8000/users/{user_id}/projects/


Curl

```
curl -X 'POST' \
  'http://127.0.0.1:8000/users/1/projects/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0anVfcmwudGp1LmVkdS5jbiIsImV4cCI6MTY0OTQ3ODc2OX0.8BTaJcSKb4rikO2-XnUb1v5xsY5OoSA6FHz94wNtn8c' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "标题",
  "description": "用来描述项目，比如当前的project_type目前就只支持pymarl或者ptf",
  "project_type": "pymarl"
}'
```

Response body

```
{
  "title": "标题",
  "description": "用来描述项目，比如当前的project_type目前就只支持pymarl或者ptf",
  "project_type": "pymarl",
  "id": 1,
  "owner_id": 1,
  "log_path": "/Users/codeman/.tju_platform/train_logs/6ef52034-b7ba-11ec-8642-88e9fe8884f5",
  "experiments": []
}
```

#### 为某个用户查询所有项目
Request URL

http://127.0.0.1:8000/users/1/projects/

Curl

```
curl -X 'GET' \
  'http://127.0.0.1:8000/users/{user_id}/projects/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0anVfcmwudGp1LmVkdS5jbiIsImV4cCI6MTY0OTQ3ODc2OX0.8BTaJcSKb4rikO2-XnUb1v5xsY5OoSA6FHz94wNtn8c'
```


Response body

```
[
  {
    "title": "标题",
    "description": "用来描述项目，比如当前的project_type目前就只支持pymarl或者ptf",
    "project_type": "pymarl",
    "id": 1,
    "owner_id": 1,
    "log_path": "/Users/codeman/.tju_platform/train_logs/6ef52034-b7ba-11ec-8642-88e9fe8884f5",
    "experiments": []
  }
]
```

#### 为某个用户查询具体项目
Request URL

http://127.0.0.1:8000/users/{user_id}/projects/{project_id}

Curl

```
curl -X 'GET' \
  'http://127.0.0.1:8000/users/1/projects/1' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0anVfcmwudGp1LmVkdS5jbiIsImV4cCI6MTY0OTQ3ODc2OX0.8BTaJcSKb4rikO2-XnUb1v5xsY5OoSA6FHz94wNtn8c'
```

Response body

```
{
  "title": "标题",
  "description": "用来描述项目，比如当前的project_type目前就只支持pymarl或者ptf",
  "project_type": "pymarl",
  "id": 1,
  "owner_id": 1,
  "log_path": "/Users/codeman/.tju_platform/train_logs/6ef52034-b7ba-11ec-8642-88e9fe8884f5",
  "experiments": []
}
```

#### 为某个用户在具体项目下创建训练
Request URL

http://127.0.0.1:8000/users/{user_id}/projects/{project_id}/experiments/

Curl

```
curl -X 'POST' \
  'http://127.0.0.1:8000/users/1/projects/1/experiments/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0anVfcmwudGp1LmVkdS5jbiIsImV4cCI6MTY0OTQ3ODc2OX0.8BTaJcSKb4rikO2-XnUb1v5xsY5OoSA6FHz94wNtn8c' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "训练标题",
  "description": "用来描述这个训练，比如这个是针对pymarl的， 然后parameter里面的参数，取决于你entry部分所使用的",
  "parameter": {
      "algo_name": "qmix",
      "map_name": "3s5z"
  }
}'
```

Response body
```
{
  "title": "训练标题",
  "description": "用来描述这个训练，比如这个是针对pymarl的， 然后parameter里面的参数，取决于你entry部分所使用的",
  "parameter": "{'algo_name': 'qmix', 'map_name': '3s5z'}",
  "id": 1,
  "project_id": 1,
  "owner_id": 1,
  "log_path": "/Users/codeman/.tju_platform/train_logs/6ef52034-b7ba-11ec-8642-88e9fe8884f5/f93e946e-b7ba-11ec-8642-88e9fe8884f5",
  "is_active": true,
  "metric": null
}
```

#### 为某个用户在具体项目下查寻所有的训练
Request URL

http://127.0.0.1:8000/users/{user_id}/projects/{project_id}/experiments/

Curl

```
curl -X 'GET' \
  'http://127.0.0.1:8000/users/1/projects/1/experiments/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0anVfcmwudGp1LmVkdS5jbiIsImV4cCI6MTY0OTQ3ODc2OX0.8BTaJcSKb4rikO2-XnUb1v5xsY5OoSA6FHz94wNtn8c'
```


Response body

```
[
  {
    "title": "训练标题",
    "description": "用来描述这个训练，比如这个是针对pymarl的， 然后parameter里面的参数，取决于你entry部分所使用的",
    "parameter": "{'algo_name': 'qmix', 'map_name': '3s5z'}",
    "id": 1,
    "project_id": 1,
    "owner_id": 1,
    "log_path": "/Users/codeman/.tju_platform/train_logs/6ef52034-b7ba-11ec-8642-88e9fe8884f5/f93e946e-b7ba-11ec-8642-88e9fe8884f5",
    "is_active": true,
    "metric": {
      "battle_won_mean": [
        0
      ],
      "battle_won_mean_T": [
        56
      ],
      "dead_allies_mean": [
        8
      ],
      "dead_allies_mean_T": [
        56
      ],
      "dead_enemies_mean": [
        1
      ],
      "dead_enemies_mean_T": [
        56
      ],
      "ep_length_mean": [
        56
      ],
      "ep_length_mean_T": [
        56
      ],
      "epsilon": [
        1
      ],
      "epsilon_T": [
        56
      ],
      "return_mean": [
        5.019867549668872
      ],
      "return_mean_T": [
        56
      ],
      "return_std": [
        0
      ],
      "return_std_T": [
        56
      ]
    }
  }
]
```

#### 为某个用户在具体项目下查寻具体的训练
Request URL
http://127.0.0.1:8000/users/{user_id}/projects/{projects_id}/experiments/{experiment_id}

Curl

```
curl -X 'GET' \
  'http://127.0.0.1:8000/users/1/projects/1/experiments/1' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0anVfcmwudGp1LmVkdS5jbiIsImV4cCI6MTY0OTQ3ODc2OX0.8BTaJcSKb4rikO2-XnUb1v5xsY5OoSA6FHz94wNtn8c'
```

Response body
```
{
  "title": "训练标题",
  "description": "用来描述这个训练，比如这个是针对pymarl的， 然后parameter里面的参数，取决于你entry部分所使用的",
  "parameter": "{'algo_name': 'qmix', 'map_name': '3s5z'}",
  "id": 1,
  "project_id": 1,
  "owner_id": 1,
  "log_path": "/Users/codeman/.tju_platform/train_logs/6ef52034-b7ba-11ec-8642-88e9fe8884f5/f93e946e-b7ba-11ec-8642-88e9fe8884f5",
  "is_active": true,
  "metric": {
    "battle_won_mean": [
      0
    ],
    "battle_won_mean_T": [
      56
    ],
    "dead_allies_mean": [
      8
    ],
    "dead_allies_mean_T": [
      56
    ],
    "dead_enemies_mean": [
      1
    ],
    "dead_enemies_mean_T": [
      56
    ],
    "ep_length_mean": [
      56
    ],
    "ep_length_mean_T": [
      56
    ],
    "epsilon": [
      1
    ],
    "epsilon_T": [
      56
    ],
    "grad_norm": [
      3.608581827478441
    ],
    "grad_norm_T": [
      1665
    ],
    "loss": [
      0.1839391589164734
    ],
    "loss_T": [
      1665
    ],
    "q_taken_mean": [
      0.035212478408584366
    ],
    "q_taken_mean_T": [
      1665
    ],
    "return_mean": [
      5.019867549668872
    ],
    "return_mean_T": [
      56
    ],
    "return_std": [
      0
    ],
    "return_std_T": [
      56
    ],
    "target_mean": [
      0.07710549294411599
    ],
    "target_mean_T": [
      1665
    ],
    "td_error_abs": [
      0.34947575749577703
    ],
    "td_error_abs_T": [
      1665
    ],
    "test_battle_won_mean": [
      0
    ],
    "test_battle_won_mean_T": [
      56
    ],
    "test_dead_allies_mean": [
      7.9375
    ],
    "test_dead_allies_mean_T": [
      56
    ],
    "test_dead_enemies_mean": [
      1.5625
    ],
    "test_dead_enemies_mean_T": [
      56
    ],
    "test_ep_length_mean": [
      55.25
    ],
    "test_ep_length_mean_T": [
      56
    ],
    "test_return_mean": [
      4.708040149006623
    ],
    "test_return_mean_T": [
      56
    ],
    "test_return_std": [
      1.0783935988345477
    ],
    "test_return_std_T": [
      56
    ]
  }
}
```

#### 为某个用户在具体项目下停止具体的训练

Request URL
http://127.0.0.1:8000/users/{user_id}/projects/{project_id}/experiments/{experiment_id}/stop


Curl

```
curl -X 'POST' \
  'http://127.0.0.1:8000/users/1/projects/1/experiments/1/stop' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0anVfcmwudGp1LmVkdS5jbiIsImV4cCI6MTY0OTQ3ODc2OX0.8BTaJcSKb4rikO2-XnUb1v5xsY5OoSA6FHz94wNtn8c' \
  -d ''
```

Response body
```
{
  "title": "训练标题",
  "description": "用来描述这个训练，比如这个是针对pymarl的， 然后parameter里面的参数，取决于你entry部分所使用的",
  "parameter": "{'algo_name': 'qmix', 'map_name': '3s5z'}",
  "id": 1,
  "project_id": 1,
  "owner_id": 1,
  "log_path": "/Users/codeman/.tju_platform/train_logs/6ef52034-b7ba-11ec-8642-88e9fe8884f5/f93e946e-b7ba-11ec-8642-88e9fe8884f5",
  "is_active": false,
  "metric": {
    "battle_won_mean": [
      0
    ],
    "battle_won_mean_T": [
      56
    ],
    "dead_allies_mean": [
      8
    ],
    "dead_allies_mean_T": [
      56
    ],
    "dead_enemies_mean": [
      1
    ],
    "dead_enemies_mean_T": [
      56
    ],
    "ep_length_mean": [
      56
    ],
    "ep_length_mean_T": [
      56
    ],
    "epsilon": [
      1
    ],
    "epsilon_T": [
      56
    ],
    "grad_norm": [
      3.608581827478441
    ],
    "grad_norm_T": [
      1665
    ],
    "loss": [
      0.1839391589164734
    ],
    "loss_T": [
      1665
    ],
    "q_taken_mean": [
      0.035212478408584366
    ],
    "q_taken_mean_T": [
      1665
    ],
    "return_mean": [
      5.019867549668872
    ],
    "return_mean_T": [
      56
    ],
    "return_std": [
      0
    ],
    "return_std_T": [
      56
    ],
    "target_mean": [
      0.07710549294411599
    ],
    "target_mean_T": [
      1665
    ],
    "td_error_abs": [
      0.34947575749577703
    ],
    "td_error_abs_T": [
      1665
    ],
    "test_battle_won_mean": [
      0
    ],
    "test_battle_won_mean_T": [
      56
    ],
    "test_dead_allies_mean": [
      7.9375
    ],
    "test_dead_allies_mean_T": [
      56
    ],
    "test_dead_enemies_mean": [
      1.5625
    ],
    "test_dead_enemies_mean_T": [
      56
    ],
    "test_ep_length_mean": [
      55.25
    ],
    "test_ep_length_mean_T": [
      56
    ],
    "test_return_mean": [
      4.708040149006623
    ],
    "test_return_mean_T": [
      56
    ],
    "test_return_std": [
      1.0783935988345477
    ],
    "test_return_std_T": [
      56
    ]
  }
}
```
