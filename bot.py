import os

from dotenv import load_dotenv

from gen_rfp import RFP
from gen_sow import SOW

from webex_bot.commands.echo import EchoCommand
from webex_bot.models.command import CALLBACK_KEYWORD_KEY, Command, COMMAND_KEYWORD_KEY
from webex_bot.webex_bot import WebexBot


load_dotenv()

bot_email = os.getenv("WEBEX_BOT_EMAIL")
bot_token = os.getenv("WEBEX_BOT_TOKEN")
bot_app_name = os.getenv("WEBEX_BOT_APP_NAME")


# Create a Bot Object
bot = WebexBot(bot_token,bot_name=bot_app_name, approved_users=["jeffrey.ward@ironbow.com", "Anupama.Vijayasekar@ironbow.com", "scott.beauton@ironbow.com"])


# Add new commands for the bot to listen out for.
#bot.add_command(EchoCommand())
bot.add_command(RFP())
bot.add_command(SOW())

# Call `run` for the bot to wait for incoming messages.
bot.run()



