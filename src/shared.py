import os
import requests
import json
import mysql.connector
import configparser
import praw
import logging


LOGGER = logging.getLogger("reddit-tipbot")
LOGGER.setLevel(logging.DEBUG)
try:
    os.makedirs("log", exist_ok=True)
except:
    pass
fh = logging.FileHandler("log/info.log")
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
LOGGER.addHandler(fh)
LOGGER.addHandler(ch)
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "config.ini"))

# if we have a file, use it. Otherwise, load testing defaults
try:
    ENVIRONMENT = config["APPLICATION"]["environment"]
    PYTHON_COMMAND = config["APPLICATION"]["python_command"]
    TIPPER_OPTIONS = config["APPLICATION"]["tipper_options"]
    MESSENGER_OPTIONS = config["APPLICATION"]["messenger_options"]

    TIPBOT_USERNAME = config["BOT"]["username"]
    TIPBOT_OWNER = config["BOT"]["owner"]
    TIPBOT_DONATION_ADDRESS = config["BOT"]["donation_address"]
    PROGRAM_MINIMUM = float(config["BOT"]["program_minimum"])
    RECIPIENT_MINIMUM = float(config["BOT"]["recipient_minimum"])
    TIPBOT_COMMANDS = config["BOT"]["commands"].split(",")
    # DONATE_COMMANDS = config["BOT"]["donate_commands"].split(",")
    # DONATION_ADMINS = config["BOT"]["donation_admins"]
    CURRENCY = config["BOT"]["currency"]
    STATUS_POST_ID = config["BOT"]["status_post_id"]

    MYSQL_USER = config["MYSQL"]["user"]
    MYSQL_PASSWORD = config["MYSQL"]["password"]
    MYSQL_DBNAME = config["MYSQL"]["dbname"]

    NODE_URL = config["NODE"]["url"]
    REPRESENTATIVE = config["NODE"]["representative"]
    USE_DPOW = config["NODE"].getboolean("use_dpow")
    DPOW_ENDPOINT = config["NODE"]["dpow_endpoint"]
    DPOW_TOKEN = config["NODE"]["dpow_token"]
    DPOW_USERNAME = config["NODE"]["dpow_username"]

    try:
        url = "https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}".format(
            CURRENCY, "USD"
        )
        results = requests.get(url, timeout=1)
        results = json.loads(results.text)
        USD_VALUE = float(results["USD"])
    except requests.exceptions.ReadTimeout:
        USD_VALUE = 1
except KeyError as e:
    LOGGER.info("Failed to read config.ini. Falling back to test-defaults...")
    LOGGER.info("Failed on: ", e)

    ENVIRONMENT = "development"
    PYTHON_COMMAND = "python"
    TIPPER_OPTIONS = ">> tipper_output 2>> tipper_error &"
    MESSENGER_OPTIONS = ">> messenger_output 2>> messenger_error &"

    TIPBOT_USERNAME = "nano_tips"
    TIPBOT_OWNER = "playnano"
    TIPBOT_DONATION_ADDRESS = "nano_3pnanopr3d5g7o45zh3nmdkqpaqxhhp3mw14nzr41smjz8xsrfyhtf9xac77"
    PROGRAM_MINIMUM = 0.0001
    RECIPIENT_MINIMUM = 0.0001
    TIPBOT_COMMANDS = ["!ntips", "!nano_tips"]
    # DONATE_COMMANDS = ["!nanocenters"]
    # DONATION_ADMINS = []
    CURRENCY = "Nano"
    STATUS_POST_ID = ""

    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DBNAME = "NanoTips_development"

    NODE_URL = "http://127.0.0.1:7076"
    REPRESENTATIVE = 'nano_3pnanopr3d5g7o45zh3nmdkqpaqxhhp3mw14nzr41smjz8xsrfyhtf9xac77'
    USE_DPOW = False
    DPOW_ENDPOINT = ""
    DPOW_TOKEN = ""
    DPOW_USERNAME = ""

    USD_VALUE = 1

# if in development, commands end with _dev
if ENVIRONMENT == 'development':
    for idx, command in enumerate(TIPBOT_COMMANDS):
        TIPBOT_COMMANDS[idx] = TIPBOT_COMMANDS[idx] + "_dev"
    # for idx, command in enumerate(DONATE_COMMANDS):
    #     DONATE_COMMANDS[idx] = DONATE_COMMANDS[idx] + "_dev"

# only fails if no databases have been created
try:
    MYDB = mysql.connector.connect(
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        host="localhost",
        auth_plugin="mysql_native_password",
        database=MYSQL_DBNAME,
    )
    MYCURSOR = MYDB.cursor()
