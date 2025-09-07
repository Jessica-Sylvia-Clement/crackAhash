# crackAhash v1.0 🍳  

_A fun egg-themed hash cracker!_  

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

---

## Features

- **Egg Hunt (`egg_hunt`)** → finds hashes hiding inside files  
- **Egg Grepper (`egg_grepper`)** → scans whole directories for eggs (hashes)  
- **Chef Threader (`chef_threader`)** → multiple chefs cracking eggs in parallel  
- **Multi-API Support** → free APIs (`hash-decrypt.io`, `md5decrypt.net`, etc.)  
- **Hashcat Integration** → fallback to local cracking with `rockyou.txt`  
- **Colorful Kitchen Logs** → shows which eggs cracked, burnt, or still in the pan  

---

## Usage

### Crack a single hash
```bash
python3 crackAhash.py -s 5f4dcc3b5aa765d61d8327deb882cf99
```
### Crack all hashes in a file
```bash
python3 crackAhash.py -f hashes.txt
```
### Hunt for hashes in a directory
```bash
python3 crackAhash.py -d /path/to/dir
```
## Requirements

- Python 3.x
- Hashcat (optional, for local cracking)
- Wordlist: `rockyou.txt` (comes with Kali Linux under `/usr/share/wordlists/rockyou.txt`)

Install Python dependencies:
```bash
pip install -r requirements.txt
```
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



