from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from knopkalar import *

teleramapi = '7351676892:AAG90Oiq1POUD1005_bw9KvFjVRZp9TdhdA'

bot = Bot(teleramapi)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='🔝 Asosiy Menyu', reply_markup=asosiymenu())

@dp.message_handler(text='🔙 Orqaga')
async def getorqaga(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='🔝 Asosiy Menyu', reply_markup=asosiymenu())

@dp.message_handler(text='🔝 Asosiy Menyu')
async def getasosiymenu(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='🔝 Asosiy Menyu', reply_markup=asosiymenu())

@dp.message_handler(text='ℹ️ Kiberxavfsizlik - bu ...')
async def getkiberxavf(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='ℹ️ Kiberxavfsizlik - bu ...', reply_markup=kiberxavfsizlik())

@dp.message_handler(text='▶️ Videokurslar')
async def getvideo(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='▶️ Videokurslar', reply_markup=videokurslar())

@dp.message_handler(text='Tarmoq administratorligi (CISCO)')
async def gettarmoq(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='Tarmoq administratorligi (CISCO)', reply_markup=tarmoqadmin())

@dp.message_handler(text='🎞️ Videodarslar')
async def getviddars(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='🎞️ Videodarslar', reply_markup=videodars())

@dp.message_handler(text="📕 Qo'llanmalar (PDF)")
async def getqollanma(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text="📕 Qo'llanmalar (PDF)", reply_markup=qollanma())

@dp.message_handler(text='💾 Kerakli dasturlar')
async def getkerakdastur(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='💾 Kerakli dasturlar', reply_markup=keraklidastur())

@dp.message_handler(text='🛡️ Antiviruslar')
async def getanti(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='🛡️ Antiviruslar', reply_markup=antivirus())

@dp.message_handler(text='🚫 Reklama bloklovchilar')
async def getrekblok(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='🚫 Reklama bloklovchilar', reply_markup=reklamablok())

@dp.message_handler(text='🅿️ Parol menejerlar')
async def getparolmenejr(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='🅿️ Parol menejerlar', reply_markup=parolmenejr())

@dp.message_handler(text='📛 Firewall dasturlari')
async def getfirewall(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='📛 Firewall dasturlari', reply_markup=firewalldastur())

@dp.message_handler(text="🔄 Ma'lumotlarni tiklovchilar")
async def getmalumottik(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text="🔄 Ma'lumotlarni tiklovchilar", reply_markup=malumotlarnitik())

@dp.message_handler(text="✅ Ma'lumotlarni himoyalovchilar")
async def getmalumothim(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text="✅ Ma'lumotlarni himoyalovchilar", reply_markup=malumotlarnihim())

@dp.message_handler(text='🔰 VPN dasturlar')
async def getvpndastur(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='🔰 VPN dasturlar', reply_markup=vpndastur())

@dp.message_handler(text='🈹 Shifrlovchi dasturlar')
async def getshirfdastur(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='🈹 Shifrlovchi dasturlar', reply_markup=shirfdastur())

@dp.message_handler(text='❗️Xavfsizlik')
async def getxavfsizlik1(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='❗️Xavfsizlik', reply_markup=xavfsizlik1())

@dp.message_handler(text='🌐 Brauzerlar')
async def getbrauzer(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='🌐 Brauzerlar', reply_markup=brauzer())

@dp.message_handler(text='📑 Maqolalar')
async def getmaqolalar(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='📑 Maqolalar', reply_markup=maqolalar())

@dp.message_handler(text='💡 Atamalar')
async def getatama(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='💡 Atamalar', reply_markup=atamalar())

@dp.message_handler(text='🌐 Foydali manzillar')
async def getmanzillar(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='🌐 Foydali manzillar', reply_markup=foydalimanzil())

@dp.message_handler(text='📊 Statistika')
async def getstatistika(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text="👥 Barcha obunachilar: 19929 kishi."
                                                "✅ Faol obunachilar: 10756 kishi."

                                                "🔜 Oxirgi 24 soatda 4 obunachi qo'shildi."
                                                "🔝 Oxirgi 1 oyda 160 obunachi qo'shildi."

                                                "📆 Bot ishga tushganiga 651 kun bo'ldi."

                                                "📊 @KiberXavfsizlikBot statistikasi!")

@dp.message_handler(text='📲 Aloqa')
async def getaloqa(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text="👨🏻‍💻 Loyiha asoschisi —  Jonibek Turapov"

                                                "📩 Murojaatlar uchun — @fullstack_online")

executor.start_polling(dp, skip_updates=True)