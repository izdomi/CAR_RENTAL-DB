import os
from dotenv import load_dotenv

load_dotenv()

DB = {
    "host": os.getenv("DATABASE_HOST"),
    "port": int(os.getenv("DATABASE_PORT", "3306")),
    "user": os.getenv("DATABASE_USER"),
    "password": os.getenv("DATABASE_PASSWORD"),
    "database": os.getenv("DATABASE_NAME"),
    "charset": os.getenv("DATABASE_CHARSET"),
}

DB_URI = os.getenv("DATABASE_URI")

APP_ENV = os.getenv("APP_ENV")
