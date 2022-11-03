#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""
Description of the bot
"""

import logging

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

# using separate configuration and parser
from configparser import ConfigParser

# configparser
cfg = ConfigParser()
cfg.read('env.cfg')

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # Starting command w/ some instructions
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
    )
    await update.message.reply_text(
        "I am your HealthTracking Bot!\n"
        "/help -- to get a list of available list of commands\n"
        "/cancel -- stopping the conversation with the bot\n"
        '"More features Under construction"'
    )

async def cancel(update: Update, context:ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation", user.first_name)
    await update.message.reply_text(
        "You have finished our dialog!\n See you soon!"
    )
    
    return ConversationHandler.END


def main() -> None:
    # bot functionality starts
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(cfg['TELEGRAM']['token']).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start",  start)],
        states={},
        fallbacks=[],
    )
    application.add_handler(conv_handler)

    # Run the bot until presses Ctrl-C
    application.run_polling()

if __name__ == "__main__":
    main()
        
