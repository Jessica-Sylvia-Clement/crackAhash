<h1 align="center">crackAhash 🍳</h1>
<p align="center">
  <b>A fun egg-themed hash cracker!</b>
</p>
<p align="center">
  <a href="https://docs.python.org/3/">
    <img src="https://img.shields.io/badge/python-3.x-blue.svg" />
  </a>
  <a href="https://github.com/Jessica-Sylvia-Clement/crackAhash/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-yellow.svg" />
  </a>
</p>

---

## What is crackAhash?

Welcome to **crackAhash** — where every hash is just an egg waiting to be cracked!  
Some shells split open with a single tap (online APIs), others need a good whack (Hashcat).  
Either way, we don’t leave the kitchen until the secrets are served hot. 🔥

```bash
                     _        /\     _                 _
  __  _ __ __ _  __ | | ___  /  \   | |__   __ _  ___ | |__
 / _|| '__/ _` |/ _|| |/  / / /\ \  | '_ \ / _` |/ __||  _ \.
| (_ [ | | (_| | (_||    / /  __  \ | | | | (_| |\__ \| | | |
 \__||_|  \__,_|\__||_|\_\/__/  \__\|_| |_|\__, ||___/|_| |_|
                                                 v1.0 by Jess
```
## The Story

### The Chef’s Kitchen of Secrets

As the **head chef**, our mission is simple: **crack the eggs (hashes), reveal the yolks (passwords/secrets), and turn them into delicious dishes (results).**

### 🥚 Identifying the eggs
Not all eggs are the same. Some are small like **MD5 quail eggs** that crack open easily, some a bit larger like **SHA1 or SHA256 chicken eggs** that take a bit more effort. And sometimes we get a giant **ostrich egg (bcrypt)** — but alas, we don’t yet have the right pan for that one, so it stays uncracked for now.  

### 👩‍🍳 How we crack them
Every egg can be cracked in one of three ways:  
1. **Ask a friend (API1)**   
2. **Ask another friend (API2)**   
3. **Smash it ourselves → use Hashcat, brute force with a trusty rock (wordlist)**   

### 🍽️ Orders big and small
Sometimes a customer just wants a single sunny-side-up (one hash).
Other times, we get a bulk restaurant order — it could be omelettes, boiled, poached… basically different egg dishes (a file full of hashes, of different types).
And occasionally, we cater a wedding with crates of eggs (an entire directory to scan). 

### 🧑‍🤝‍🧑 More chefs in the kitchen
When the restaurant is busy, we bring in more **chefs (threads)**.  
Each chef grabs an egg and cracks it in parallel, so the meals come out faster.  
And yes — even Chef Gordon Ramsay works for us when things get hectic😜.

### 📋 The kitchen report
At the end of service, we serve a neat summary:  
- ✅ How many eggs were cracked (secrets revealed).  
- ❌ Which eggs were burnt (not found).  
- 🚫 Which were exotic ostrich eggs (unsupported).  
- 🤷 Which turned out not to be eggs at all (unidentified).  

### 🍾 Closing time
When the last dish is served, the chefs hang up their aprons,  
wipe down the counters, and celebrate another day of cracked secrets.  

---

## Features

- **Egg Hunt (`egg_hunt`)** → finds hashes hiding inside files  
- **Egg Grepper (`egg_grepper`)** → scans whole directories for eggs (hashes)  
- **Chef Threader (`chef_threader`)** → multiple chefs cracking eggs in parallel  
- **Multi-API Support** → free APIs (`hash-decrypt.io`, `md5decrypt.net`, etc.)  
- **Hashcat Integration** → fallback to local cracking with `rockyou.txt`  
- **Colorful Kitchen Logs** → shows which eggs cracked, burnt, or still in the pan  

---
## Configuration (API Keys)

Some providers like [md5decrypt.net](https://md5decrypt.net) require an **email + API code**.

1. Register for a free account at [md5decrypt.net/register](https://md5decrypt.net/register).
2. Copy your **email** and **API code**.
3. Set them as environment variables in your terminal before running crackAhash:

### Linux / macOS
```bash
export MD5DECRYPT_EMAIL="youremail@example.com"
export MD5DECRYPT_CODE="your_api_code_here"
```
### Windows (PowerShell)
```bash
setx MD5DECRYPT_EMAIL "youremail@example.com"
setx MD5DECRYPT_CODE "your_api_code_here"
```
---
## Installation
### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/crackAhash.git
cd crackAhash
```
### 2. Install system-wide
```bash
sudo make install
```
### 3. Don’t want it anymore?
```bash
sudo make uninstall
```
--- 
## Usage

### Crack a single hash
```bash
crackAhash -s 5f4dcc3b5aa765d61d8327deb882cf99
```
### Crack all hashes in a file
```bash
crackAhash -f hashes.txt
```
### Hunt for hashes in a directory
```bash
crackAhash -d /path/to/dir
```
## Requirements

- Python 3.x
- Hashcat (optional, for local cracking)
- Wordlist: `rockyou.txt` (comes with Kali Linux under `/usr/share/wordlists/rockyou.txt`)

## Supported Hashes

- MD5
- SHA1
- SHA256
- SHA512
- (More coming soon)

## Example Output
- [🥚] Scrambling eggs...
- [🥄] Sorting eggs...
- [🍳] Eggs cooked: 5f4dcc3b5aa765d61d8327deb882cf99 : password (via md5decrypt.net) — thanks to Chef Gordon! 👩‍🍳
- [❌] Burnt batch: hash not found.



