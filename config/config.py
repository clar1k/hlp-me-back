from os import environ as env

from dotenv import load_dotenv

load_dotenv('.env.dev')

class Config:
  MONGO_CONNECTION = env.get('MONGO_CONNECTION')
  SECRET_KEY = env.get('SECRET_KEY')
