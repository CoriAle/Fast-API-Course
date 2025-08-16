from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return 'Hello world! :)'

# Id is a path parameter
@app.get('/property/{id}')
def property(id: int):
    return { f'This is a property page {id}' }

@app.get('/profile/{username}')
def profile(username: str):
    return { f'This is the profile page for username: {username}'}

@app.get('/movies')
def movies():
    return { 'movies': ['Movie 1', 'Movie 2'] }

# Static route
@app.get('/user/admin')
def admin():
    return { f'This is the admin page' }

# Dynamic Route
@app.get('/user/{username}')
def profile(username):
    return { f'This is a profile page for {username}' }