import os

class API:
    API_ID = int(os.getenv("API_ID", "28682883"))
    API_HASH = os.getenv("API_HASH", "f965ac4aeca63bdd81f0b1c284294efe")

class TOKENS:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "6185038239:AAGxR9oPVc-s4pVv8AhZyKB1A5i0834GHug")
    STRING_SESSION = os.getenv("STRING_SESSION", "BQG1qoMAPqGF30AGbzwqEp07lcYoBkOhzQ9Aafo08BsjyvkJCm1MjYUOTbH2wAwwZ8AVEFobMjAuOLjVoe3pf7UEswiLSVW3IKiExAUqhAzOK3ViQ1ux5A9AJ-pAve_q636fGJGYVDfLTmRCUlyB9_XpfvXDeiaTtQP0nmeJrNvZLFKmEG6Emr8m4Mb_ZpedwITACGzZKQ_MZWNGhIjuCCXfiivB1X-12CFdMHG3TIbktkUvm2ckpICy3a4cBoMT0jppGJ7uVVHgNofG-iRsRUYFwlzOSSn6j9QbMmPIZzCdBrIR_1x-dWiQ6hyZ2uZKj_fOZ_-8I-yvSmPoEjmsZcUdqoiiYwAAAAFRKo54AA"
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
