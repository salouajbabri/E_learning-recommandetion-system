import os

from deta import Deta
from dotenv import load_dotenv


#load_dotenv(".env")
#DETA_KEY = os.getenv("DETA_KEY")
DETA_KEY = 'a0bykawvjzf_gb9JniLtwo5KBmEZcgg1uyuqfto39TiQ'

deta = Deta(DETA_KEY)

db = deta.Base("login_pwd.db")

def insert_user(username, name, password):
    """Return the user on a successful user creation,otherwise raises and error """
    return db.put({"key": username, "name": name, "password": password})

def fetch_all_users():
    """Returns a dict of all users"""
    res = db.fetch()
    return res.items

def get_user(username):
    """if not found, the function will return none"""
    return db.get(username)

def update_user(username, updates):
    """if the item is updated, return None.otherwise, en exception is raised """
    return db.update(updates, username)

def delete_user(username):
    """Always returns None, even if the key does not exist"""
    return db.delete(username)
