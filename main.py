try :
    import httpx
    import requests
    import os , sys , time
    from datetime import datetime
    from time import sleep
    import telebot
    from telebot import types
    import random
    import pip
except ImportError :
    import os
    os.system('pip install httpx requests ')
    os.system('pip install pyTelegramBotAPI  ')
bot = telebot.TeleBot(token='6820653441:AAG2sqzKU10uw-cQUUUIEMDpm_TgtjqU79M' )
owner = ['6640183279' , '6037113802' ,'5489872238']
def sendwebhook(claimuser , att , finish , begining) :
    webhookurl = 'https://discord.com/api/webhooks/1163888841627811870/PyQVDWZQfIdg_SzFIOVJYhEYN6JTJZ4sYzdz7xo0LGJRIrfEqX9PjvWrjWiEdSxvk4OZ'
    webhookjson ={
                                'avatar_url' : 'https://www.pinterest.com/pin/263531015690088612/',
                                'username' : 'ASTA CLAIM-V0.1',
                                'content' : f' > Username {claimuser} \n > attempts :{att} \n > Time : {finish - begining} R/S',
                                'embeds' : [{
                                        'title' : "ASTA V0.1",
                                        "description" : "Let's move to a new one "
                                }]
                                        }
    httpx.post(url=webhookurl , json=webhookjson)
attempts = 0
group_id = '1974322453'
id_subs = []
attempt = 0
message_to_edit = None

def login(user , passw):

    with open('proxy.txt' , 'r' ) as proxyfile :
        proxies = proxyfile.read().splitlines()
    proxy = random.choice(proxies)
    time = int(datetime.now().timestamp())
    url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/"
    payload = {'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{passw}',
    'optIntoOneTap': 'false',
    'queryParams': {},
    'username': user}
    files=[

  ]
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
    session = requests.Session()
    session.proxies = {"http": proxy}
    session.headers.update(headers)
    getcsrf = session.post(url, data=payload , files=files)

    global csrf
    csrf=getcsrf.cookies["csrftoken"]
    global sid
    headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'X-Csrftoken': f'{csrf}',
    'Cookie': f"csrftoken={csrf}; mid=ZIrEtgALAAE7GrCUwQ9wcQbbrefW; ig_did=80445D30-C9F9-4D3F-8BF0-78B39275775C; ig_nrcb=1; datr=tcSKZFMeDkyjVKNghYr_9-WI"
  }
    session = requests.Session()
    session.proxies = {"http": proxy}
    session.headers.update(headers)
    getsid = session.post(url , payload )
    global x
    x = getsid.json()

    if x["status"]=="ok" and x["authenticated"]!=None and x["authenticated"]==True:
        sid = getsid.cookies['sessionid']
        return True
    elif x == {'message': 'Please wait a few minutes before you try again.', 'status': 'fail'} :
        return False
    else :
        return False
def swapuser(csrf , sid , email , claim ,username ) :
    with open('proxy.txt' , 'r' ) as proxyfile :
        proxies = proxyfile.read().splitlines()
    proxy = random.choice(proxies)
    url = 'https://www.instagram.com/api/v1/web/accounts/edit/'
    urljj = f'https://www.instagram.com/{username}/?__a=1&__d=dis'
    jss = httpx.get(urljj ).json()
    data = jss["graphql"]["user"]
    full_name=data["full_name"]
    headers = {
                    'X-Csrftoken': f'{csrf}',
                    'Cookie': f"ig_did=29F806F6-618B-4AEE-AB10-3135FEFC0ADF; ig_nrcb=1; mid=ZKiWsQALAAHpZUSVh1zhvRB_rjKw; datr=r5aoZPJ_i4dQ4KOxwb85x848; oo=v1; csrftoken={csrf}; dpr=1.25; sessionid={sid};"
                }
    dat  = {
                'first_name': full_name ,
            " chaining_enabled": "on",
                "email" : email,
                "biography": 'close ur tool baby , Asta here ' ,
                "username" : claim

            }
    global start
    error = {
    "message": {
        "errors": [
            "This username isn't available. Please try another."
        ]
    },
    "status": "fail"
}
    session = requests.Session()
    session.proxies = {"http": proxy}
    session.headers.update(headers)
    start = session.post(url, data=dat).json()

    if start['status']=="ok":
        return True
    else :
        return False
@bot.message_handler(commands=['start'])
def starting(message) :
    chat_id = message.from_user.id
    for idd in owner :
        if str(chat_id) in idd :
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            claim_button = types.InlineKeyboardButton('Claim', callback_data='claim')
            owner_button = types.InlineKeyboardButton('Owner', callback_data='owner')
            keyboard.add(claim_button , owner_button)
            bot.send_message(chat_id, f'Welcome Sirr @{message.from_user.username} This is Claimer menu check what u want  ', reply_markup=keyboard)

    for ids in id_subs :
        if str(chat_id) in ids :
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            claim_button = types.InlineKeyboardButton('Claim', callback_data='claim')

            keyboard.add(claim_button).row=1
            bot.send_message( chat_id, f'Welcome @{message.from_user.username} in ASTA 404 click in this ', reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: call.data == 'claim' )
