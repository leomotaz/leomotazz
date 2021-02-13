import requests,json,random,string,termcolor,time,pyfiglet
from bs4 import BeautifulSoup
# -----------------------------------

logo = pyfiglet.figlet_format('MR WOLF')
descr = """
 By: Mr Wolf
Channel Telegram: https://t.me/nettfree1

اسكربت كبر باقتك
 """
print(termcolor.colored(logo, color="green"), termcolor.colored(descr, color="red"))
number = input(" Enter your number: ").strip()
pwd = input(" Enter your password: ").strip()
with requests.Session() as req:
    def generationLink(stringLingth):
        latters = string.ascii_lowercase
        return ''.join(random.choice(latters) for i in range(stringLingth))
    urlLoginPage = f'https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/auth?client_id=website&redirect_uri=https%3A%2F%2Fweb.vodafone.com.eg%2Far%2FKClogin&state=286d1217-db14-4846-86c1-9539beea01ed&response_mode=query&response_type=code&scope=openid&nonce={generationLink(10)}&kc_locale=en'
    responsePageLogin = req.get(urlLoginPage)
    soup = BeautifulSoup(responsePageLogin.content, 'html.parser')
    getUrlAction = soup.find('form').get('action')
    # print(getUrlAction)
    # ---------------------------------------------------
    headerRequest = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en;q=0.9,ar;q=0.8,ar-EG;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'web.vodafone.com.eg',
    'Origin': 'https://web.vodafone.com.eg',
    'Referer': urlLoginPage,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    formData = {
    'username':number,
    'password':pwd
    }
    sendUserData = req.post(getUrlAction,headers=headerRequest,data=formData)
    checkRegistry = sendUserData.url
    _checkRegistry = checkRegistry.find('KClogin')
    # [2] Check the registry
    if _checkRegistry != -1:
        code = checkRegistry
        _code = code[code.index('code=') + 5:]
        headerAccessToken = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en;q=0.9,ar;q=0.8,ar-EG;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-type': 'application/x-www-form-urlencoded',
        'Host': 'web.vodafone.com.eg',
        'Origin': 'https://web.vodafone.com.eg',
        'Referer': 'https://web.vodafone.com.eg/ar/KClogin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        }
        formDataAccessToken = {
        'code': _code,
        'grant_type': 'authorization_code',
        'client_id': 'website',
        'redirect_uri': 'https://web.vodafone.com.eg/ar/KClogin'
        }
        sendDataAccessToken = req.post('https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token',headers=headerAccessToken,data=formDataAccessToken)
        access_token = sendDataAccessToken.json()['access_token']
        # print(access_token)
        #--------------------------------------------------------
        def gifts():
            count = 0
            while True:
                count += 1
                url = "https://web.vodafone.com.eg/services/promo/eligibleGifts"
                header = {
                'Host': 'web.vodafone.com.eg',
                'Connection': 'keep-alive',
                'Accept': 'application/json, text/plain, */*',
                'Authorization': f'Bearer {access_token}',
                'msisdn': number,
                'api-host': 'PromoHost',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 9; SM-J701F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36',
                'Content-Type': 'application/json',
                'Origin': 'https://web.vodafone.com.eg',
                'Referer': 'https://web.vodafone.com.eg/ar/outofbundleoffer',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6'
                }
                jsonData = {"msisdn":f"{number}","promoId":"2815","operationId":"4","channelId":"1","param1":"5","param2":"0","param11":"0","param12":"1","param13":"0","param14":"0","param15":0.62,"param16":453,"serviceType":"AggregatedProfile","triggerId":"8"}
                res = req.post(url,headers=header,data=json.dumps(jsonData))
                giftNameEn = res.json()['gifts'][0]['giftNameEn']
                if giftNameEn == "Enjoy More":
                    giftShortCode = res.json()['gifts'][0]['giftShortCode']
                    giftDescEn = res.json()['gifts'][0]['giftDescEn']
                    return f"{giftShortCode} {giftDescEn}"
                    # print(giftShortCode)
                    break 
                else:
                    if count == 10:
                        return " No Enjoy More."
                        break
        # print(gifts())                
        ################################################## REPLY_FAIL   Success Bundle 100 LE
        ## Check Stop Rollover NEXT Month Flag
        def checkRollover():
            url = "https://web.vodafone.com.eg/services/dxl/pim/product"
            params = f"relatedParty.id={number}&place.@referredType=Local&@type=MIProfile"
            header = {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'EN',
            'Authorization': f'Bearer {access_token}',
            'msisdn': number,
            'Accept-Language': 'EN',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
            'Content-Type': 'application/json',
            'Referer': 'https://web.vodafone.com.eg/spa/miManagement',
            'Accept-Encoding': 'gzip, deflate, br'
            }
            sendReq = req.get(url,headers=header,params=params)
            rollover = sendReq.text
            rollover = rollover.find("Stop Rollover NEXT Month Flag")
            return rollover
        #################################################################    
        def subEnjoyMore(code):
            url = "https://web.vodafone.com.eg/services/promo/unifiedRedeemPromo"
            header = {
            'Host': 'web.vodafone.com.eg',
            'Connection': 'keep-alive',
            'msisdn': number,
            'api-host': 'PromoHost',
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 9; SM-J701F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36',
            'Origin': 'https://web.vodafone.com.eg',
            'Referer': 'https://web.vodafone.com.eg/ar/outofbundleoffer',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6'
            }
            data = {"msisdn":f"{number}","promoId":"2815","channelId":"1","shortcode":f"{code}","param1":"1","param2":"3","param3":"453","param4":"0.62","param5":"","category":"Non-Contextual"}
            res = req.post(url,headers=header,data=json.dumps(data))
            return res.json()['eDescription']

        # ###################################################
        def MI_LFC_Upgrade_PayDiff():
            url = "https://web.vodafone.com.eg/services/dxl/pom/productOrder"    
            header = {
            'Host': 'web.vodafone.com.eg',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'Authorization': f'Bearer {access_token}',
            'msisdn': number,
            'Accept-Language': 'EN',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
            'Content-Type': 'application/json',
            'Origin': 'https://web.vodafone.com.eg',
            'Referer': 'https://web.vodafone.com.eg/spa/miManagement',
            'Accept-Encoding': 'gzip, deflate, br'
            }
            jsonData = {"channel":{"name":"MobileApp"},"orderItem":[{"action":"add","product":{"characteristic":[{"name":"ExecutionType","value":"Sync"},{"name":"LangId","value":"en"}],"relatedParty":[{"id":f"{number}","name":"MSISDN","role":"Subscriber"}],"id":"MI_LFC_Upgrade_PayDiff","@type":"MI"}}],"@type":"MIProfile"}
            sendReq = req.post(url,headers=header,data=json.dumps(jsonData))
            res = sendReq.json()['state']
            return res 
        #################################################
        


        def result():
            if checkRollover() == -1 or checkRollover() == 1 :
                search = gifts()
                getCode = search[0:5]
                bundle = search
                if gifts() !=" No Enjoy More.":
                    # check = subEnjoyMore(getCode)
                    if 1>5:
                        pass
                    else:
                        while True:
                            check = subEnjoyMore(getCode)
                            if check == "Success":
                                if bundle.find("Bundle 10 LE") != -1:
                                    print(f" {MI_LFC_Upgrade_PayDiff()} [500MB]")
                                    break
                                elif bundle.find("Bundle 20 LE") != -1:
                                    print(f" {MI_LFC_Upgrade_PayDiff()} [1100MB]")
                                    break 
                                elif bundle.find("Bundle 30 LE") != -1:
                                    print(f" {MI_LFC_Upgrade_PayDiff()} [1800MB]")
                                    break
                                elif bundle.find("Bundle 40 LE") != -1:
                                    print(f" {MI_LFC_Upgrade_PayDiff()} [2500MB]")
                                    break
                                elif bundle.find("Bundle 60 LE") != -1:
                                    print(f" {MI_LFC_Upgrade_PayDiff()} [4GB]")
                                    break
                                elif bundle.find("Bundle 80 LE") != -1:
                                    print(f" {MI_LFC_Upgrade_PayDiff()} [6GB]")
                                    break
                                elif bundle.find("Bundle 100 LE") != -1:
                                    print(f" {MI_LFC_Upgrade_PayDiff()} [8GB]")
                                    break
                                elif bundle.find("Bundle 150 LE") != -1:
                                    print(f" {MI_LFC_Upgrade_PayDiff()} [12GB]")
                                    break
                                elif bundle.find("Bundle 250 LE") != -1:
                                    print(f" {MI_LFC_Upgrade_PayDiff()} [20GB]")
                                    break
                                elif bundle.find("Bundle 400 LE") != -1:
                                    print(f" {MI_LFC_Upgrade_PayDiff()} [40GB]")
                                    break                                   
                                break
                            else:
                                pass
                else:
                    print(" No offer")
            else:
                print(" Not Stop Rollover NEXT Month Flag.")                    
        result() 


