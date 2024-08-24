from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import get_bot_information
from plugins.rtp_function import sudo, sudooo, sudooo2


async def destroy_all_group(c: Client, m: Message):
    global mid
    mid = m
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("نعم", callback_data="destroyyes")] +
        [InlineKeyboardButton("لا", callback_data="destroyno")],

    ])
    await m.reply_text("⌯ هل انت متاكد من امر التدمير\n√",
                       reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^destroyyes$"))
async def destroyyes(c: Client, m: CallbackQuery):
    if sudo(m):
        await m.message.delete()
        await mid.delete()
        async for x in c.iter_chat_members(m.message.chat.id):
            try:
                if x.user.id == get_bot_information()[0]:
                    continue
                else:
                    if sudooo2(x.user.id):
                        continue
                    else:
                        await c.ban_chat_member(m.message.chat.id, x.user.id)
            except Exception as er:
                continue
    else:
        await c.answer_callback_query(m.id, text="مش مسموحلك بالزرار الخطير ده", show_alert=True)


@Client.on_callback_query(filters.regex("^destroyno$"))
async def destroyno(c: Client, m: CallbackQuery):
    if sudo(m):
        await m.message.delete()
        await m.message.reply_text("نورت عيوني")
    else:
        await c.answer_callback_query(m.id, text="مش مسموحلك بالزرار الخطير ده", show_alert=True)
