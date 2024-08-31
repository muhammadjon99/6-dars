from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup

def asosiymenu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text='ℹ️ Kiberxavfsizlik - bu ...'),
        KeyboardButton(text='▶️ Videokurslar'), KeyboardButton(text='🎞️ Videodarslar'),
    )
    markup.add(
        KeyboardButton(text="📕 Qo'llanmalar (PDF)"),
        KeyboardButton(text='💾 Kerakli dasturlar'), KeyboardButton(text='📑 Maqolalar'),
    )
    markup.add(
        KeyboardButton(text='💡 Atamalar'), KeyboardButton(text='🌐 Foydali manzillar'),
        KeyboardButton(text='📲 Aloqa'), KeyboardButton(text='📊 Statistika'),
    )
    return markup

def kiberxavfsizlik():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text='Kiberxavfsizlik nima?'),
        KeyboardButton(text='Kiberxavfsizlik tarixi'),
        KeyboardButton(text="Kibertahdidlarning tarqalish ko'lami"),
        KeyboardButton(text='Kiber tahdidlar turlari'),
        KeyboardButton(text="Kiberxavfsizlikga qayerda o'qiladi?"),
        KeyboardButton(text='🔙 Orqaga'), KeyboardButton(text='🔝 Asosiy Menyu'),
    )
    return markup

def videokurslar():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text='✅ Bepul darslar'),
        KeyboardButton(text='Tarmoq administratorligi (CISCO)'),
        KeyboardButton(text='Offensive SQL darslari'),
        KeyboardButton(text='🔙 Orqaga'), KeyboardButton(text='🔝 Asosiy Menyu'),
    )
    return markup

def tarmoqadmin():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text='Tarmoq administratorligi 1-dars'), KeyboardButton(text='Tarmoq administratorligi 2-dars'),
        KeyboardButton(text='Tarmoq administratorligi 3-dars'), KeyboardButton(text='Tarmoq administratorligi 4-dars'),
        KeyboardButton(text='Tarmoq administratorligi 5-dars'), KeyboardButton(text='Tarmoq administratorligi 6-dars'),
        KeyboardButton(text='Tarmoq administratorligi 7-dars'), KeyboardButton(text='Tarmoq administratorligi 8-dars'),
        KeyboardButton(text='Tarmoq administratorligi 9-dars'), KeyboardButton(text='Tarmoq administratorligi 10-dars'),
        KeyboardButton(text='Tarmoq administratorligi 11-dars'), KeyboardButton(text='Tarmoq administratorligi 12-dars'),
        KeyboardButton(text='Tarmoq administratorligi 13-dars'), KeyboardButton(text='Tarmoq administratorligi 14-dars'),
        KeyboardButton(text='Tarmoq administratorligi 15-dars'),
        KeyboardButton(text='🔙 Orqaga'), KeyboardButton(text='🔝 Asosiy Menyu'),
    )
    return markup

def videodars():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text='🗂️ Antivirus - Nod32'), KeyboardButton(text='🗂 Kaspersky'),
        KeyboardButton(text='Fleshkani himoyalashni eng oson va samarali usuli!'),
        KeyboardButton(text='Shaxsiy fayllarni yashiramiz!'),
        KeyboardButton(text="Windows 10'dagi ayg'oqchi funksiyalarini o'chirish"),
        KeyboardButton(text="O'chirilgan fayllarni qayta tiklash"),
        KeyboardButton(text='🔙 Orqaga'), KeyboardButton(text='🔝 Asosiy Menyu'),
    )
    return markup

def qollanma():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text='Kiberxavfsizlik asoslari'),
        KeyboardButton(text='🔙 Orqaga'), KeyboardButton(text='🔝 Asosiy Menyu'),
    )
    return markup

