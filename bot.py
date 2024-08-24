import logging
from pyrogram import Client, idle, enums
from pyrogram.errors.exceptions.bad_request_400 import BadRequest
from config import app, disabled_plugins, log_chat
from utils import get_restarted, del_restarted

########################################################################################################################
########################################################################################################################

with open("version.txt") as f:
    version = f.read().strip()


async def start_client():
    wr = get_restarted()
    del_restarted() 
    try:
        await app.start()
        await app.send_message(
            log_chat,
            "<b>Bot started</b>\n\n" f"<b>Version:</b> {version}",
        )
        print("Bot started\n" f"Version: {version}") 
        if wr:
            await app.edit_message_text(wr[0], wr[1], "Restarted successfully.")
    except BadRequest:
        logging.warning("Unable to send message to log_chat.")
    await idle()

if __name__ == "__main__":
    app.loop.run_until_complete(start_client())
