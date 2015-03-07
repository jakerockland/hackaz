# standard library imports
import json
import os

# custom module imports
from flock import app


# find the path of this file (config.py)
config_py_path = os.path.realpath(__file__)
# find the directory of this file (config.py)
config_py_dirname = os.path.dirname(config_py_path)

# get the path to secrets.json
secrets_path = os.path.join(config_py_dirname, "..", "secrets.json")
# load the secrets.json file
secrets_file = open(secrets_path)

SECRETS = json.loads(secrets_file.read()) # parse the JSON

# update application container with config
app.config.update(SECRETS.get("APP_CONFIG", {}))

# get configurations specific to parts of the codebase
oauth = SECRETS.get("oauth")
