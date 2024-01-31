import os
from dotenv import load_dotenv

class Settings:

    load_dotenv()
    port = os.getenv("PORT")

settings = Settings()
