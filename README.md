
# Telegram Notification
**Send a notification to Telegram from bash or python:**

 1. configure Telegram bot
 2. configure Telegram notifier
 3. send notification
 
**How to use it:** 

    sh some_script.sh
    python -m notify --message="Hello world! :)"

## **Set-up:**

 1. Open Telegram and search "BotFather" in the search bar. This is the official bot that allows you to create other bots.  
 2. Create new bot: `/newbot`
 3. Choose a name for your bot: `ScriptNotifier`
 4. Choose a username for your bot that must end with "_bot": `script_notifier_bot`  
 5. Once the bot is created, you will have a long string: this is the TOKEN ID
 6. The bot will send you messages on a specific chat that you need to create. Go to Telegram search bar, on your smartphone, and search your bot (e.g. ScriptNotifier). Then, start the bot: `/start` 
 
**..and you're ready to go!**

    python -m notify --message="Hello world! :)" --token_id="0123456:78910" --chat_id="12345"

To avoid passing the arguments `--token_id` and `--chat_id` through command line, you can directly modify the varaibles `TELEGRAM_TOKEN_ID` and `TELEGRAM_CHAT_ID` in the script notify.py 
 
## **Requirements:**

	pip install requests

 ------------------
**Inspired by:** https://www.marcodena.it/blog/telegram-logging-handler-for-python-java-bash/