def handle_claim_button(message):
    chat_id = message.from_user.id
    if str(chat_id) in id_subs or  str(chat_id) in owner:
            global credentials
            credentials = {}
            del credentials
            photo = open('pin.mp4' , 'rb')
            bot.send_video(chat_id , photo)
            bot.send_message(chat_id , "Welcome ! Let's start Give mecredentials in this form - user:pass:email:claimuser - . ")
            sleep(5)
            @bot.message_handler(func=lambda message: message.text is not None)
            def handle_credentials(message):
                    with open('proxy.txt' , 'r') as proxyfile :
                        proxies = proxyfile.read().splitlines()
                    proxy =  random.choice(proxies)
                    credentials = {}
                    chat_id = message.chat.id
                    if chat_id in credentials :
                        bot.send_message(chat_id , 'Please reclick in claim and send credentiels ')
                        del credentials[chat_id]
                    elif chat_id not in credentials:
                        credentials[chat_id] = ""
                        credentials[chat_id] += message.text
                        if len(credentials[chat_id].split(':')) == 4:
                            user_input = credentials[chat_id].split(':')
                            user ,passowrd, email, claimuser = user_input
                            sleep(2)
                            logincheck = login(user=user , passw=passowrd)
                            begining = time.time()
                            if logincheck :
                                bot.send_message(chat_id , f' > Log in was corect wait ...  ')
                                urlcheck = f'https://www.instagram.com/{claimuser}/?__a=1&__d=dis'
                                checkuser = requests.get(urlcheck).status_code
                                if checkuser == 404:
                                    bot.send_message(chat_id , f'{claimuser} is available ')
                                    attempts =+1
                                    checkswap = swapuser(csrf=csrf , sid=sid , email=email , claim=claimuser , username=user)
                                    if checkswap :
                                        finish = time.time()
                                        bot.send_message(chat_id , f' >Username {claimuser} \n > attempts :{attempts} \n > Time : {finish - begining} R/S \n > Develloper : @Telllonym ')
                                        sendwebhook(claimuser , att , finish , begining)
                                        del credentials[chat_id]
                                    else :
                                        bot.send_message(chat_id , f'> Maybe @{claimuser} have 14 days condition or banned wait for next version V0.2 it support skip 14 day json is {start} ')
                                        del credentials[chat_id]
                                else :
                                    
                                    attempt = 0
                                    att =0
                                    first = bot.send_message(chat_id,  f'> User : {claimuser} \n\n > Attempts : {att} \n\n > Just wait when it became available')
                                    urlcheck = f'https://www.instagram.com/{claimuser}/?__a=1&__d=dis'
                                    ch = requests.get(urlcheck).status_code
                                    while ch == 200 :
                                        bot.edit_message_text(f'> User : {claimuser} \n\n > Attempts : {att} \n\n > Just wait when it became available' , chat_id , first.message_id)
                                        sleep(2)
                                        urlcheck = f'https://www.instagram.com/{claimuser}/?__a=1&__d=dis'
                                        attempt +=1
                                        att += 1
                                        ch = requests.get(urlcheck).status_code
                                        if ch == 404 :
                                            att += 1
                                            bot.send_message(chat_id , f'{claimuser} became  available  after {att} attempts ')
                                            checkswapp = swapuser(csrf=csrf , sid=sid , email=email , claim=claimuser , username=user)
                                            if checkswapp:
                                                finish = time.time()
                                                att += 1
                                                bot.send_message(chat_id , f' >Username {claimuser} \n > attempts :{att} \n > Time : {finish - begining} R/S \n > Develloper : @Telllonym ')
                                                sendwebhook(claimuser , att , finish , begining)
                                                del credentials[chat_id]
                                            else :
                                                while not checkswapp :
                                                    checkswap3 =  swapuser(csrf=csrf , sid=sid , email=email , claim=claimuser , username=user)
                                                    if checkswap3 :
                                                        att += 1
                                                        bot.send_message(chat_id , f' >Username {claimuser} \n > attempts :{att} \n > Time : {finish - begining} R/S \n > Develloper : @Telllonym ')
                                                        sendwebhook(claimuser , att , finish , begining)
                                                        del credentials[chat_id]
                                                        starting(message)
                                        else :
                                            attempt =+1
                            else :
                                bot.send_message(chat_id , f'Credentials are incorect please check your information json {x}')

@bot.callback_query_handler(func=lambda call: call.data == 'owner')
def owner_button(message):
    chat_id = message.from_user.id
    if str(chat_id) in owner  :
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        users = types.InlineKeyboardButton('Users', callback_data='users')
        delete = types.InlineKeyboardButton('Delete', callback_data='delete')
        add = types.InlineKeyboardButton('Add', callback_data='add')
        back = types.InlineKeyboardButton('Back', callback_data='back')
        keyboard.add(users , add , delete , back)
        bot.send_message(chat_id, f'Welcome Sirr @{message.from_user.username} in Owner menu', reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: call.data == 'users')
def users(message):
    chat_id = message.from_user.id
    if str(chat_id) in owner  :
        id_list = list(id_subs)
        for ids in id_list :
            bot.send_message(chat_id , text=f'{ids}')
@bot.callback_query_handler(func=lambda call: call.data == 'add')
def users(message):
    chat_id = message.from_user.id
    if str(chat_id) in owner  :
        bot.send_message(chat_id , f'Give me id that you wanna to add ')
        @bot.message_handler(func=lambda message: True)
        def getuser(inner) :
            new = inner.text
            id_subs.append(new)
@bot.callback_query_handler(func=lambda call: call.data == 'delete')
def delete(message):
    chat_id = message.from_user.id
    if str(chat_id) in owner:
        bot.send_message(chat_id , f'Give me id that you wanna to delete ')
        @bot.message_handler(func=lambda message: True)
        def getuser(inner) :
            id = inner.text
            if id in id_subs :
                del id
                id_list = list(id_subs)
                for id in id_list :
                    bot.send_message(chat_id , f' User was removed New list is :' )
                    bot.send_message(chat_id , f' New list is : {id_list} ')
@bot.callback_query_handler(func=lambda call: call.data == 'back')
def back(message):
    chat_id = message.from_user.id
    if str(chat_id) in owner :
        starting(message)

if __name__ == "__main__":
  
  bot.polling(none_stop=True)
