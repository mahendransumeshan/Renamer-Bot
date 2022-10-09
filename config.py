import os

class Config(object):

    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5758713151:AAGqv_s4BqhZDGcf1_pebwzIYY5Z2PwSIXc")

    APP_ID = int(os.environ.get("APP_ID", 10396835))
    
    API_HASH = os.environ.get("API_HASH","d31bbec822ee6b1e9c70dd1ba3018aea")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 3600
    
    TG_MAX_FILE_SIZE = 2097152000

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    DB_URI = os.environ.get("DATABASE_URL", "postgres://abgwpysf:jBKrj0LRkvKqqCMuq8waY37V1CQPijuu@jelani.db.elephantsql.com/abgwpysf")

    UPDATE_GROUP = os.environ.get("UPDATE_GROUP", "sdsfhtuyh")
    
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "sdsfhtuyhd")

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5526901717").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
