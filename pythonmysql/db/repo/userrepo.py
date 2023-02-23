from db.models.user import User
from db.session import get_session


def get_user():
    with get_session() as session:
        return session.query(User).all()

def insert_user(user):
    with get_session() as session:
        session.add(user)
        session.commit()

def update_user(id, schema_user):
    with get_session() as session:
        user = session.get(User, id)
        for key, value in schema_user.items():
            setattr(user, key, value)
        session.commit()

def delete_user(id):
    with get_session() as session:
        user = session.get(User, id)
        session.delete(user)
        session.commit()
        
