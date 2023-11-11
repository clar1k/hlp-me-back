from dotenv import load_dotenv
from os import environ as env

load_dotenv('.env.dev')

# if not load_dotenv(".env.development"):
#     raise Exception("Could not find dotenv file")


class Config:
  MONGO_CONNECTION = env.get('MONGO_CONNECTION')
  SECRET_KEY = env.get('SECRET_KEY')