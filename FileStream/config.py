from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = int(env.get('API_ID', '29171167'))
    API_HASH = str(env.get("7ea2149629e445936619f06a3c0dc716"))
    BOT_TOKEN = str(env.get("BOT_TOKEN"))
    OWNER_ID = int(env.get('OWNER_ID', '7251898668'))
    WORKERS = int(env.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    DATABASE_URL = str(env.get('mongodb+srv://stream:bot@cluster0.ftlr8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "akmoviebotz"))
    SESSION_NAME = str(env.get('SESSION_NAME', 'ak_filestreambot'))
    FORCE_SUB_ID = env.get('-1001785093771', None)
    FORCE_SUB = env.get('FORCE_UPDATES_CHANNEL', True)
    FORCE_SUB = True if str(FORCE_SUB).lower() == "true" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    FILE_PIC = env.get('FILE_PIC', "https://envs.sh/gAa.jpg")
    START_PIC = env.get('START_PIC', "https://envs.sh/gAO.jpg")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://graph.org/file/736e21cc0efa4d8c2a0e4.jpg")
    MULTI_CLIENT = False
    FLOG_CHANNEL = int(env.get("-1002493002460", None))   # Logs channel for file logs
    ULOG_CHANNEL = int(env.get("-1002210359926", None))   # Logs channel for user logs
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("1049173662", "")).split()))

class Server:
    PORT = int(env.get("PORT", 8080))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
    HAS_SSL = str(env.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "80").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("FQDN", BIND_ADDRESS))
    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )



