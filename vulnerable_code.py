import os

def get_user_input():
    return input("Enter your command: ")

def execute_command(command):
    os.system(command)  # Vulnerable to command injection

def query_database(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"  # Vulnerable to SQL injection
    # Execute query...

def render_template(user_input):
    template = f"<div>{user_input}</div>"  # Vulnerable to XSS
    return template

SECRET_KEY = "hardcoded_secret_key"  # Hardcoded secret

if __name__ == "__main__":
    user_input = get_user_input()
    execute_command(user_input)
    query_database(user_input)
    print(render_template(user_input))