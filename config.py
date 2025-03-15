from os import environ 

class Config:
    API_ID = environ.get("API_ID", "20373203")
    API_HASH = environ.get("API_HASH", "8962717c7c708e210f66ea658db58d85")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7610408338:AAECyIf_nfgsNQjgScox1vBXCvvoGxgqg4M") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://gipowel806:m1J2VOO1EsgSN23g@cluster0.pzgcw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7369976226').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
