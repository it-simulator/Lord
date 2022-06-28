import httpx
import time
import telebot
from telebot import types

update_id = None

#из задачи со встречи
#while True:
 # contents = httpx.get('https://api.telegram.org/bot5479838908:AAGACo54yOGqeY2CgiyfPbu_pUpX04pH98g/getUpdates')
 # updates = contents.json()
 # messages = updates['result']

 # new_update_id = messages[-1]['update_id']
  #if new_update_id != update_id:
  #    update_id = new_update_id

#если тип сообщения = команда "старт", Бот отвечает: Hi, Bro!  
commands=['start']
httpx.get('https://api.telegram.org/bot5479838908:AAGACo54yOGqeY2CgiyfPbu_pUpX04pH98g/sendMessage?chat_id=5301913989&text=Hi, Bro!')

#если тип сообщения = текст и текст = "hi", Бот отвечает: How are you?
content_types=['text']
if message.text == 'hi':
 httpx.get('https://api.telegram.org/bot5479838908:AAGACo54yOGqeY2CgiyfPbu_pUpX04pH98g/sendMessage?chat_id=5301913989&text=How are you?')
 
#если тип сообщения = текст и текст = "by",Бот отвечает: By, Bro! 
elif message.text == "by":
 httpx.get('https://api.telegram.org/bot5479838908:AAGACo54yOGqeY2CgiyfPbu_pUpX04pH98g/sendMessage?chat_id=5301913989&text=By, Bro!')

time.sleep(1)
