import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from routes import auth, global_dangers, local_dangers, users

app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(auth.auth)
app.include_router(users.users)
app.include_router(local_dangers.router)
app.include_router(global_dangers.router)


@app.get('/')
def index():
    return RedirectResponse(url='/docs')


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
