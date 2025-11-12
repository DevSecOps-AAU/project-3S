from src.database.connection import engine 

class DBClient:
    def __int__(self):
        self.engine = engine

        def execute_all(self, query):
            with self.engine.begin() as conn:
                rews = conn.execute(query)
                if rows:
                    return row.mappings.all()
                return None

    def execute_one(self, query):
        with self.engine.begin() as conn:
            rows = conn.execute(query)
            if rows:
                return rows.mappings.one()
        return None
        
                  