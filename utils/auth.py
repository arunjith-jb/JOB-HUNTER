import json
import hashlib
import os

USERS_FILE = "users.json"


def _ensure_users_file():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            json.dump({}, f)


def load_users():
    _ensure_users_file()
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def save_users(users: dict):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def signup_user(username: str, password: str):
    users = load_users()
    if username in users:
        return False, "User already exists!"
    users[username] = hash_password(password)
    save_users(users)
    return True, "Signup successful. You can now log in."


def login_user(username: str, password: str):
    users = load_users()
    if username not in users:
        return False, "User does not exist!"
    if users[username] != hash_password(password):
        return False, "Incorrect password!"
    return True, "Login successful!"
