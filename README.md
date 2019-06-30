# RAT-via-Telegram-Bot

[![link to youtube video](http://img.youtube.com/vi/56VxwpOZkOM/0.jpg)](http://www.youtube.com/watch?v=56VxwpOZkOM "link to youtube video")

⬆️⬆️⬆️ This is link to YouTube video ⬆️⬆️⬆️

# What is it?
It's Windows Remote Administration Tool who work via Telegram Bot.

# How start using it?
1. First step you need to create your telegram bot:
- open telegram
- go to @BotFather
- choose name and username of your bot
- @BotFaher send you token, you need to copy and save it
- go to your bot and type /start
2. Second step you need to know your ChatId:
- in telegram go to @userinfobot and type /start
- he sent you your ChatId
- copy and save it id!
3. Next you need to edit bot code:
- open file RAT.py in any text editor
- edit variables bot_token and chat_id at the beginning code afret imports on previously saved data
- save all changes
4. In last step you need to create application .exe
- open terminal or cmd and type: pip install pyinstaller
- open directory where is RAT.py and type: pyinstaller -w -F RAT.py
- in current directory where is RAT.py will be created several folders
- in folder dist will be your RAT.exe

# functional
- /screen - screenshot
- /info - info about user
- /location - location on a map
- /kill_process - kill the process (process.exe)
- /reboot - reboot pc
- /shutdown - shutdown pc
- /pwd - know current directory
- /passwords_chrome - chrome passwords 
- /passwords_opera - opera passwords
- /cockies_chrome - chrome cockies
- /cockies_opera - opera cockies
- /get_discord - get token of Discord session
- /cmd command - execute command in CMD
- /open_url - open link
- /ls - all files and folders in directory
- /cd - move to folder
- /download - download file
- /rm_dir - delete folder
