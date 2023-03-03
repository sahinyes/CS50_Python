import re
import sys
import requests
from colorama import Fore, Style
import pyfiglet

#Banner
print(pyfiglet.figlet_format("CS50 @sahinyes\nFinal Project", font= "digital"))
print(f"{Fore.YELLOW}python ./project.py\npython ./project.py -u <url>\npython ./project.py --url <url>\n{Style.RESET_ALL}")

def main():
    global l
    l = []
    is_regex(url_valid())
    if int(len(l)) != 0:
        for i in range(len(l)):
            req(l[i])
            i += 1    
    else:
        pass


#URL validation
def url_valid():
    if len(sys.argv) == 1:
        url = input("URL:")
        return url
    elif len(sys.argv) != 3: 
        sys.exit(f"{Fore.RED}Should be three argument <<python ./project -u or --url >>{Style.RESET_ALL}")
    elif str(sys.argv[1]) != "-u" and str(sys.argv[1]) != "--url":
        sys.exit(f"{Fore.RED}Need -u or --url flag{Style.RESET_ALL}")
    else:
        url = str(sys.argv[2])
        return url            

def is_regex(url):
    if re_url := re.findall(r"^https?://.*", url):
        global g_url
        g_url = re_url[0]
        return req(g_url)
    else:
        print(f"{Fore.RED}URL is not valid{Style.RESET_ALL}")
        return False


#Request 
def req(url):
    try:
        r = requests.get(url)
        if int(r.status_code) <= 302:
            print(f"{url} {Fore.GREEN}Status: {r.status_code}{Style.RESET_ALL} Size: {len(r.content)}")            
        elif int(r.status_code) >= 500:
            print(f"{url} {Fore.YELLOW}Status: {r.status_code}{Style.RESET_ALL} Size: {len(r.content)}")
        elif int(r.status_code) == 403 :
            print(f"{url} {Fore.RED}Status: {r.status_code}{Style.RESET_ALL} Size: {len(r.content)}")
        elif int(r.status_code) == 404:
            print(f"{url} {Fore.WHITE}Status: {r.status_code}{Style.RESET_ALL} Size: {len(r.content)}")
        else:
            print(f"{url} {Fore.YELLOW}Status: {r.status_code}{Style.RESET_ALL} Size: {len(r.content)}")
        return dir(r), comment(r), True
    except:
        sys.exit(f"{Fore.RED}Cannot not request to website{Style.RESET_ALL}")
    
#Comment lines
def comment(r):
    comments = re.findall(r"<!--[\s\S]*?-->", r.text)
    global com_l
    com_l = []
    
    if len(comments) == 0:
        print(f"{Fore.YELLOW}No comment line founded{Style.RESET_ALL}") 
    else:
        print(f"{Fore.GREEN}# COMMENT LINES{Style.RESET_ALL}") 
        for comment in comments:
            a = comment.replace("<!--", "#").replace("-->","")
            if a not in com_l: com_l.append(a)
            print(f"{Fore.CYAN}{a}{Style.RESET_ALL}")  


#Check Directories
def dir(r):
    try:
        dirs = re.findall(r"href=[\"']?(?!http|mailto)([^\"'#@>]+\.?\w+)", r.text)
        #print(f"{Fore.YELLOW}Possible Directories: {len(dirs)}{Style.RESET_ALL}")
        return scanner(dirs)
    except:
        print("Cannot discover directories")


#Dirscanner
def scanner(dirs):
    for dir in dirs:
        new_u = str(g_url).removesuffix("/") + "/" + str(dir).replace("/","",1).replace(".","",1)
        if new_u not in l:
            l.append(new_u)
        else:
            pass                  


if __name__ == "__main__":
    main()

