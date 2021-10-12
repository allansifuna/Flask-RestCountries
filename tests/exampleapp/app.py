from flask import Flask
from flask_restcountries import CountriesAPI
app = Flask(__name__)
rapi = CountriesAPI(app)
