A fun egg-themed hash cracker!

                     _        /\     _                 _   
  __  _ __ __ _  __ | | ___  /  \   | |__   __ _  ___ | |__ 
 / _|| '__/ _` |/ _|| |/  / / /\ \  | '_ \ / _` |/ __||  _ \
| (_ [ | | (_| | (_||    / /  __  \ | | | | (_| |\__ \| | | |
 \__||_|  \__,_|\__||_|\_\/__/  \__\|_| |_|\__, ||___/|_| |_| 
                                           crackAhash v1.0 by Jess

🍳 What is crackAhash?

Welcome to crackAhash — where every hash is just an egg waiting to be cracked!
Some shells split open with a single tap (online APIs), others need a good whack (Hashcat).
Either way, we don’t leave the kitchen until the secrets are served hot. 🔥

🧑‍🍳 Features

Egg Hunt (egg_hunt) → finds hashes hiding inside files
Egg Grepper (egg_grepper) → scans whole directories for eggs (hashes)
Chef Threader (chef_threader) → lets multiple chefs crack eggs (parallel cracking)
Multi-API Support → cracks hashes with free APIs (hash-decrypt.io, md5decrypt.net, etc.)
Hashcat Integration → fallback to local cracking using rockyou.txt
Colorful Kitchen Logs → see which eggs cracked, burnt, or still in the pan

🥄 Usage

Crack a single hash:
python3 crackAhash.py -s 5f4dcc3b5aa765d61d8327deb882cf99

Crack all hashes in a file:
python3 crackAhash.py -f hashes.txt

Hunt for hashes in a directory:
python3 crackAhash.py -d /path/to/dir

📦 Requirements

Python 3.x
Hashcat
 (optional, for local cracking)
Wordlist: rockyou.txt (ships with Kali Linux under /usr/share/wordlists/rockyou.txt)

Install Python deps:
pip install -r requirements.txt

🥚 Supported Hashes

MD5
SHA1
SHA256
SHA512
(More coming soon — scrambled, sunny side up, and over easy 😏)

🍳 Example Output
[🥚] Scrambling eggs...
[🥄] Sorting eggs...
[🍳] Eggs cooked: 5f4dcc3b5aa765d61d8327deb882cf99 : password (via md5decrypt.net)
[❌] Burnt batch: hash not found.
