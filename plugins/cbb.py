#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : @Khesari_lal_fan\n○ Library : <a href='https://t.me/Anime_Srinnes'>Pyrogram asyncio {__version__}</a>\n○ Source Code : <a href='https://t.me/Anime_Srinnes'>Click here</a>\n○ Channel : @Anime_Shrinnes\n○ Support Group : @Shrines_discussion</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
