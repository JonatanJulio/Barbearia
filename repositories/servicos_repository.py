from models.servico import Servico
from repositories.db import DB
from repositories.base_repository import BaseRepository


class ServicosRepository(BaseRepository):
    def list_by_barbe_id(self, barbe_id):
        result = self.execute(
            f"SELECT id, barbe_id, name, description, due_date, status FROM servicos WHERE barbe_id = {barbe_id} ORDER BY id desc"
        )
        servicos = []

        for row in result:
            servico = Servico(
                id=row[0],
                barbe_id=row[1],
                name=row[2],
                description=row[3],
                due_date=row[4], 
                status=row[5]
            )
            servicos.append(servico)
            
        return servicos