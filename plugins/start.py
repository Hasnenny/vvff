from pyrogram import Client, filters, enums
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message, ReplyKeyboardMarkup,\
    KeyboardButton
from config import prefix, developer, get_bot_information 
from database import get_db_botname
from plugins.commands import command2
from plugins.general import confirm_user


@Client.on_message(filters.command("start", prefix) & filters.user(developer))
async def startsudo(c: Client, m: Message):
    await confirm_user(c, m)
    if m.chat.type == enums.ChatType.PRIVATE:
        t = """↯︙ اهلا بك عزيزي ↫ ⦗ {await get_Rank(user_data2)} ⦘
– – – – – –
↯︙ يمكنك التحكم في بوت ↫ ⦗ {botname} ⦘
↯︙ عبر الازرار في الاسفل"""
        keyboard = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton("⏬ قفل الكيبورد ⏬")],
            [KeyboardButton("تعطيل التواصل 🔰")] +
            [KeyboardButton("تفعيل التواصل ⚡️")],
            [KeyboardButton("تعطيل الاذاعه 🔕")] +
            [KeyboardButton("تفعيل الاذاعه 🔔")],
            [KeyboardButton("تعطيل اليوتيوب 🛠")] +
            [KeyboardButton("تفعيل اليوتيوب ⚙️")],
            [KeyboardButton("المطورين 🔱")],
            [KeyboardButton("اذاعه خاص 🔊")] +
            [KeyboardButton("اذاعه بالمجموعات 📡")],
            [KeyboardButton("اذاعه بالتوجيه خاص 👤")] +
            [KeyboardButton("اذاعه بالتوجيه للمجموعات ⁦♻️⁩")],
            [KeyboardButton("اذاعه موجهه بالتثبيت ⁦♻️⁩")] +
            [KeyboardButton("اذاعه بالتثبيت 📎")],
            [KeyboardButton("الاحصائيات 📊")],
            [KeyboardButton("المشتركين ⁦🗣️⁩")] +
            [KeyboardButton("الجروبات 📢")],
            [KeyboardButton("حذف الاعضاء الفيك ⚡️")] +
            [KeyboardButton("حذف الجروبات الفيك ⚡️")],
            [KeyboardButton("حذف رد عام 🚫")] +
            [KeyboardButton("اضف رد عام 💬")],
            [KeyboardButton("الردود العامه 📝")],
            [KeyboardButton("قائمه الكتم العام 🛑")] +
            [KeyboardButton("قائمه الحظر العام 🚫")],
            [KeyboardButton("ضع اسم للبوت 🤖")],
            [KeyboardButton("معلومات السيرفر ℹ️")] +
            [KeyboardButton("سرعه السيرفر 🚀️")],
            [KeyboardButton("جلب نسخه احتياطيه اساسيه 📬")],
            [KeyboardButton("رفع نسخه احتياطيه ⛓")],
            [KeyboardButton("الاصدار ⁦⚙️⁩")] +
            [KeyboardButton("تحديث السورس 📥")],
            [KeyboardButton("رستر البوت 🕹")],
            [KeyboardButton("الغاء ⁦🛠️⁩")],
        ],
            resize_keyboard=True,
            one_time_keyboard=False
        )
        await m.reply_text(t, reply_markup=keyboard, parse_mode=enums.ParseMode.MARKDOWN)
    else:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("🤖 ابدأ محادثة", url=f"https://t.me/{get_bot_information()[1]}?start=start")]])
        await m.reply_text("مرحبا! أنا بلاك. لاكتشاف وظائفي ، ابدأ محادثة معي.", reply_markup=keyboard)


@Client.on_message(filters.command("start", prefix) & ~filters.user(developer))
async def start(c: Client, m: Message):
    await confirm_user(c, m)
    if m.chat.type == enums.ChatType.PRIVATE:
        botname = get_db_botname() or "بلاك"
        x = f"""
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
︙اختصاصي حماية المجموعات
︙من التفليش والفشار والخخ .. . ،
︙تفعيلي سهل ومجانا فقط قم برفعي ادمن في مجموعتك وارسل امر ↫ تفعيل
︙سيتم تفعيل البوت من ثم اختر ترتيب الاوامر ورفع الادمنية..
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
        """
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("الاوامر 📚", callback_data="commandss")] + [InlineKeyboardButton("ℹ️ حول", callback_data="infos")], [InlineKeyboardButton("تغير اللغه 🌐", callback_data="chlang")], [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=dream")]])
        async for photo in c.get_chat_photos(get_bot_information()[1], limit=1):
            await m.reply_photo(photo.file_id, caption=x, reply_markup=keyboard)
    else:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("🤖 ابدأ محادثة", url=f"https://t.me/{get_bot_information()[1]}?start=start")]])
        await m.reply_text("مرحبا! أنا فالكيري. لاكتشاف وظائفي ، ابدأ محادثة معي.", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^start_back$"))
async def start_back(c: Client, m: CallbackQuery):
    botname = get_db_botname() or "فالكيري"
    x = f"""
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
🎤╖ أهلآ بك عزيزي أنا بوت {botname}
⚙️╢ وظيفتي حماية المجموعات
✅╢ لتفعيل البوت عليك اتباع مايلي 
🔘╢ أضِف البوت إلى مجموعتك
⚡️╢ ارفعهُ » مشرف
⬆️╜ سيتم ترقيتك مالك في البوت
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
    """
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("الاوامر 📚", callback_data="commandss")] + [InlineKeyboardButton("ℹ️ حول", callback_data="infos")], [InlineKeyboardButton("تغير اللغه 🌐", callback_data="chlang")], [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=dream")]])
    async for photo in c.get_chat_photos(get_bot_information()[1], limit=1):
        await m.message.edit_text(x, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^infos$"))
async def infos(c: Client, m: CallbackQuery):
    res = """
- [Source Black](t.me/aa_ggc)
- [BlackBerry updates](t.me/aa_ggc)
- [Black](t.me/OOQ_OC)
Welcome to Source Black 
        """
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("« عوده", callback_data="start_back")]])
    await m.message.edit_text(res, reply_markup=keyboard, disable_web_page_preview=True, parse_mode=enums.ParseMode.MARKDOWN)


@Client.on_callback_query(filters.regex("^commandss$"))
async def commandsss(c: Client, m: CallbackQuery):
    await command2(c, m)
