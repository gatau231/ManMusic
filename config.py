from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "26689028"))
API_HASH = getenv("API_HASH", "HRKU-326a8859-e979-4132-a9ef-99d3b27bd176")
BOT_TOKEN = getenv("BOT_TOKEN", "7515695303:AAEGslztlvsceODJTmRdDoGhwy0RDJXP04M")
BOT_NAME = getenv("BOT_NAME","idoyx")
BOT_USERNAME = getenv("BOT_USERNAME", "@idoyyyx_bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@akutaker")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "AzumanProject")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "")
PING_IMG = getenv("PING_IMG", "")
SESSION_NAME = getenv("SESSION_NAME", "1BVtsOGoBu5xrQBnKiLmjyGmmp2fpXq5hDYDBvydAVbF5h6eOci290cyXR2YWW0V9eVeVRt6rsSP-_F35s3NfrRgb5v04n-ofDnkfkaU34_fwx7zW5vtwH4LJz_1q371wkdOUnM1Bu39bmFhmRxhjY1Ea-_9jKnIsWB6ghSm2XXw3eGkPMgNLH3KvIyC1HcyqWVlPWDOwF_U1fv-EWvtx480fyba5mNB-mCP5lfB-NgknbQcE3lkPq9G2WRt5uFbogwZLWEpjCZZdJt80HH9NyLft4-XobwpOyzxid55OC5PWoi83V2Iig-XUFsKmKo3GOLFTWz150Gb7jh6IakF8XdC_viQFFeg=")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
