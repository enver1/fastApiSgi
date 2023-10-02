from fastapi import FastAPI
from paq_routers import sgiPerfilRoute
app = FastAPI()
app.include_router(sgiPerfilRoute.sgiPerfil_ruta)