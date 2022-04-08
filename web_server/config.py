import os

if os.getenv("TJU_PLATFORM_DIR"):
    ROOT_DIR = os.getenv("TJU_PLATFORM_DIR")
else:
    ROOT_DIR = os.path.join(os.getenv("HOME"), ".tju_platform")

DATABASE_PATH = os.path.join(ROOT_DIR, "database.db")
LOG_DIR = os.path.join(ROOT_DIR, "train_logs")

config = {
    "SQLALCHEMY_DATABASE_URI": "sqlite:///%s" % DATABASE_PATH,
}

# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
HASH_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def prepare_directory():
    if not os.path.exists(ROOT_DIR):
        os.makedirs(ROOT_DIR)

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)


project_config = {
    'ptf': {
        'python_path': "~/anaconda3/envs/PTF/bin/python",
        'train_file_path': os.path.join(os.getenv("HOME"), "projects", "ptf"),
        'entry_path': 'ptf_entry'
    },

    'pymarl': {
        'python_path': "~/anaconda3/envs/sc2_new/bin/python",
        'train_file_path': os.path.join(os.getenv("HOME"), "projects", "pymarl"),
        'entry_path': 'pymarl_entry'
    }
}

