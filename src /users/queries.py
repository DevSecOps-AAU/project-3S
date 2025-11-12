from src.database.execute.execute import DBClient
from src.users.model import UserRequest

class UserQueries:
    def __int__(self):
        self.db_client = DBClient()

        def login(self, email, password):
            query = users.select().where(users.c.email == email)
            row = self.db_client.execute_one(query)
            if not row:
                return None, "No user found"
            return row 

    def register(self, user_name, email, password):
        query = user.insert().values(user_name=user_name, email=email, password=password).returning(users)
        row = self.db_client.execute_one(query)
        if not row:
            return None, "user account creation issue"
        return row
