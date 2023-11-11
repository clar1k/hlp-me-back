from fastapi import FastAPI
from routes import auth, users
from routes import test, local_dangers
import uvicorn

app = FastAPI(debug=True)

app.include_router(auth.auth)
app.include_router(users.users)
app.include_router(test.router)
app.include_router(local_dangers.router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
