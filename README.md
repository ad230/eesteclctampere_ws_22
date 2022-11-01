# eesteclctampere_ws_22
Base project for Great Northern Health Tracking Trek. EESTEC LC Tampere workshop November 2022

## 0. Installing required tools and packages

### Git if you don't have already

- `sudo apt install git`

### Package installer for Python

- `sudo apt install python3-pip`

### Python Telegram Bot 

- `pip install python-telegram-bot -U --pre`
  - pre-releases https://github.com/python-telegram-bot/python-telegram-bot/wiki/introduction-to-the-API
  - If you want to use older version like 13.0 the syntax is quite different.

### Data is stored with sqlite3 database so let's install that

- `sudo apt install sqlite3`

## 0. Getting access to repository

- Log in or sign up to github.
- Now let's fork this repository: https://github.com/ahvena91/eesteclctampere_ws_22
- Forking means that you take a copy of source code and start independet development on it
- main branch has few minimal examples
- if you get stuck or want to check something there's a bit more advanced sources in other branches

### 1. Installing all libraries listed in requirements

- `pip install -r requirements.txt`

## 2. Talking to botfather and getting your token

- start conversation with https://t.me/botfather
- make a copy of `env-example.cfg` and rename it to `env.cfg`
- `env.cfg` is se to .gitignore so that we wont't publish our personal bot token by accident

## 3. Run echobot and conversationbot to test things out

- `python3 echobot.py`
- `python3 conversationbot.py`

## 4. Check the features 

- check out features.mmd and start to plan your own features
- core features would be at least to store data to database and plot it on request
- after that we would like to plot 3, 5, 7 day trends propably

