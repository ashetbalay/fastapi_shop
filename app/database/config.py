import os

from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")
HOST = os.getenv("HOST")

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
