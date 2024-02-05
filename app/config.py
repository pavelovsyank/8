import os
from dotenv import load_dotenv

class Settings:

    load_dotenv()
    port =int(os.getenv("PORT")) 
    secret =os.getenv("SECRET")
    host=os.getenv("HOST")

settings = Settings()
