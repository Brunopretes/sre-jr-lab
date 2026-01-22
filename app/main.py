from fastapi import FastAPI

app = FastAPI(title="Laboratório SRE API")

@app.get("/status")
async def get_status():
    return {
        "status": "ok",
        "service": "laboratorio-sre",
        "message": "Serviço operando normalmente"
    }
@app.get("/")
async def root():
    return {"message": "Bem-vindo ao Lab SRE! Acesse /status para o healthcheck."}

if __name__ == "__main__":
    import uvicorn
    # Inicia o servidor na porta 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
    