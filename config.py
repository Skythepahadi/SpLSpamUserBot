import os

class API:
    API_ID = int(os.getenv("API_ID", "28682883"))
    API_HASH = os.getenv("API_HASH", "f965ac4aeca63bdd81f0b1c284294efe")

class TOKENS:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "6185038239:AAGxR9oPVc-s4pVv8AhZyKB1A5i0834GHug")
    STRING_SESSION = os.getenv("STRING_SESSION", "BQBubP9_CqilAlou-4rwxyH6n48kaZ05ikTGjbZcTuV-qMW8UQS8jyHW-fOrZDdZ1Spme0cUi3oBdt4yT7ZVVJSoa0GDH-TAyog5Ovrx-IvITBGLpeahsgU_mzKHr9CA2hzU8aC4OoOdl9MgUWHVIpGIBc47DOeZjTThbnAMG2zHwXbOzitsiuJ8yM9Eh3RN2sVvrRnZhnYQJPnsYoe-S9gvQI-7W7P6ZUD38Rnk5Ibo9rlScRJA_6Kd5fjAKjBe7A7WFSxdfSHA5RqZZJp5mN2aY05qrWkkQ0Z0Aga2VJ_knr5AQRPyvL2660X4RsEGrmMYfFTeVMHqDgiRhk-E-IgCAAAAAVEqjngA")
    STRING_SESSION_2 = os.getenv("STRING_SESSION_2", "")
    STRING_SESSION_3 = os.getenv("STRING_SESSION_3", "")
    STRING_SESSION_4 = os.getenv("STRING_SESSION_4", "")
    STRING_SESSION_5 = os.getenv("STRING_SESSION_5", "")
    STRING_SESSION_6 = os.getenv("STRING_SESSION_6", "")
    STRING_SESSION_7 = os.getenv("STRING_SESSION_7", "")
    STRING_SESSION_8 = os.getenv("STRING_SESSION_8", "")
    STRING_SESSION_9 = os.getenv("STRING_SESSION_9", "")
    STRING_SESSION_10 = os.getenv("STRING_SESSION_10", "")

class DATABASE:
    MONGO_DB_URL = os.getenv("MONGO_DB_URL", "mongodb+srv://skypahadi:prabhatchamoli41@cluster0.aunjres.mongodb.net/?retryWrites=true&w=majority")

class DEV:
    OWNER_ID = int(os.getenv("OWNER_ID", "5656710776"))
    
    # DONT EDIT THIS 
    SUDO_USERS = [] 
    # YOU CAN ADD SUDO USING /addsudo

class STUFF:
    ALIVE_PIC = os.getenv("ALIVE_PIC", "https://graph.org/file/8fd33da8e4e7f6512ced5.jpg")
    HELP_PIC = os. getenv("HELP_PIC", "https://graph.org/file/479fdc2efe0cd9769f3dc.jpg")
    START_PIC = os. getenv("START_PIC", "https://graph.org/file/28d473d129643123bc425.jpg")
    COMMAND_HANDLER = os. getenv("COMMAND_HANDLER", "!")
    ALLOW_PORN = os.getenv("ALLOW_PORN", True) # CHANGE 'True' TO 'False' IF YOU WANNA DISABLE PORN
