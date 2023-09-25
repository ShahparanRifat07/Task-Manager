from .models import User

def isEmpty(*args):
    for item in args:
        if not item:
            return True
    return False

def checkUserExists(email):
    user = User.objects.filter(email= email)
    if user:
        return True
    return False