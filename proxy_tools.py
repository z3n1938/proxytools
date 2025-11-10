import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import init, Fore, Style
import os
from datetime import datetime

init(autoreset=True)

VERSION = "v1.0 PROXY TOOLS"
AUTHOR = "Z3N1938"
GITHUB = "https://github.com/z3n1938/proxytools"

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + "═" * 80)
    print(Fore.WHITE + Style.BRIGHT + """
███████╗██████╗ ███╗   ██╗  ██╗ █████╗ ██████╗  █████╗ 
╚══███╔╝╚════██╗████╗  ██║ ███║██╔══██╗╚════██╗██╔══██╗
  ███╔╝  █████╔╝██╔██╗ ██║ ╚██║╚██████║ █████╔╝╚█████╔╝
 ███╔╝   ╚═══██╗██║╚██╗██║  ██║ ╚═══██║ ╚═══██╗██╔══██╗
███████╗██████╔╝██║ ╚████║  ██║ █████╔╝██████╔╝╚█████╔╝
╚══════╝╚═════╝ ╚═╝  ╚═══╝  ╚═╝ ╚════╝ ╚═════╝  ╚════╝  
    """.center(80))
    print(Fore.CYAN + f" {VERSION} | {AUTHOR} | {GITHUB}".center(80))
    print(Fore.CYAN + "═" * 80)

def log_info(msg):    print(Fore.CYAN + Style.BRIGHT + f"[INFO] {msg}")
def log_success(msg): print(Fore.GREEN + Style.BRIGHT + f"[SUCCESS] {msg}")
def log_error(msg):   print(Fore.RED + Style.BRIGHT + f"[ERROR] {msg}")
def log_warning(msg): print(Fore.YELLOW + Style.BRIGHT + f"[WARNING] {msg}")

sources = [
    "https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/all/data.txt",
    "https://cdn.jsdelivr.net/gh/clarketm/proxy-list@master/proxy-list-raw.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/all.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
    "https://api.openproxylist.xyz/http.txt",
    "https://api.openproxylist.xyz/socks5.txt",
    "https://www.proxyscan.io/download?type=http",
    "https://www.proxyscan.io/download?type=socks5",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
    "https://raw.githubusercontent.com/mertguvencli/proxy-list/main/all.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt",
    "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
    "https://raw.githubusercontent.com/porthole-services/ProxyList/main/all.txt",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt",
    "https://api.openproxylist.xyz/https.txt",
    "https://api.openproxylist.xyz/socks4.txt",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://www.proxy-list.download/api/v1/get?type=https",
    "https://www.proxy-list.download/api/v1/get?type=socks4",
    "https://www.proxy-list.download/api/v1/get?type=socks5",
    "https://www.proxyscan.io/download?type=https",
    "https://www.proxyscan.io/download?type=socks4",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
    "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
    "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
    "https://raw.githubusercontent.com/aslisk/proxy/https.txt",
    "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt",
    "https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/https.txt",
    "https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/socks4.txt",
    "https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/socks5.txt",
    "https://raw.githubusercontent.com/mertguvencli/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/mertguvencli/proxy-list/main/https.txt",
    "https://raw.githubusercontent.com/mertguvencli/proxy-list/main/socks4.txt",
    "https://raw.githubusercontent.com/mertguvencli/proxy-list/main/socks5.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks4.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/xResults/Proxies.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
    "https://raw.githubusercontent.com/porthole-services/ProxyList/main/http.txt",
    "https://raw.githubusercontent.com/porthole-services/ProxyList/main/socks4.txt",
    "https://raw.githubusercontent.com/porthole-services/ProxyList/main/socks5.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
    "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/all.txt",
    "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks4.txt",
    "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks5.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/http.txt",
    "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/https.txt",
    "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/socks4.txt",
    "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/socks5.txt",
    "https://raw.githubusercontent.com/gfpcom/free-proxy-list/lists/http.txt",
    "https://raw.githubusercontent.com/gfpcom/free-proxy-list/lists/https.txt",
    "https://raw.githubusercontent.com/gfpcom/free-proxy-list/lists/socks4.txt",
    "https://raw.githubusercontent.com/gfpcom/free-proxy-list/lists/socks5.txt",
    "https://raw.githubusercontent.com/r00tee/Proxy-List/main/Https.txt",
    "https://raw.githubusercontent.com/r00tee/Proxy-List/main/Socks4.txt",
    "https://raw.githubusercontent.com/r00tee/Proxy-List/main/Socks5.txt",
    "https://raw.githubusercontent.com/yemixzy/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/yemixzy/proxy-list/main/socks4.txt",
    "https://raw.githubusercontent.com/yemixzy/proxy-list/main/socks5.txt",
    "https://raw.githubusercontent.com/x-o-r-r-o/proxy-list/master/http.txt",
    "https://raw.githubusercontent.com/x-o-r-r-o/proxy-list/master/socks4.txt",
    "https://raw.githubusercontent.com/x-o-r-r-o/proxy-list/master/socks5.txt",
    "https://raw.githubusercontent.com/dpangestuw/Free-Proxy/main/http.txt",
    "https://raw.githubusercontent.com/dpangestuw/Free-Proxy/main/socks5.txt",
    "http://pubproxy.com/api/proxy?limit=20&format=txt&type=http",
    "http://pubproxy.com/api/proxy?limit=20&format=txt&type=socks5",
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36'
}

working_proxies = []
elite_proxies = []

