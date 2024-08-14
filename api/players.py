from fastapi import APIRouter, HTTPException, Query
from api.models import Player
import json
from pathlib import Path

router = APIRouter()
file_path = Path("api/jugadores.json")

# Cargar jugadores desde el archivo JSON
def cargar_jugadores():
    if file_path.exists():
        with open(file_path, "r") as file:
            return json.load(file)
    return {}

jugadores_por_equipo = cargar_jugadores()

@router.get("/jugadores", response_model=list[Player])
def obtener_jugadores(equipo: str = Query(None, description="Nombre del equipo")):
    if equipo is None:
        # Devuelve todos los jugadores de todos los equipos
        todos_los_jugadores = [Player(**jugador) for equipo in jugadores_por_equipo.values() for jugador in equipo]
        return todos_los_jugadores
    if equipo in jugadores_por_equipo:
        return [Player(**jugador) for jugador in jugadores_por_equipo[equipo]]
    raise HTTPException(status_code=404, detail="Equipo no encontrado")

@router.get("/jugadores/{jugador_id}", response_model=Player)
def obtener_jugador(jugador_id: str, equipo: str = Query(None, description="Nombre del equipo")):
    if equipo is None:
        # Busca en todos los equipos
        for jugadores in jugadores_por_equipo.values():
            jugador = next((j for j in jugadores if j["id"] == jugador_id), None)
            if jugador:
                return Player(**jugador)
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    if equipo in jugadores_por_equipo:
        jugador = next((j for j in jugadores_por_equipo[equipo] if j["id"] == jugador_id), None)
        if jugador:
            return Player(**jugador)
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    raise HTTPException(status_code=404, detail="Equipo no encontrado")
