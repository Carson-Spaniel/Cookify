import os
from recipesite.settings import DEBUG

if DEBUG:
    from recipesite.secrets import USERS as users
else:
    users = os.environ["USERS"]

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