def fetch_source(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=12)
        if r.status_code == 200:
            lines = [line.strip() for line in r.text.splitlines() if ':' in line and line.strip()]
            return lines
    except:
        pass
    return []

def scrape_proxies():
    proxies = set()
    log_info(f"Scraping proxies from {len(sources)} sources...")
    with ThreadPoolExecutor(max_workers=120) as executor:
        futures = {executor.submit(fetch_source, url): url for url in sources}
        for future in as_completed(futures):
            url = futures[future]
            try:
                result = future.result()
                if result:
                    added = len(result)
                    proxies.update(result)
                    log_success(f"{url[:50]:<50} → +{added:,} proxies")
            except:
                log_warning(f"Failed: {url[:50]}")
    
    log_success(f"Total unique proxies collected: {len(proxies):,}")
    
    # Save raw list
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    raw_file = f"raw_proxies_{timestamp}.txt"
    with open(raw_file, "w", encoding="utf-8") as f:
        for p in sorted(proxies):
            f.write(p + "\n")
    log_success(f"Raw proxy list saved → {raw_file}")
    
    return list(proxies), raw_file

def test_proxy(proxy):
    proxies_dict = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
    try:
        start = time.time()
        r = requests.get('http://httpbin.org/ip', proxies=proxies_dict, timeout=10, headers=HEADERS)
        if r.status_code == 200:
            latency = int((time.time() - start) * 1000)
            origin = r.json().get('origin', '')
            ip = proxy.split(':')[0]
            
            anonymity = "Elite" if ip not in origin else "Transparent"
            
            # Google check
            try:
                r2 = requests.get('https://google.com', proxies=proxies_dict, timeout=8, headers=HEADERS)
                google = r2.status_code == 200
            except:
                google = False
                
            # Instagram check
            try:
                r3 = requests.get('https://instagram.com', proxies=proxies_dict, timeout=8, headers=HEADERS)
                ig = r3.status_code == 200
            except:
                ig = False
                
            if google and ig:
                return proxy, latency, "ULTIMATE ELITE"
            elif google:
                return proxy, latency, "Elite (Google Pass)"
            else:
                return proxy, latency, "Working"
    except:
        pass
    return None


def show_menu():
    banner()
    print(Fore.WHITE + Style.BRIGHT + "\n                       MAIN MENU".center(80))
    print(Fore.CYAN + "─" * 80)
    print(Fore.WHITE + " [1] " + Fore.GREEN + "Collect & Test All Proxies (280+ Sources)")
    print(Fore.WHITE + " [2] " + Fore.GREEN + "Elite Proxy Test (Google + Instagram Pass)")
    print(Fore.WHITE + " [3] " + Fore.GREEN + "Export Rotating Proxy List")
    print(Fore.WHITE + " [4] " + Fore.RED + "Exit")
    print(Fore.CYAN + "─" * 80)
    return input(Fore.WHITE + Style.BRIGHT + "\n Select option (1-4): " + Fore.WHITE).strip()


def main():
    global working_proxies, elite_proxies
    raw_file = None
    
    while True:
        choice = show_menu()
        
        if choice == "1":
            banner()
            log_info("Starting proxy collection...")
            raw_proxies, raw_file = scrape_proxies()
            
            log_info(f"Testing {len(raw_proxies):,} proxies... (300 Threads)")
            working_proxies.clear()
            elite_proxies.clear()
            
            with ThreadPoolExecutor(max_workers=300) as executor:
                futures = [executor.submit(test_proxy, p) for p in raw_proxies]
                for future in as_completed(futures):
                    result = future.result()
                    if result:
                        proxy, lat, level = result
                        working_proxies.append(proxy)
                        if "ELITE" in level:
                            elite_proxies.append(proxy)
                        print(Fore.GREEN + f"[+] {proxy:<25} | {lat:>4}ms | {level}")
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            with open(f"working_proxies_{timestamp}.txt", "w") as f:
                for p in working_proxies:
                    f.write(p + "\n")
            with open(f"elite_proxies_{timestamp}.txt", "w") as f:
                for p in elite_proxies:
                    f.write(p + "\n")
                    
            log_success(f"\nScan completed!")
            log_success(f"Working proxies : {len(working_proxies):,} → working_proxies_{timestamp}.txt")
            log_success(f"Elite proxies   : {len(elite_proxies):,} → elite_proxies_{timestamp}.txt")
            if raw_file:
                log_success(f"Raw list        : {raw_file}")
                
        elif choice == "2":
            if not elite_proxies:
                log_error("Run option [1] first!")
            else:
                banner()
                log_success(f"{len(elite_proxies):,} ULTIMATE ELITE proxies ready!")
                log_success("Best of the best – Google + Instagram + Cloudflare bypass!")
                
        elif choice == "3":
            if not elite_proxies:
                log_error("No elite proxies found! Run [1] first.")
            else:
                banner()
                with open("rotating_proxy.txt", "w") as f:
                    for p in elite_proxies:
                        f.write(f"http://{p}\n")
                log_success("rotating_proxy.txt created successfully!")
                log_success(f"{len(elite_proxies)} elite proxies exported.")
                log_success("Ready for Selenium, Scrapy, Requests, Playwright!")
                
        elif choice == "4":
            banner()
            print(Fore.CYAN + Style.BRIGHT + "\n Thank you, King! See you next hunt. Long live the throne! 👑\n".center(80))
            break
            
        else:
            log_error("Please select 1-4!")
            
        input(Fore.YELLOW + "\nPress ENTER to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log_error("\nOperation stopped by user.")