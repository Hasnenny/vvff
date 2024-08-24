from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import get_bot_information

################################
## Dev By: @S550D ##
################################

@Client.on_callback_query(filters.regex("^command (\\d+)$"))
async def command(c: Client, m: Message):
    global mid
    mid = m.id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⨳ م1", callback_data="m1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⨳ م2", callback_data="m2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⨳ م3", callback_data="m3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⨳ م4", callback_data="m4 " + str(m.from_user.id))],
        [InlineKeyboardButton("⨳ م5", callback_data="m5 " + str(m.from_user.id))], 

        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.reply_text("""
    ⌔︙اوامــر البــوت الرئيسيـة 
—————————————
⌔︙اختر ماتريد عرضه من القائمه :

⌔︙قناة السورس والتحديثات
@aa_ggc - @aa_ggc
—————————————

""", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^command2 (\\d+)$"))
async def command2(c: Client, m: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("القفـل / الفتـح", callback_data="m1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اوامر التحشيش", callback_data="m2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اوامر الاعضـاء", callback_data="m3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اوامر الـمالكيـن", callback_data="m4 " + str(m.from_user.id))],
        [InlineKeyboardButton("اوامر المطـرين", callback_data="m5 " + str(m.from_user.id))], 

        [InlineKeyboardButton("اضف البوت الي مجموعتك ⌯", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
    ⌔︙اوامــر البــوت الرئيسيـة 
—————————————
⌔︙اختر ماتريد عرضه من القائمه :

⌔︙قناة السورس والتحديثات
@aa_ggc - @aa_ggc
—————————————

""", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^m1 (\\d+)$"))
async def m1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر ", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
↯︙اوامر ↫ ⦗ القفل ~ الفتح ⦘
– – – – – –
↯︙ الدردشه ~ المعرفات الصور 
↯︙ الفيديوهات ~ الستيكر ~ الملفات
↯︙ المتحركه ~ الرفع الريكورد ~ الصوت 
↯︙ الجهات ~ الترحيب ~ المغادره
↯︙ الاغاني ~ الزغارفه ~ الافلام 
↯︙ اليوتيوب ~ الترجمه ~ الردود 
↯︙ التوجيه ~ الاشعارات ~ التاج
↯︙ رابط الحذف ~ الايدي بالصوره ~ اطردني 
↯︙ مين ضافني ~ الالعاب ~ الروايات 
↯︙ الابراج ~ معاني الاسماء ~ الترحيب
– – – – – –
استخدم الاوامر مع ↫ ⦗ قفل ~ فتح ⦘
↯︙مثال الاستخدام ↫ ⦗ قفل الروابط ⦘
– – – – – –
اوامر ↫ ⦗ القفل بالطرد ~ بالكتم ~ بالتقييد ~ بالمسح ⦘
– – – – – –
↯︙التوجيه ~ الاضافه ~ الدخول
↯︙البوتات ~ التكرار
– – – – – –
↯︙مثال الاستخدام ↫ ⦗ قفل التوجيه بالكتم ⦘
    """, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^mxx (\\d+)$"))
async def mxx(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر ", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("اوامر التسلية / 1", callback_data="mx1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اوامر التسلية / 2", callback_data="mx2 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرجوع للخلف", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ⌯", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text(" ⌯ اهلا بك فى اوامر التسليه\n√", reply_markup=keyboard)

@Client.on_callback_query(filters.regex("^m2 (\\d+)$"))
async def m2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر ", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("اوامر التسلية / 1", callback_data="mx1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اوامر التسلية / 2 ", callback_data="mx2 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرجوع للخلف", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ⌯", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text(" ◍ اهلا بك فى اوامر التسليه\n√", reply_markup=keyboard)

@Client.on_callback_query(filters.regex("^mx1 (\\d+)$"))
async def mx1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر ", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ التالي", callback_data="mx2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⌯", callback_data="mxx " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ⌯", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""↯︙  ❬ م2 ❭ 1 اوامر اوامر التسلية ( رفع + تنزيل )
– – – – – –
↯︙ متوحد ~ متوحده ~ تاج للمتوحدين ~ مسح المتوحدين
↯︙ بقره ~ تاج للبقرات ~ مسح البقرات
↯︙ غبي ~ تاج للاغبيه ~ مسح الاغبياء
↯︙ حمار ~ تاج للحمير ~ مسح الحمير 
↯︙ كلب ~ تاج للكلاب ~ مسح الكلاب
↯︙ قرد ~ تاج للقرود ~ مسح القرود 
↯︙ فرسه ~ تاج للفرسات ~ مسح الفرسات 
↯︙ عره ~ تاج للعرر ~ مسح العرر 
↯︙  زوجتي ~ تاج للزوجات ~ مسح المتزوجات 
↯︙ زواج ~ تاج للمتزوجين ~ مسح المتزوجين 
↯︙ من قلبي ~ تاج للي بقلبي ~ مسح من قلبي 
↯︙ بيستي ~ تاج للبيست ~ مسح البيستيه

    """, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^mx2 (\\d+)$"))
async def mx2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر ", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه", callback_data="mxx " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ⌯", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
      اوامر التسلية ( رفع + تنزيل )

– – – – – –
↯︙ وتكه ~ تاج للوتكات ~ مسح الوتكات
↯︙ رقاصه ~ تاج للرقاصات ~ مسح الرقاصات 
↯︙ مهزء ~ تاج للمهزئين ~ مسح المهزئين 
↯︙ حيوان ~ تاج للحيوانات ~ مسح الحيوانات
↯︙ فاشل ~ تاج للفشله ~ مسح الفاشله
↯︙ دكري ~ تاج للدكور ~ مسح الدكور
↯︙ قطتي ~ تاج للقطط ~ مسح القطط 
↯︙ ابني ~ تاج للابناء ~ مسح الابناء
↯︙ بنتي ~ تاج للبنوتات ~ مسح البنوتات 
↯︙ حبيبي ~ تاج للحبايب ~ مسح الحبايب 
↯︙ زوجي ~ تاج للزواج ~ مسح الازواج 
↯︙ زوجتي ~ تاج للزوجات ~ مسح الزوجات 
↯︙ خاين ~ تاج للخونه ~ مسح للخونه
↯︙ خاينه ~ تاج للخاينين ~ مسح الخاينين 
↯︙ عبيط ~ تاج للعبيط ~ مسح العبط 
↯︙ متخزوق ~ تاج للمتخزوقين ~ مسح المتخزوقين

    """, reply_markup=keyboard)

@Client.on_callback_query(filters.regex("^m3 (\\d+)$"))
async def m3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر ", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ⌯", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
اوامر الاعضاء ( العامة ) 

– – – – – –
↯︙ غنيلي ~ نسبه جمالي ~ صورتي 
↯︙ رمزيات ~ حساب العمر ~ استوري
↯︙ قرءان ~ الاعدادات ~ نقاطي 
↯︙ حذف ~ بيع نقاطي ~ رسائلي 
↯︙ حذف رسائلي ~ زخرفه ~ اغاني 
↯︙ افلام ~ كارتون ~ ترجمه ~ روايات 
↯︙ يوتيوب ~ العاب ~ طقس 
↯︙ المنطقة ~ الرابط ~ اسمي 
↯︙ الرتبه ~ بحبك ~ تتجوزيني 
↯︙ جهاتي ~ حذف جهاتي ~صلاحياتي 
↯︙ بينج ~ قول + كلمة ~ قطة 
↯︙ كلب ~ اطردني ~ اطردني 
↯︙ اكتمني ~ تاك للاولاين ~ تاكد للاعضاء
↯︙ سورس ~ السورس ~ المطور
↯︙ ايدي ~ رتبتي ~ كشف
↯︙ رد انت يابوت ~اي رايك يابوت 
↯︙ هينو ~ هينها ~ بوسو 
↯︙ بوسها ~ بتحب دي ~ بتحب ده
    """, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^m4 (\\d+)$"))
async def m4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر ", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ⌯", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
اوامر الادمنية و المالكيـن 
– – – – – –
اوامر ( المميزين )
↯︙ كشف ~ المحظورين ~ المكتومين 
– – – – – –
اوامر ( الادمنية )

↯︙ رفع مميز ~ تنزيل مميز ~ الترحيب 
↯︙ اضف مغادره ~ مسح المغادره ~ رساله المغادره
↯︙ كشف البوتات ~ المميزين ~ حذف المميزين
↯︙ حظر ~ الغاء الحظر ~ كتم 
↯︙ الغاء كتم ~ حظر لمده ~ كتم لمده
↯︙ طرد ~ تطهير ~ تثبيت بدون اشعار
↯︙ الغاء تثبيت الكل 
– – – – – –
اوامر ( المنشئين )

↯︙ رفع ادمن ~ تنزيل ادمن ~ اضف رد
↯︙ حذف رد ~ الردود ~ حذف الردود 
↯︙ ايقاف المنشن ~ تعيين الايدي ~ مسح الايدي
↯︙ الادمنيه ~ حذف الادمنيه ~ اضف ترحيب 
↯︙ حذف المحظورين ~ حذف المكتومين ~ منع 
↯︙ الغاء المنع ~ المميزين عام 
– – – – – –
اوامر ( المالك ) 

↯︙ اضف صوره للجروب ~ اضف وصف للجروب 
↯︙ رفع منشئ ~ تنزيل منشئ ~ تاج للاعضاء 
↯︙ اضف رابط ~ مسح الرابط ~ اضف امر
↯︙ حذف امر ~ الاوامر المضافه ~ اضف اسم 
↯︙ اضف تحديث ~ المنشئين ~ حذف المنشئين
    """, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^m5 (\\d+)$"))
async def m5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر ", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⌯", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ⌯", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
اوامر ( المطورين )

↯︙ رفع مالك ~ تنزيل مالك ~ تغيير رابط الجروب
↯︙ اذاعه بالمجموعات ~ اذاعه بالتوجيه للمجموعات 
↯︙ اذاعه موجهه بالتثبيت ~ اذاعه خاص ~ اذاعه بالتوجيه خاص
↯︙ اذاعه بالتثبيت ~ جلب نسخه احتياطيه ~ رفع نسخه احتياطيه 
↯︙ الاحصائيات ~ حذف المالكين 
– – – – – –
اوامر ( المطورين الاساسيين )

↯︙ اضف رد عام ~ حذف رد عام ~ رفع مميز عام 
↯︙ تنزيل مميز عام ~ مسح المميزين عام ~ الردود العامه 
↯︙ حذف الردود العامه ~ اذاعه بالتوجيه خاص ~ اذاعه بالتوجيه للمجموعات 
↯︙ اذاعه بالتثبيت ~ اذاعه موجهه بالتثبيت ~ جلب نسخه احتياطيه 
↯︙ رفع نسخه احتياطيه ~ الاحصائيات ~ رفع مطور
↯︙ تنزيل مطور ~ المطورين ~ حذف المطورين 
↯︙ ضع اسم البوت ~ تغيير رساله المغادره ~ حظر عام 
↯︙ كتم عام ~ المكتومين عام ~ المحظورين عام
↯︙ الغاء العام
    """, reply_markup=keyboard)
