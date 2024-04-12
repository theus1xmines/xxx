import time
import random
import json
import telebot
from datetime import datetime, timezone
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import bd

api_key = '7162452045:AAEbCWNUV9XglsdbM38A7Vwjn4DQGp7puuA'  # Substitua pelo seu próprio token
chat_id = '-1002074612431'  # Substitua pelo ID do seu canal

bot = telebot.TeleBot(token=api_key)

# Defina as funções ALERT_GALE1 e DELETE_GALE1 como antes
def ALERT_GALE1():
    h = datetime.now().hour
    m = datetime.now().minute + 1
    if h <= 9:
        h = f'0{h}'
    if m <= 9:
        m = f'0{m}'
    message_id = bot.send_message(chat_id=chat_id, text=f'''
🔍 Buscando proximo sinal 100% 🔍….''').message_id
    bd.message_ids1 = message_id
    time.sleep(13)
    bd.message_delete1 = True

def DELETE_GALE1():
    if bd.message_delete1 == True:
        bot.delete_message(chat_id=chat_id, message_id=bd.message_ids1)
        bd.message_delete1 = False

# Resto do código
def button_link():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton(text="ㅤㅤㅤㅤㅤCLIQUE AQUI NO JOGO 💎ㅤㅤㅤㅤㅤ", url="https://brwinwin.com/y3leimk3u"))
    return markup

def button_link2():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton(text="PLATAFORMA AQUI 💎 ", url="https://brwinwin.com/y3leimk3u"))
    return markup

while True:
    h = datetime.now().hour
    m = datetime.now().minute + 2
    s = datetime.now().second
    if h <= 9:
        h = f'0{h}'
    if m <= 9:
        m = f'0{m}'
    if s <= 9:
        s = f'0{s}'
    print(f'{h}:{m}:{s}')
   
    cc = random.randint(2, 4)
    tt = random.randint(3, 4)

    num_john = random.randint(3, 4)
    cores = ['💎'] * num_john + ['💣'] * (25 - num_john)

    ALERT_GALE1()  # Chama a função de alerta

    DELETE_GALE1()  # Chama a função de exclusão do alerta

    sample = random.sample(cores, k=25)
    message_text = f'''
🟢 SINAL CONFIRMADO 🟢

 Theus Mines 💣  

💣 Minas: {cc}
⏱ Valido até: {h}:{m}
📊 Chance de acerto: 100.00%                                     
🔁 Nº de tentativas: {1}


{''.join(sample[:5])}
{''.join(sample[5:10])}
{''.join(sample[10:15])}
{''.join(sample[15:20])}
{''.join(sample[20:])}
'''

    dados = bot.send_message(chat_id=chat_id, text=message_text, reply_markup=button_link())

    time.sleep(60)


    bot.edit_message_text(f'''
                          
🔴 SINAL FINALIZADO 🔴

Theus Mines 💣   

💣 Minas: {cc}
⏱ Valido até: {h}:{m}
📊 Chance de acerto: Acertou! ✅                                   
🔁 Nº de tentativas: {1}


{''.join(sample[:5])}
{''.join(sample[5:10])}
{''.join(sample[10:15])}
{''.join(sample[15:20])}
{''.join(sample[20:])}

    ''', 
    dados.chat.id, dados.message_id, bot.send_message, reply_markup=button_link())

    time.sleep(13)
    
    sample = random.sample(cores, k=25)
    message_text = f'''
+1 Green ✅, aguarde o próximo!
Cadastre-se na plataforma👇🏼
'''

    dados = bot.send_message(chat_id=chat_id, text=message_text, reply_markup=button_link2())
    

    time.sleep(15)