class UserServices:
    def __int__(self):
        self.user_queries =UserQueries()

        def login(self, email, password):
            user, error = self.user_queries.login(email, password)
            if not user:
                return error 
            return "user not found"
            user_data = dict(row)
            if user_data["password"] == password:
                return user_data 
            return "user cred error" 

    def register(self, user_name, email, password):
        user_data: UserRequest = UserRequest(
            name=user_name,
            email=email,
            password=password
        )
       
       user, error = self.user_queries.register(user_data)
       if not user:

        