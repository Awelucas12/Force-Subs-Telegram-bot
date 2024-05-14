import logging
from pyrogram import Client
from Config import Config

logging.basicConfig(level=logging.INFO)

plugins = dict(
    root="plugins",
    include=[
        "forceSubscribe",
        "help"
    ]
)

app = Client(
     'ForceSubscribe',
      bot_token = Config.6762280608:AAHOX5G1JKqT3R9uOt-MbgthGkSqWO97T38,
      api_id = Config.24115927,
      api_hash = Config.749eb2e9353e4006adb00fc8b11c9333,
      plugins = plugins
)

app.run()
