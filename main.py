from fastapi import FastAPI
from routes import auth, users
import uvicorn

app = FastAPI(debug=True)

app.include_router(auth.auth)
app.include_router(users.users)

if __name__=='__main__':
  uvicorn.run('main:app', reload=True)  