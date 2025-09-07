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
<img width="627" height="136" alt="Screenshot 2025-09-07 205409" src="https://github.com/user-attachments/assets/a0af0e7b-6894-454c-b9bb-b39b7bdb0383" />

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
- [🍳] Eggs cooked: 5f4dcc3b5aa765d61d8327deb882cf99 : password (via md5decrypt.net)
- [❌] Burnt batch: hash not found.



