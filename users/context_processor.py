# myapp/context_processors.py

from users.models.user import User

def all_users(request):
    # Fetch all user objects
    users = User.objects.all()
    # Return a dictionary with the users list
    return {'all_users': users}