def keraklidastur():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text='🛡️ Antiviruslar'), KeyboardButton(text='🚫 Reklama bloklovchilar'),
        KeyboardButton(text='🅿️ Parol menejerlar'), KeyboardButton(text='📛 Firewall dasturlari'),
        KeyboardButton(text="🔄 Ma'lumotlarni tiklovchilar"), KeyboardButton(text="✅ Ma'lumotlarni himoyalovchilar"),
        KeyboardButton(text='🔰 VPN dasturlar'), KeyboardButton(text='🈹 Shifrlovchi dasturlar'),
        KeyboardButton(text='❗️Xavfsizlik'), KeyboardButton(text='🌐 Brauzerlar'),
        KeyboardButton(text='🔙 Orqaga'), KeyboardButton(text='🔝 Asosiy Menyu'),
    )
    return markup

def antivirus():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="Kaspersky Free"),
        KeyboardButton(text="NOD32"),
        KeyboardButton(text="Kaspersky"),
        KeyboardButton(text='🔙 Orqaga'), KeyboardButton(text='🔝 Asosiy Menyu'),
    )
    return markup

def reklamablok():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="Adguard"),
        KeyboardButton(text='🔙 Orqaga'), KeyboardButton(text='🔝 Asosiy Menyu'),
    )
    return markup

def parolmenejr():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="KeePass"), KeyboardButton(text="LastPass Password"),
        KeyboardButton(text='🔙 Orqaga'), KeyboardButton(text='🔝 Asosiy Menyu'),
    )
    return markup

def firewalldastur():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="Windows Firewall Control"),
        KeyboardButton(text='🔙 Orqaga'), KeyboardButton(text='🔝 Asosiy Menyu'),
    )
    return markup

def malumotlarnitik():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="Hetman Partition Recovery"),
        KeyboardButton(text="R-Studio"), KeyboardButton(text="Recuva"),
        KeyboardButton(text='🔙 Orqaga'), KeyboardButton(text='🔝 Asosiy Menyu'),
    )
    return markup

def malumotlarnihim():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="Hide Folders"), KeyboardButton(text="Wise Folder Hider Pro"),
        KeyboardButton(text='🔙 Orqaga'), KeyboardButton(text='🔝 Asosiy Menyu'),
    )
    return markup

def vpndastur():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="Aman VPN"), KeyboardButton(text="Psiphon"),
        KeyboardButton(text='🔙 Orqaga'), KeyboardButton(text='🔝 Asosiy Menyu'),
    )
    return markup

def shirfdastur():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="DeepSound"), KeyboardButton(text="SilentEye"),
        KeyboardButton(text='🔙 Orqaga'), KeyboardButton(text='🔝 Asosiy Menyu'),
    )
    return markup

def xavfsizlik1():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="Starus Web Detective"),
        KeyboardButton(text='🔙 Orqaga'), KeyboardButton(text='🔝 Asosiy Menyu'),
    )
    return markup

def brauzer():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="Firefox"), KeyboardButton(text="Chrome"),
        KeyboardButton(text="Opera"), KeyboardButton(text="Edge"),
        KeyboardButton(text='🔙 Orqaga'), KeyboardButton(text='🔝 Asosiy Menyu'),
    )
    return markup

def maqolalar():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="Crack dasturlar"),
        KeyboardButton(text="💣 Zip-bomba"),
        KeyboardButton(text="Ma’lumotlarni bir zumda o‘chiruvchi fleshka"),
        KeyboardButton(text="Tizim ustidan nazoratni qo'lga kiritish yo'llari"),
        KeyboardButton(text="Kiberxavfsizlik bo'yicha foydali maslahatlar"),
        KeyboardButton(text='🔙 Orqaga'), KeyboardButton(text='🔝 Asosiy Menyu'),
    )
    return markup

def atamalar():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="1-qism"), KeyboardButton(text="2-qism"),
        KeyboardButton(text='🔙 Orqaga'), KeyboardButton(text='🔝 Asosiy Menyu'),
    )
    return markup

def foydalimanzil():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="Anonimlik sari yana bir qadam"),
        KeyboardButton(text="Raqamli izlarimizni yo'qotamiz"),
        KeyboardButton(text='🔙 Orqaga'), KeyboardButton(text='🔝 Asosiy Menyu'),
    )

    return markup
