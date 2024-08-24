import random
import re
from pyrogram import Client, enums
from pyrogram.types import Message
from database import get_db_addcustomid, get_db_mypointgame, get_db_mymessage, get_db_mycontact
from config import get_bot_information
from plugins.locks import *
from plugins.admin import get_available_adminstrator
from plugins.rtp_function import get_Rank


def get_mycontact(m):
    if get_db_mycontact(m.from_user.id, m.chat.id) is None:
        num = 0
    else:
        num = get_db_mycontact(m.from_user.id, m.chat.id)
    return num


def get_mypoint(m):
    if get_db_mypointgame(m.from_user.id, m.chat.id) is None:
        num = 0
    else:
        num = get_db_mypointgame(m.from_user.id, m.chat.id)
    return num


def get_mymessage(m):
    if get_db_mymessage(m.from_user.id, m.chat.id) is None:
        num = 0
    else:
        num = get_db_mymessage(m.from_user.id, m.chat.id)
    return num


def get_mymessage_interaction(m):
    interaction_msg = ''
    if m < 100:
        interaction_msg = 'سايق مخدة 😹'
    else:
        if m < 200:
            interaction_msg = 'عفيه اتفاعل 😽'
        else:
            if m < 400:
                interaction_msg = 'عفيه اتفاعل 😽'
            else:
                if m < 700:
                    interaction_msg = ' بدأ يتحسن 😐'
                else:
                    if m < 1200:
                        interaction_msg = ' شكد تحجي 😒'
                    else:
                        if m < 2000:
                            interaction_msg = 'استمر بطل 😍'
                        else:
                            if m < 3500:
                                interaction_msg = 'تفاعل غنبله 🧡'
                            else:
                                if m < 4000:
                                    interaction_msg = ' جيد جدا ♥️'
                                else:
                                    if m < 4500:
                                        interaction_msg = ' ممتاز جدا 🥰'
                                    else:
                                        if m < 5500:
                                            interaction_msg = 'استمر يعسل 🥳'
                                        else:
                                            if m < 7000:
                                                interaction_msg = ' مــلــک 💯😻'
                                            else:
                                                if m < 9500:
                                                    interaction_msg = 'ملك التلكرام 💖'
                                                else:
                                                    if m < 10000000000:
                                                        interaction_msg = 'ملك التلكرام 💖'
    return interaction_msg


async def ids_private(c: Client, m: Message):
    user_data = m.from_user
    await m.reply_text(f"**معلومات:**\n**الاسم:** `{user_data.first_name} {user_data.last_name or ''}`\n**المعرف:** {'@' + user_data.username if user_data.username else 'فارغ'}\n**الايدي:** `{user_data.id}`\n**المركز:** `{user_data.dc_id or 'غير معروف'}`\n**اللغه:** `{user_data.language_code or 'غير معروف'}`\n**نوع الشات:** `{m.chat.type}`", parse_mode=enums.ParseMode.MARKDOWN)


