from schema import user as SchemaUser
from db.models.user import User
from db.repo import userrepo


def fetch_user():
    return userrepo.get_user()

def insert_user(schema_user):
    user = User(**schema_user.dict())
    userrepo.insert_user(user)

def update_user(id, schema_user):
    user = schema_user.dict()
    del user['id']
    userrepo.update_user(id, user)

def delete_user(id):
    userrepo.delete_user(id)