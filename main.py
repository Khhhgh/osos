import requests,time,re
from time import sleep
import telebot
from telebot import types
import os
from uuid import uuid4 as uid
from secrets import token_hex
import requests
from uuid import uuid4 as uid
from secrets import token_hex
import requests
import telebot
from telebot import types
import os
from uuid import uuid4
import json
import requests
from requests import get
from user_agent import generate_user_agent
import requests
import re
import json
requests.urllib3.disable_warnings()
sudo = 8011996271 #خلي ايدي حسابك التلي 

def id_file1(id):
 all = False
 file = open("users.txt","r")
 for line in file:
  if line.strip() ==id:
   all = True
 file.close()
 return all
pg = "https://t.me/mover7i/3" 
ti=0
users = []
token = "7688125082:AAG_htr5oru-4xCkjYFG0hVzjHQJ2-8QWHo"
print('- اذهب للبوت واضغط \n /start')
bot = telebot.TeleBot(token) 
def short(url):
    return pyshorteners.Shortener().tinyurl.short(url)
@bot.message_handler(commands = ["start"])
def start(message):
   id = message.from_user.id
   with open('users.txt','a') as f3:
    f3.write(f'{id}\n')
    channel = "A_S_4A" # Your channel username without @
    
    a = message.from_user.first_name
    b = message.from_user.username
    if message.chat.type == "private":
      if not id in users:
        users.append(id)
        stats = len(users)
        bot.send_message(sudo,"""-» قام شخص جديد بالدخول الى البوت الخاص بك 
- -» اسمه : {}
-» معرفه : @{}
-» ايديه : {}
➖ أصبح عدد مستخدمين البوت : ~ {}""".format(a,b,id,stats),disable_web_page_preview=True)
      x = requests.get(f"https://api.telegram.org/bot{token}/getChatMember?chat_id=@{channel}&user_id={id}").text
      if x.count("left") or x.count("Bad Request: user not found"):
       z = types.InlineKeyboardMarkup()
       x = types.InlineKeyboardButton(text = "➕ channel ",url=f"t.me/{channel}")
       z.add(x)
       return bot.send_message(message.chat.id,f'''<strong>- ⌔︙عليك الاشتراك في قناة البوت لأستخدام الاوامر
-» اشترك في القناة @{channel} .
-» ثم ارسل /start ✅ </strong>''',reply_markup=z,parse_mode='html')

      
      bot.send_photo(message.chat.id,pg)
      bot.send_message(message.chat.id,f"اهلا\tبك\tلبدأ\tالتنزيل\tاضغط\n/SEXY") 
     
@bot.message_handler(commands = ["SEXY"])
def s1(message):
    mj=bot.send_message(message.chat.id,"""  
* -  افلام هنا 👉 https://t.me/mono3i. 
--------------------------------------
 -                                           *
""",parse_mode = "markdown")
    bot.register_next_step_handler(mj,ag)
def ag(message):
 global us,ti
 url = message.text
 try:
  request = get(f"https://www.tikwm.com/api/?url={url}").json()
  video = request["data"]["play"]
  bot.send_video(message.chat.id,video,caption="- تم تحميل الفيديو\nرابط بوت التحميل : @TOM6Y7BOT . ")
 except:
  bot.send_message(message.chat.id,f"-  الرابط غير صالح ❌ . ")
bot.infinity_polling()
