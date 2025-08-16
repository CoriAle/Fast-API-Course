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
def profilePage(username: str):
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
def userprofile(username):
    return { f'This is a profile page for {username}' }

# Id and price are query parameters since they are not defined in the path
@app.get('/products')
def products(id: int = 1, price: int = None): # With default values
    return { f'This is a product with id: {id} and price: {price}' }

@app.get('/profile/{userid}/comments')
def profile(userid: int, commentid: int):
    return { f'This is a page for user with id: {userid} with comment id: {commentid}'}