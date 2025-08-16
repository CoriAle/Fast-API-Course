from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return 'Hello world! :)'


@app.get('/property')
def property():
    return 'This is a property page'

@app.get('/movies')
def movies():
    return { 'movies': ['Movie 1', 'Movie 2'] }