async def ids_default(c: Client, m: Message):
    randomtext = [
        '↫ فديـت الصــاڪ مِححـہ🥰',
        "↫ صــــــــاڪ عـمــــــي 😉🔥",
        "↫ منــــــــور اليـــــــــــوم 💡🙈",
        "↫ تـحبنـــــــــــــــــــيٰ؟😉🙈",
        "↫ يمـه يمـه شڪد حـلــو 🍫💖",
        "↫ فـــديـــــت الحــلـــــــو 🥰",
        "↫ ببـڪــــــن خــــــــاص 😉😹"
    ]
    if m.reply_to_message:
        user_data = m.reply_to_message.from_user
        user_data2 = m.reply_to_message
    else:
        user_data = m.from_user
        user_data2 = m

    if user_data.first_name:
        first_name = user_data.first_name + " "
    else:
        first_name = " "
    if user_data.last_name:
        last_name = user_data.last_name
    else:
        last_name = ""

    if user_data.username:
        username = user_data.username
    else:
        username = "لايوجد"

    check = await get_available_adminstrator(c, m)
    if check[0]:
        adminrom = "مشرف"
    else:
        adminrom = "عضو"

    medooid = f"""
{random.choice(randomtext)}
✧︙ايديك : ❨ {user_data.id} ❩
✧︙معرفك : ❨ @{username} ❩
✧‍︙رتبتك : ❨ {await get_Rank(user_data2)} ❩
✧︙تفاعلك : ❨ {get_mymessage_interaction(get_mymessage(m))} ❩
✧︙رسائلك : ❨ {get_mymessage(m)} ❩
✧︙نقاطك : ❨ {get_mypoint(m)} ❩
        """

    medooid2 = f"""
{random.choice(randomtext)}
✧︙ايديك : ❨ {user_data.id} ❩
✧︙معرفك : ❨ @{username} ❩
✧‍︙رتبتك : ❨ {await get_Rank(user_data2)} ❩
✧︙تفاعلك : ❨ {get_mymessage_interaction(get_mymessage(m))} ❩
✧︙رسائلك : ❨ {get_mymessage(m)} ❩
✧︙نقاطك : ❨ {get_mypoint(m)} ❩
            """

    elnagarid = f"""
✧︙ايديك : ❨ {user_data.id} ❩
✧︙معرفك : ❨ @{username} ❩
✧‍︙رتبتك : ❨ {await get_Rank(user_data2)} ❩
✧︙تفاعلك : ❨ {get_mymessage_interaction(get_mymessage(m))} ❩
✧︙رسائلك : ❨ {get_mymessage(m)} ❩
✧︙نقاطك : ❨ {get_mypoint(m)} ❩
            """

    try:
        await c.get_chat_photos(user_data.id, limit=1).__anext__()
    except:
        await m.reply_text(medooid, parse_mode=enums.ParseMode.MARKDOWN)
        return
    if lock_idgroup2_test(m):
        await m.reply_text(elnagarid, parse_mode=enums.ParseMode.MARKDOWN)
        return
    async for photo in c.get_chat_photos(user_data.id, limit=1):
        await m.reply_photo(photo.file_id, caption=medooid2, parse_mode=enums.ParseMode.MARKDOWN)
    return


async def ids(c: Client, m: Message):
    if get_db_addcustomid(m.chat.id) is None:
        await ids_default(c, m)
    else:
        for per in get_db_addcustomid(m.chat.id):
            if per[1] == m.chat.id:
                randomtext = [
                    '↫ ببـڪــــــن خــــــــاص 😉😹',
                    "↫ فـــديـــــت الحــلـــــــو 🥰",
                    "↫ فديـت الصــاڪ مِححـہ🥰",
                    "↫ صــــــــاڪ عـمــــــي 😉🔥",
                    "↫ منــــــــور اليـــــــــــوم 💡🙈",
                    "↫ تـحبنـــــــــــــــــــيٰ؟😉🙈",
                    "↫ يمـه يمـه شڪد حـلــو 🍫💖"
                ]
                if m.reply_to_message:
                    user_data = m.reply_to_message.from_user
                    user_data2 = m.reply_to_message
                else:
                    user_data = m.from_user
                    user_data2 = m

                if user_data.first_name:
                    first_name = user_data.first_name + " "
                else:
                    first_name = " "
                if user_data.last_name:
                    last_name = user_data.last_name
                else:
                    last_name = ""

                if user_data.username:
                    username = user_data.username
                else:
                    username = "لايوجد"

                check = await get_available_adminstrator(c, m)
                if check[0]:
                    adminrom = "مشرف"
                else:
                    adminrom = "عضو"
                a = re.sub("#rdphoto", random.choice(randomtext), per[0])
                a = re.sub("#fname", str(first_name), a)
                a = re.sub("#lname", str(last_name), a)
                a = re.sub("#id", str(m.from_user.id), a)
                a = re.sub("#user", "@" + str(username), a)
                a = re.sub("#mention", f"[{first_name + last_name}](tg://user?id={m.from_user.id})", a)
                a = re.sub("#game", str(get_mypoint(m)), a)
                a = re.sub("#msgs", str(get_mymessage(m)), a)
                a = re.sub("#contact", str(get_mycontact(m)), a)
                a = re.sub("#auto", str(get_mymessage_interaction(get_mymessage(m))), a)
                a = re.sub("#brank", str(await get_Rank(user_data2)), a)
                a = re.sub("#grank", str(adminrom), a)
                a = re.sub("#gmsgs", str(m.id + 1), a)

                if not await c.get_profile_photos(user_data.id, limit=1):
                    await m.reply_text(a, parse_mode=enums.ParseMode.MARKDOWN)
                    return

                async for photo in c.get_chat_photos(user_data.id, limit=1):
                    await m.reply_photo(photo.file_id, caption=a, parse_mode=enums.ParseMode.MARKDOWN)
                    return
        await ids_default(c, m)
