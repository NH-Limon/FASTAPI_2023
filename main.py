from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return "Hello there!🍕"


@app.get('/about')
def about():
    return {'data': {'name': 'About Page'}}
