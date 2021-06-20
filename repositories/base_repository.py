from repositories.db import DB
class BaseRepository:
    def execute(self, sql):
        conn = DB.connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()

        return result
