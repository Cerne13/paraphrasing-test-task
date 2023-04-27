import uvicorn as uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from routes import parahprasing

app = FastAPI()
app.include_router(parahprasing.router)


@app.get('/', description='Redirects to Swagger documentation from home page')
async def redirect_to_docs():
    response = RedirectResponse(url='/docs')
    return response


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
