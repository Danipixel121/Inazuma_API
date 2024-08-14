from pydantic import BaseModel
from typing import List, Dict
from uuid import uuid4

class Player(BaseModel):
    id: str
    nombre: str
    apellido: str
    posicion: str
    img: str = None
    equipo: str = None

    def __init__(self, **data):
        super().__init__(**data)
        if 'id' not in data:
            self.id = str(uuid4())
        if 'img' not in data or data['img'] is None:
            equipo = data.get('equipo', 'Unknown')
            self.img = f"/{equipo}/{self.nombre}.png"
        if not self.equipo:
            self.equipo = self.img.split('/')[1].capitalize()  # Extraer y capitalizar el nombre del equipo

class Team(BaseModel):
    nombre: str
    jugadores: List[Player]

class TeamsContainer(BaseModel):
    equipos: Dict[str, Team]
