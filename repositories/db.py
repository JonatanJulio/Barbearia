import psycopg2


class DB:
    @staticmethod
    def connection():
        conn = psycopg2.connect(
            host="localhost",
            database="barbearia",
            user="postgres",
            password="123"
        )

        return conn
