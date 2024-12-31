import os

class API:
    API_ID = int(os.getenv("API_ID", ""))
    API_HASH = os.getenv("API_HASH", "")

class TOKENS:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    STRING_SESSION = os.getenv("STRING_SESSION", ""
    STRING_SESSION_3 = os.getenv("STRING_SESSION_3", "")
    STRING_SESSION_4 = os.getenv("STRING_SESSION_4", "")
    STRING_SESSION_5 = os.getenv("STRING_SESSION_5", "")
    STRING_SESSION_6 = os.getenv("STRING_SESSION_6", "")
    STRING_SESSION_7 = os.getenv("STRING_SESSION_7", "")
    STRING_SESSION_8 = os.getenv("STRING_SESSION_8", "")
    STRING_SESSION_9 = os.getenv("STRING_SESSION_9", "")
    STRING_SESSION_10 = os.getenv("STRING_SESSION_10", "")

class DATABASE:
    MONGO_DB_URL = os.getenv("MONGO_DB_URL", "")

class DEV:
    OWNER_ID = int(os.getenv("OWNER_ID", ""))
    
    # DONT EDIT THIS 
    SUDO_USERS = [] 
    # YOU CAN ADD SUDO USING /addsudo

class STUFF:
    ALIVE_PIC = os.getenv("ALIVE_PIC", "https://graph.org/file/8fd33da8e4e7f6512ced5.jpg")
    HELP_PIC = os. getenv("HELP_PIC", "https://graph.org/file/479fdc2efe0cd9769f3dc.jpg")
    START_PIC = os. getenv("START_PIC", "https://graph.org/file/28d473d129643123bc425.jpg")
    COMMAND_HANDLER = os. getenv("COMMAND_HANDLER", "!")
    ALLOW_PORN = os.getenv("ALLOW_PORN", True) # CHANGE 'True' TO 'False' IF YOU WANNA DISABLE PORN
