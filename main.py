import telebot
from telebot import types
from Rooz import *
from keep_alive import keep_alive
keep_alive()

boss = types.InlineKeyboardMarkup(row_width=2)
rkkuu = types.InlineKeyboardButton(text='SiRius ♪ ,',url='rKKuu.t.me')
boss.add(rkkuu)

bot = telebot.TeleBot('6292366475:AAGcbFXzFswK9A43oQ3P5hiC2ZaTLzK13ao')

@bot.message_handler(commands=['start'])
def start(m):
 fe = types.InlineKeyboardMarkup(row_width=2)
 dirt = types.InlineKeyboardButton(text='🧑🏻‍💻',url='XuuDD.t.me')
 fe.add(dirt)
 name = m.from_user.first_name
 id = m.from_user.id
 dmj = f'[{m.from_user.first_name}](tg://user?id={m.from_user.id})'
 bot.reply_to(m,f'مرحباً بك عزيزي {dmj} في بوت التحميل من التيك توك ، ارسل الرابط ليتم التحميل ✓',parse_mode='markdown',reply_markup=fe)
 
@bot.message_handler(func=lambda m:True)
def don(m):
 mm = m.text
 ree = re.findall(r'https([^>]+)',mm)[0]
 li = f'https{ree}'
 print(li)
 print(ree)
 if mm.text.startswith("https://vm.tiktok.com/") or mm.text.startswith('https://www.tiktok.com/'):
   rr = random.randint(1,100)
   wwb = open(f'video_{m.from_user.id}.mp4','wb')
   tiik = Download(str(li)).DownTikTok()
   lln = tiik['Video_Url']
   print(tiik)
   requ = requests.get(lln).content
   wwb.write(requ)
   rb = open(f'video_{m.from_user.id}.mp4','rb')
   bot.send_video(m.chat.id,
   video=rb,
   caption=tiik['Title'],
   reply_markup=boss)
   os.remove('video_{m.from_user.id}.mp4')
 else:
  bot.reply_to(m,'خطأ في الرابط :(')
  

bot.infinity_polling()
