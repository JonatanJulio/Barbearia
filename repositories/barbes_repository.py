from repositories.base_repository import BaseRepository
from models.barbe import Barbe
from repositories.db import DB


class BarbesRepository(BaseRepository):
    def list(self):
        result = self.execute(
            'SELECT id, name, status FROM barbes ORDER BY id desc'
        )
        barbes = []

        for row in result:
            barbe = Barbe(id=row[0], name=row[1], status=row[2])
            barbes.append(barbe) 
            
        
        return barbes