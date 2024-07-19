import os
import logging
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

import ai

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_CHAT_ID = os.getenv('ADMIN_CHAT_ID')

async def text_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # To prevent processing messages from you
    if ADMIN_CHAT_ID == str(update.effective_user.id):
        return

    text = update.business_message.text
    ai_response = ai.send_message_to_user(update.business_message.from_user.id, text)
    await update.business_message.reply_text(ai_response)


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    text_handler = MessageHandler(filters.TEXT & filters.UpdateType.BUSINESS_MESSAGE, text_message_handler)

    app.add_handler(text_handler)

    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
