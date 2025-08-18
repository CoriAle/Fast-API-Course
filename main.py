from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl
from typing import Set, List

class Profile(BaseModel):
    name: str = Field(example="John Doe")
    email: str
    age: int

class Image(BaseModel):
    url: HttpUrl
    title: str

class Product(BaseModel):
    name: str
    price: int = Field(title="Price of the item", description="This is the price of the item beign added", gt=0)
    discount: int
    price_discounted: float
    tags: Set[str]
    image: List[Image]

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Phone",
                "price": 100,
                "discount": 5,
                "price_discounted": 0,
                "tags": [
                    "Electronics", 
                    "Computers"
                ],
                "image": [
                    {
                        "url": "https://example.com/",
                        "title": "Product image 1"
                    },
                    {
                        "url": "https://example.com/",
                        "title": "Product image 1"
                    }
                ]
            }
        }

class Offer(BaseModel):
    name: str
    description: str
    price: float
    products: List[Product]

class User(BaseModel):
    name: str
    email: str

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


@app.post('/adduser')
def addUser(profile: Profile):
    return {'user data'}

# Product is the request boyd, product id a path parameter and category a query param 
@app.post('/addproduct/{product_id}')
def addproduct(product: Product, product_id: int, category: str):
    product.price_discounted = product.price - (product.price * product.discount)/100
    return {'product_id': product_id, 'product': product, 'category': category}

# Both product and user are part of the request body (extend baseModel)
@app.post('/purchase')
def purhase(product: Product, user: User):
    return {'product': product, 'user': user}

@app.post('/addoffer')
def addoffer(offer: Offer):
    return offer 