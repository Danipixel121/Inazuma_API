from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Importa CORSMiddleware
from api.players import router as players_router  # Ajusta la importación según la nueva estructura

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las solicitudes, puedes especificar dominios en lugar de "*"
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los headers
)

# Incluimos el router que maneja los endpoints de los jugadores
app.include_router(players_router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Inazuma Eleven.En /jugadores está todo"}
