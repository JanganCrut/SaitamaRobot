# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/SaitamaRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 749081  # integer value, dont use ""
    API_HASH = "140921fbf82d86cc0c951b2e0f3d1d0a"
    TOKEN = "1416293632:AAEvV1T9gzIiVdZxQy0b70Wriad9MMvdyjc"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1124079706  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Oreooo"
    SUPPORT_CHAT = "CritozyPublic"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001206895493
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001206895493
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgresql://misaka:123@0.0.0.0:5432/bot"  # needed for any database modules # its "URI" and not "URL" as herok and similar ones only accept it as such
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "dl57SmYrjiWA3Vfh3OwJPbLRYSPG_xD3tP~t2pHwp3sW3aDQrxB8LMPhAwOT1w7g"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    ALLOW_CHAT = True
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = "CAACAgUAAxkBAAEDH8BhcUvueasvf6iRoYUpVltM4eSkMwACSQIAAouV5QjhTYckY0fjAyEE"  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "VCQ8IZRHFOVS6UQ5"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "DJ8K06TZBRQ6"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "5d28c8c668a84d5129b1412d6c341ca4"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "45bf73b8f5e30f381be4e2ab2b7e12f1d78def13ff7d751c5edffeb0d12f2fe010d914ca7a16c8e09254feb5d2e561c809fdf3368383979c7860250afc7e7b0e"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
