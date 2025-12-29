import os
import re
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ---------- SAFE HELPERS ----------

def get_int(name, default):
    val = os.getenv(name)
    try:
        return int(val) if val and val.strip() else default
    except ValueError:
        return default

def get_bool(name, default=False):
    val = os.getenv(name)
    if val is None:
        return default
    return val.lower() in ("true", "1", "yes", "y")

# ---------- REQUIRED ----------

API_ID = get_int("API_ID", 27806628)
API_HASH = os.getenv("API_HASH", "25d88301e886b82826a525b7cf52e090")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8577192556:AAH_VGCGYNA_s-_NFXeyXMb12_J7UIGK4Og")

OWNER_ID = get_int("OWNER_ID", 8525952693)
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "funnytamilan")
BOT_USERNAME = os.getenv("BOT_USERNAME", "tfc_x_musicbot")

# ---------- DATABASE ----------

MONGO_DB_URI = os.getenv(
    "MONGO_DB_URI",
    "mongodb+srv://ajmalitsme_db_user:cvGvDymXtfTbfcys@cluster0.2qz2d97.mongodb.net/?appName=Cluster0"
)

LOG_GROUP_ID = get_int("LOG_GROUP_ID", -1003369263462)

# ---------- HEROKU / GIT ----------

HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/NoxxOP/ShrutiMusic")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN")

# ---------- LINKS ----------

SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/ShrutiBots")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/ShrutiBotSupport")
INSTAGRAM = os.getenv("INSTAGRAM", "https://instagram.com/yaduwanshi_nand")
YOUTUBE = os.getenv("YOUTUBE", "https://youtube.com/@NandEditz")
GITHUB = os.getenv("GITHUB", "https://github.com/NoxxOP")
DONATE = os.getenv("DONATE", "https://t.me/ShrutiBots/91")
PRIVACY_LINK = os.getenv("PRIVACY_LINK", "https://graph.org/Privacy-Policy-05-01-30")

# ---------- LIMITS ----------

DURATION_LIMIT_MIN = get_int("DURATION_LIMIT", 300)
PLAYLIST_FETCH_LIMIT = get_int("PLAYLIST_FETCH_LIMIT", 25)

TG_AUDIO_FILESIZE_LIMIT = get_int("TG_AUDIO_FILESIZE_LIMIT", 104857600)
TG_VIDEO_FILESIZE_LIMIT = get_int("TG_VIDEO_FILESIZE_LIMIT", 2145386496)

# ---------- SPOTIFY ----------

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# ---------- STRING SESSIONS ----------

STRING1 = os.getenv("STRING_SESSION")
STRING2 = os.getenv("STRING_SESSION2")
STRING3 = os.getenv("STRING_SESSION3")
STRING4 = os.getenv("STRING_SESSION4")
STRING5 = os.getenv("STRING_SESSION5")

# ---------- FLAGS ----------

AUTO_LEAVING_ASSISTANT = get_bool("AUTO_LEAVING_ASSISTANT", False)
START_STICKER_ENABLED = get_bool("START_STICKER_ENABLED", True)

# ---------- IMAGES ----------

START_IMG_URL = os.getenv("START_IMG_URL", "https://files.catbox.moe/7q8bfg.jpg")

PING_IMG_URL = PLAYLIST_IMG_URL = STATS_IMG_URL = (
    TELEGRAM_AUDIO_URL
) = TELEGRAM_VIDEO_URL = STREAM_IMG_URL = (
    SOUNCLOUD_IMG_URL
) = YOUTUBE_IMG_URL = (
    SPOTIFY_ARTIST_IMG_URL
) = SPOTIFY_ALBUM_IMG_URL = (
    SPOTIFY_PLAYLIST_IMG_URL
) = "https://files.catbox.moe/eehxb4.jpg"

# ---------- RUNTIME ----------

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

TEMP_DB_FOLDER = "tempdb"

# ---------- TIME ----------

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

ERROR_FORMAT = int("7574330905")

# ---------- URL VALIDATION ----------

for name, url in {
    "SUPPORT_CHANNEL": SUPPORT_CHANNEL,
    "SUPPORT_GROUP": SUPPORT_GROUP,
}.items():
    if url and not re.match(r"https?://", url):
        raise SystemExit(f"[ERROR] - {name} must start with https://")