except mysql.connector.errors.DatabaseError:
    try:
        MYDB = mysql.connector.connect(
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            host="localhost",
            auth_plugin="mysql_native_password",
        )
        MYCURSOR = MYDB.cursor()
    except mysql.connector.errors.DatabaseError:
        MYDB = None
        MYCURSOR = None

if MYCURSOR != None:
    MYCURSOR.execute("SET CHARACTER SET utf8mb4")

try:
    REDDIT = praw.Reddit("nano_tips_bot")
except:\
    REDDIT = None


if CURRENCY == "Nano":

    def to_raw(amount):
        return round(int(amount * 10 ** 30), -20)

    def from_raw(amount):
        return amount / 10 ** 30


elif CURRENCY == "Banano":

    def to_raw(amount):
        return round(int(amount * 10 ** 24), -20)

    def from_raw(amount):
        return amount / 10 ** 24


# initiate the bot and all friendly subreddits
def get_subreddits():
    MYCURSOR.execute("SELECT subreddit FROM subreddits")
    results = MYCURSOR.fetchall()
    MYDB.commit()
    if len(results) == 0:
        class MockSubreddit():
            def comments(self):
                return []
        return MockSubreddit()

    subreddits = "+".join(result[0] for result in results)
    return REDDIT.subreddit(subreddits)


# disable for testing
try:
    SUBREDDITS = get_subreddits()
except (AttributeError, mysql.connector.errors.ProgrammingError) as e:
    SUBREDDITS = None


EXCLUDED_REDDITORS = [
    "xno",
    "nano",
    "nanos",
    "btc",
    "xrb",
    "eth",
    "xrp",
    "eos",
    "ltc",
    "bch",
    "xlm",
    "etc",
    "neo",
    "bat",
    "aed",
    "afn",
    "all",
    "amd",
    "ang",
    "aoa",
    "ars",
    "aud",
    "awg",
    "azn",
    "bam",
    "bbd",
    "bdt",
    "bgn",
    "bhd",
    "bif",
    "bmd",
    "bnd",
    "bob",
    "bov",
    "brl",
    "bsd",
    "btn",
    "bwp",
    "byr",
    "bzd",
    "cad",
    "cdf",
    "che",
    "chf",
    "chw",
    "clf",
    "clp",
    "cny",
    "cop",
    "cou",
    "crc",
    "cuc",
    "cup",
    "cve",
    "czk",
    "djf",
    "dkk",
    "dop",
    "dzd",
    "egp",
    "ern",
    "etb",
    "eur",
    "fjd",
    "fkp",
    "gbp",
    "gel",
    "ghs",
    "gip",
    "gmd",
    "gnf",
    "gtq",
    "gyd",
    "hkd",
    "hnl",
    "hrk",
    "htg",
    "huf",
    "idr",
    "ils",
    "inr",
    "iqd",
    "irr",
    "isk",
    "jmd",
    "jod",
    "jpy",
    "kes",
    "kgs",
    "khr",
    "kmf",
    "kpw",
    "krw",
    "kwd",
    "kyd",
    "kzt",
    "lak",
    "lbp",
    "lkr",
    "lrd",
    "lsl",
    "lyd",
    "mad",
    "mdl",
    "mga",
    "mkd",
    "mmk",
    "mnt",
    "mop",
    "mru",
    "mur",
    "mvr",
    "mwk",
    "mxn",
    "mxv",
    "myr",
    "mzn",
    "nad",
    "ngn",
    "nio",
    "nok",
    "npr",
    "nzd",
    "omr",
    "pab",
    "pen",
    "pgk",
    "php",
    "pkr",
    "pln",
    "pyg",
    "qar",
    "ron",
    "rsd",
    "rub",
    "rwf",
    "sar",
    "sbd",
    "scr",
    "sdg",
    "sek",
    "sgd",
    "shp",
    "sll",
    "sos",
    "srd",
    "ssp",
    "stn",
    "svc",
    "syp",
    "szl",
    "thb",
    "tjs",
    "tmt",
    "tnd",
    "top",
    "try",
    "ttd",
    "twd",
    "tzs",
    "uah",
    "ugx",
    "usd",
    "usn",
    "uyi",
    "uyu",
    "uzs",
    "vef",
    "vnd",
    "vuv",
    "wst",
    "xaf",
    "xcd",
    "xdr",
    "xof",
    "xpf",
    "xsu",
    "xua",
    "yer",
    "zar",
    "zmw",
    "zwl",
]
