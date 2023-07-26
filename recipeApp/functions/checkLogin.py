import os
from recipesite.settings import DEBUG
import json

if DEBUG:
    from recipesite.secrets import USERS_ENV_VAR as users
else:
    users_json = os.environ.get("USERS_ENV_VAR", "{}") #users_env_var must be in double quotes
    users = json.loads(users_json)

def checkLoginFun(username, password):
    try:
        if password == users[username]:
            usernameCheck = True
            passwordCheck = True
        else:
            usernameCheck = True
            passwordCheck = False
    except KeyError:
        usernameCheck = False
        passwordCheck = False
    finally:
        return usernameCheck, passwordCheck
