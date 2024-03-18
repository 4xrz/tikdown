import telebot, re , random
from telebot import types
from Rooz import *
from keep_alive import keep_alive
keep_alive()

boss = types.InlineKeyboardMarkup(row_width=2)
rkkuu = types.InlineKeyboardButton(text='SiRius ♪ ,',url='rKKuu.t.me')
boss.add(rkkuu)

bot = telebot.TeleBot('6292366475:AAH_1vCSYAS8hUoZKDfJ87pNKroHGsZ_MTw')

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
	try:
			rr = random.randint(1,100)
			wwb = open(f'video{rr}.mp4','wb')
			tiik = Download(str(li)).DownTikTok()
			lln = tiik['Video_Url']
			print(tiik)
			requ = requests.get(lln).content
			wwb.write(requ)
			rb = open(f'video{rr}.mp4','rb')
			bot.send_video(m.chat.id,
			video=rb,
			caption=tiik['Title'],
			reply_markup=boss)
			os.remove('video{rr}.mp4')
	except Exception:
		bot.reply_to(m,'خطأ في الرابط :(')

bot.infinity_polling()	