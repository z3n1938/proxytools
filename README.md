# Z3N1938 Proxy Tools v1.0  
**The ultimate all-in-one Python proxy toolkit** that lets you scrape, test, filter and export thousands of elite proxies in seconds — all from a clean, colorful terminal menu. Built for speed, anonymity and zero bans.

## Features
- **Scrape 300+ Live Sources (Bulk)**  
  Pull fresh proxies from 300+ auto-updated GitHub repos, APIs and public lists in under 30 seconds.

- **Ultra-Fast Elite Testing (300 Threads)**  
  Test every proxy for connectivity, latency, anonymity level and Cloudflare/Google bypass using 300 parallel threads.

- **ULTIMATE ELITE Filtering**  
  Only keeps high-anonymity, low-latency proxies that pass the toughest checks (perfect for Instagram, TikTok, Twitter, Selenium).

- **Smart Export System**  
  Auto-saves timestamped files:  
  `raw_proxies_20251110_223415.txt`  
  `working_proxies_20251110_223415.txt`  
  `elite_proxies_20251110_223415.txt`  
  `rotating_proxy.txt` (ready for Selenium/Scrapy)

- **Real-Time Colored Terminal**  
  Live stats, progress bars and beautiful ANSI colors powered by **colorama**.

- **Zero Config – Just Run**  
  No API keys, no login, no rate-limits. Works out of the box.

- **GitHub-Safe & Educational**  
  Fully compliant, MIT licensed, with clear “ethical use only” disclaimer.

## Requirements
```bash
pip install requests colorama
```
(Optional for SOCKS5 testing: `pip install requests[socks]`)

## Usage
```bash
python proxy_tools.py
```

Select an option from the menu:  
```
[1] Collect & Test All Proxies (300+ Sources)
[2] Show Elite Proxy Stats
[3] Export Rotating Proxy List
[4] Exit
```

- Option 1 → Scrapes + tests everything automatically  
- Option 3 → Instantly creates `rotating_proxy.txt` for your bots  

All files are saved in the same folder with timestamps — never overwrite your gold.

## Example Output
```
[+] 312 sources loaded
[+] 48,291 unique proxies collected
[+] Testing with 300 threads...
[+] 185.45.12.34:8080   |  142ms | ULTIMATE ELITE
[+] 2,104 elite proxies saved → elite_proxies_20251110_223415.txt
[+] rotating_proxy.txt → READY FOR SELENIUM
```

## Notes
- Works on **Windows, Linux, macOS**  
- 100% free & open source (MIT License)  
- Educational & ethical use only — never spam or abuse platforms  
- Proxies are public; quality varies — we just hunt the best ones  
- Star ⭐ the repo if you become unstoppable

```
One run → 2000+ elite proxies → Instagram falls, Cloudflare cries, you rule.
```


**by Z3N1938**  

**The hunt never ends. The throne is yours.** 👑🔥
