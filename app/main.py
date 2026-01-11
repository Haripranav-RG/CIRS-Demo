

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.user_router import router as user_router

app = FastAPI()

# ✅ CORS MUST BE HERE (before include_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # for development
    allow_credentials=True,
    allow_methods=["*"],   # IMPORTANT
    allow_headers=["*"],   # IMPORTANT
)

# ✅ Now include routers
app.include_router(user_router)

# from fastapi import FastAPI
# from app.db.session import engine
# from app.db.base import Base
# from app.routers.user_router import router as user_router

# Base.metadata.create_all(bind=engine)

# app = FastAPI(title="CIRS Backend")

# app.include_router(user_router)