from flask import Flask
from flask_restplus import Api, Resource

from src.server.instance import server

app. api = server.app, server.api

book_db = [
    {'id': 0, 'tittle': 'Wars and Peace'},
    {'id': 1, 'tittle': 'Clean Code'}
]

class BookList(Resource):
    def get(self, ):
        return book_db   