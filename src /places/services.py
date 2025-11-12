class PlacesServices:
    def __int__(self):
        self.user_queries =UserQueries()

        def login(self, email, password):
            user, error = self.user_queries.login(email, password)
            if not user:
                return error 
            return user 
            