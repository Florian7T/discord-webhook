import requests,json,os
from colorama import Fore

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(Fore.BLUE + """
     __          __  _     _                 _    
     \ \        / / | |   | |               | |   
      \ \  /\  / /__| |__ | |__   ___   ___ | | __
       \ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ /
        \  /\  /  __/ |_) | | | | (_) | (_) |   < 
         \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\\

    """ + Fore.WHITE)

clear()

self_avatar = ""
base_url = "https://discord.com/api/webhooks/WEBHOOK_ID/WEBHOOK_TOKEN"
url = ""

while True:
    option2 = input("""Login:
[1] URL
[2] ID + Token 
""")
    if option2=="1":
        url = input(Fore.CYAN+"Webhook URL ~> "+Fore.WHITE)
        break
    elif option2=="2":
        webhook_id = input(Fore.CYAN+"Webhook ID ~> "+Fore.WHITE)
        webhook_token = input(Fore.CYAN + "Webhook Token ~> " + Fore.WHITE)
        url = base_url.replace("WEBHOOK_ID",webhook_id).replace("WEBHOOK_TOKEN",webhook_token)
        break
    else:
        print(Fore.RED+"Invalid option: "+option2+Fore.WHITE)

# check webhook
rq = requests.get(url)
if rq.status_code == 200:
    clear()
    print(Fore.GREEN+"HTTP 200 Token and ID valid. Session Started"+Fore.WHITE)
    print()
else:
    print(Fore.RED+f"HTTP {rq.status_code}. Token or/and ID might not be valid. Program will now exit.."+Fore.WHITE)
    exit(0)



while True:
    option=input(f"""Options:
[1] Chat Session
[2] Edit webhook
{Fore.RED}[3] Delete Webhook {Fore.WHITE}
""")
    if option == "1":
        clear()
        print(Fore.BLUE+"Session Started! (\'exit\' to exit)")
        while True:
            inp = input(Fore.CYAN+'~> '+Fore.WHITE)
            if inp == "exit":
                clear()
                break
            data = {"content": inp}
            if self_avatar!="":
                data['avatar_url']=self_avatar

            x=requests.post(url, data=json.dumps(data), headers={ "Content-Type": "application/json"})
            if x.status_code == 204:
                print(Fore.GREEN+"HTTP 204: Succes!"+Fore.WHITE)
            else:
                print(Fore.YELLOW+f"HTTP {x.status_code}: Action might've failed"+Fore.WHITE)
    elif option == "2":
        print(Fore.BLUE + "Enter blank for default"+Fore.WHITE)
        name = input(Fore.CYAN+"Custom Name ~> "+Fore.WHITE)
        avatar = input(Fore.CYAN+"Custom Avatar Url ~> "+Fore.WHITE)
        data = {"name":name,"avatar":avatar}
        self_avatar=avatar
        x = requests.patch(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
        if x.status_code == 200:
            clear()
            print(Fore.GREEN+"HTTP 200: Succes!"+Fore.WHITE)
        else:
            print(Fore.YELLOW+f"HTTP {x.status_code}: Action might've failed"+Fore.WHITE)
    elif option == "3":
        clear()
        yn = input(Fore.CYAN+"Are you sure? (y/n) ~> "+Fore.WHITE)
        if yn == "y":
            inp = input(Fore.CYAN+"Any last words (Leave blank for none) ~> "+Fore.WHITE)
            if inp != "":
                data = {"content": inp}
                x = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
                if x.status_code == 204:
                    print(Fore.GREEN + "HTTP 204: Succes!" + Fore.WHITE)
                else:
                    print(Fore.YELLOW + f"HTTP {x.status_code}: Action might've failed" + Fore.WHITE)
            print()
            rq = requests.delete(url)
            if rq.status_code == 204:
                print(Fore.GREEN+"HTTP 204 from Discord: Webhook deleted succesfully. The Program will now exit.."+Fore.WHITE)
            else:
                print(Fore.YELLOW+f"HTTP {rq.status_code}: Action might've failed. The Program will now exit.."+Fore.WHITE)
            exit(0)
        else:
            clear()

    else:
        print(Fore.YELLOW+f"Invalid option: {option}\n"+Fore.WHITE)
