import json

# Load the username from memory, if it has been stored previously.
# Otherwise, prompt the user for their name and add it to the username.json file.

def get_stored_username():
    """ Get stored username, if avaiable"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
       return None
    else:
        return username
        
def get_new_username():
    """Prompt for a new username"""
    username = input("What's your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """ Greet the user by name"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()