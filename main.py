from fastapi import FastAPI
from routes import test
import uvicorn

app = FastAPI(debug=True)

app.include_router(test.router)
if __name__=='__main__':
  uvicorn.run('main:app', reload=True)