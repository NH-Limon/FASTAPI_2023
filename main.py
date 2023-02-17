from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return "Hello there!🍕"


@app.get('/blog/{id}')
def show(id: int):
    return {'data': 'Blog - ' + str(id)}


@app.get('/blog/{blog_id}/comments/{comment_id}')
def comment(blog_id: int, comment_id: int):
    return {'data': 'Blog ID ' + str(blog_id) + ' and Comment ID ' + str(comment_id)}
