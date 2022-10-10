import logging
import logging.handlers
import os

import requests

from discord import Webhook, RequestsWebhookAdapter

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
    #logger.info("Token not available!")
    #raise

def get_token():
    try:
        TOKEN_K = os.environ["TOKEN_KEY"]
        return TOKEN_K
    except KeyError:
        return None


if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")

    r = requests.get('https://weather.talkpython.fm/api/weather?city=Delhi&country=IN')
    if r.status_code == 200:
        data = r.json()
        temperature = data["forecast"]["temp"]
        TOKEN_K=get_token()
        if TOKEN_K:
            #webhook = Webhook.from_url(f'https://discord.com/api/webhooks/1000714163875754004/{TOKEN_K}', adapter=RequestsWebhookAdapter())
            #webhook.send(f'🚀 Weather in Delhi 🚀: {temperature}')
            logger.info(f'Weather in Delhi: {temperature}')
        else:
            logger.info(f'Token Not Found!')
            
