import re

def validate_username(username):
    if not re.match("^[a-zA-Z0-9_]{4,20}$", username):
        return False
    if " " in username:
        return False
    return True

def validate_password(password):
    if len(password) < 6:
        return False
    if " " in password:
        return False
    return True