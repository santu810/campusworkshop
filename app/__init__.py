"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaanrm7avj5o49ahmq0-a.oregon-postgres.render.com",
        database="todo_2czx",
        user="todo_2czx_user",
        password="ouaan8wxqWKYgTOcYZ90EvNdq4v9yq7U")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
