from typing import List
from fastapi import FastAPI
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime, ARRAY, create_engine, select

engine = create_engine('postgresql://scqbykeqqlvmhy:14c7a2b194592d6d23f7a02c19590e6cc860faa3acdf97cae5c4f21aa1a97999@ec2-44-194-201-94.compute-1.amazonaws.com:5432/d6v3fr4b5uvlc6')
Base = declarative_base()
app = FastAPI()


class Product(Base):
    __tablename__ = 'Product'

    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
    description = Column(String(512), nullable=False)
    price = Column(Float(), nullable=False)
    stock = Column(Integer(), nullable=False)
    post_date = Column(DateTime(), default=datetime.datetime.now())
    images = Column(ARRAY(), default=[])

    def __str__(self) -> str:
        return self.name


@app.get('/api/products')
def get_products(id: int = None):
    if id == None:
        return 'All the products'
    else:
        return 'Product number ' + str(id)


@app.put('/api/buy')
def update_product_bought(id: int):
    return 'El producto ' + str(id) + ' fue comprado con exito.'


@app.get('/api/user')
def get_user(id: int):
    return 'User id ' + str(id)


    

