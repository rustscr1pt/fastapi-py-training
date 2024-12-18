from fastapi import FastAPI
from handlers.ping import router as ping_router
from handlers.tasks import router as task_router
app = FastAPI()

app.include_router(router=ping_router)
app.include_router(router=task_router)