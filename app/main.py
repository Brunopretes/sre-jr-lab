from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import os

app = FastAPI()

# Configuração do Banco de Dados
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://sre_user:sre_password@db:5432/lab_db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelo da tabela de Logs
class AccessLog(Base):
    __tablename__ = "access_logs"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# Criar a tabela se não existir
Base.metadata.create_all(bind=engine)

@app.get("/status")
def get_status():
    # Salva o acesso no banco
    db = SessionLocal()
    new_log = AccessLog()
    db.add(new_log)
    db.commit()
    db.close()
    
    return {
        "status": "online",
        "database": "connected",
        "message": "Acesso registrado no Postgres!"
    }