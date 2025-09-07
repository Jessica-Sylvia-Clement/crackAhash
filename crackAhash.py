#!/usr/bin/env python3
import re
import os
import requests
import argparse
import concurrent.futures
import subprocess
import urllib3
import threading

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ---------------- ARGUMENT PARSER ---------------- #
parser = argparse.ArgumentParser()
parser.add_argument('-s', help='hash', dest='hash')
parser.add_argument('-f', help='file containing hashes', dest='file')
parser.add_argument('-d', help='directory containing hashes', dest='dir')
parser.add_argument('-t', help='number of threads', dest='threads', type=int)
args = parser.parse_args()

# ---------------- COLORS & STATUS TAGS ---------------- #
end   = '\033[0m'
red   = '\033[91m'
green = '\033[92m'
white = '\033[97m'
yellow= '\033[93m'

cwd = os.getcwd()
directory = args.dir
file = args.file
thread_count = args.threads or 4
if directory and directory.endswith('/'):
    directory = directory[:-1]

# ---------------- ASCII BANNER ---------------- #
BANNER_TEXT = r"""
                     _        /\     _                 _
  __  _ __ __ _  __ | | ___  /  \   | |__   __ _  ___ | |__
 / _|| '__/ _` |/ _|| |/  / / /\ \  | '_ \ / _` |/ __||  _ \.
| (_ [ | | (_| | (_||    / /  __  \ | | | | (_| |\__ \| | | |
 \__||_|  \__,_|\__||_|\_\/__/  \__\|_| |_|\__, ||___/|_| |_|

"""
def show_banner():
    print(f"{green}{BANNER_TEXT}{end}")
    
    # align signature under "hash"
    spaces = " " * (len("   ____                _          ") + 22)
    print(f"{red}{spaces}crackAhash v1.0 by Jess{end}\n")
    
    print(f"Welcome to crackAhash — where every hash is just an egg waiting to be cracked.")
    print("Some shells split open with a single tap (APIs), others need a good whack (hashcat brute force).")
    print("But either way, we don’t leave the kitchen until the secrets are served hot! 🍳🥚\n")

info = f"{yellow}[🥚] Scrambling eggs...{end}"           
run  = f"{white}[🥄] Sorting eggs...{end}"         
good = f"{green}[🍳] Eggs cooked: hash cracked!{end}" 
bad  = f"{red}[❌] Burnt batch: hash not found.{end}" 

# ---------------- API FUNCTIONS ---------------- #

def api_hashdecrypt(hashvalue, hashtype):
    """Uses hash-decrypt.io (free, supports many algorithms)"""
    url = f"https://api.hash-decrypt.io/v1/{hashtype}/{hashvalue}"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            txt = (r.text or "").strip()
            if txt and not txt.lower().startswith("error"):
                return (txt, "hash-decrypt.io")
    except:
        pass
    return False


def api_md5decrypt(hashvalue, hashtype):
    """Uses md5decrypt.net (requires API key + email from env vars)"""
    email = os.getenv("MD5DECRYPT_EMAIL")
    code = os.getenv("MD5DECRYPT_CODE")
    if not email or not code:
        return False
    try:
        url = (
            f"https://md5decrypt.net/Api/api.php?"
            f"hash={hashvalue}&hash_type={hashtype}&email={email}&code={code}"
        )
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            txt = (r.text or "").strip()
            # don't treat provider error messages as cracked plaintexts
            if not txt or "CODE ERREUR" in txt.upper() or "ERROR" in txt.upper():
                return False
            return (txt, "md5decrypt.net")
    except:
        pass
    return False


def local_hashcat(hashvalue, hashtype):
    """Fallback to hashcat (rockyou.txt wordlist) — actually crack, then --show"""
    modes = {"md5": 0, "sha1": 100, "sha256": 1400, "sha512": 1700}
    mode = modes.get(hashtype)
    if not mode:
        return False

    tmp = "temp_hash.txt"
    pot = os.path.join(cwd, ".crackAhash.potfile")

    # Write hash to temp file
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(hashvalue.strip() + "\n")

    try:
        # 1) do an actual crack attempt (quiet)
        subprocess.run([
            "hashcat", "-m", str(mode), "-a", "0", tmp,
            "/usr/share/wordlists/rockyou.txt",
            "--potfile-path", pot, "--quiet", "--status", "--status-timer", "9999"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)

        # 2) then show crack result from potfile
        out = subprocess.check_output([
            "hashcat", "-m", str(mode), "--show", tmp, "--potfile-path", pot, "--quiet"
        ], stderr=subprocess.DEVNULL).decode().strip()

        if out and ":" in out:
            return (out.split(":", 1)[1], "hashcat")
    except:
        pass
    finally:
        try:
            os.remove(tmp)
        except:
            pass
    return False

# ---------------- DETECTION ---------------- #
def detect_type(hashvalue):
    """Guess hash type by length/prefix"""
    hv = hashvalue.strip().lower()

    if len(hv) == 32:
        return "md5"      # could also be NTLM or MD4
    elif len(hv) == 40:
        return "sha1"
    elif len(hv) == 64:
        return "sha256"
    elif len(hv) == 128:
        return "sha512"
    elif len(hv) == 16:
        return "mysql-old"
    elif hv.startswith(("$2y$", "$2a$", "$2b$")) and len(hv) == 60:
        return "bcrypt"
    return None

# ---------------- CRACK LOGIC ---------------- #
apis = [api_hashdecrypt, api_md5decrypt, local_hashcat]
result = {}

# counters
cracked_count = 0
unsupported_count = 0
unidentified_count = 0
notfound_count = 0

def crack(hashvalue):
    global unsupported_count, unidentified_count, notfound_count, cracked_count

    hashtype = detect_type(hashvalue)
    if not hashtype:
        print(f"{bad} Could not identify hash type: {hashvalue}")
        unidentified_count += 1
        return ("unidentified", None)

    print(f"{info} Trying {hashtype.upper()} for {hashvalue}")

    # unsupported
    if hashtype in ["bcrypt", "mysql-old"]:
        print(f"{bad} Unsupported hash: {hashtype} cracking not implemented yet")
        unsupported_count += 1
        return ("unsupported", None)

    # try APIs / hashcat
    for api in apis:
        res = api(hashvalue, hashtype)
        if res:
            cracked_count += 1
            return ("cracked", res)

    print(f"{bad} {hashvalue} : Hash was not found in any database")
    notfound_count += 1
    return ("notfound", None)

CHEF_NAMES = [
    "Gordon", "Julia", "George", "Ramsay", "Gary",
    "Sanjeev", "Curtis", "Matt"
]
chef_map = {}

def get_chef_name():
    tid = threading.get_ident()
    if tid not in chef_map:
        chef_map[tid] = CHEF_NAMES[len(chef_map) % len(CHEF_NAMES)]
    return chef_map[tid]

def chef_threader(hashvalue):
    chef = get_chef_name()
    status, resp = crack(hashvalue)
    if status == "cracked":
        plain, source = resp
        print(f"{good} {hashvalue} : {plain} (via {source}) — thanks to Chef {chef}! 👨‍")
        result[hashvalue] = resp
    # all other statuses already printed inside crack()

def egg_grepper(directory):
    cmd = r'''grep -Pr -o '\$2[aby]\$\d{2}\$[./A-Za-z0-9]{53}|[A-Fa-f0-9]{128}|[A-Fa-f0-9]{96}|[A-Fa-f0-9]{64}|[A-Fa-f0-9]{40}|[A-Fa-f0-9]{32}|[A-Fa-f0-9]{16}' --exclude-dir=.git --exclude=*.{png,jpg,jpeg,mp3,mp4,zip,gz} %s >> %s/%s.txt''' % (directory, cwd, directory.split('/')[-1])
    os.system(cmd)
    print('%s Results saved in %s.txt' % (info, directory.split('/')[-1]))

def egg_hunt(file):
    global cracked_count, unsupported_count, unidentified_count, notfound_count
    lines = []
    tokens = set()

    with open(file, 'r', errors='ignore') as f:
        for line in f:
            lines.append(line.strip('\n'))

    # regex: bcrypt + hex hashes
    pattern = re.compile(
        r'\$2[aby]\$\d{2}\$[./A-Za-z0-9]{53}|'
        r'[A-Fa-f0-9]{128}|'
        r'[A-Fa-f0-9]{96}|'
        r'[A-Fa-f0-9]{64}|'
        r'[A-Fa-f0-9]{40}|'
        r'[A-Fa-f0-9]{32}|'
        r'[A-Fa-f0-9]{16}'
    )

    for line in lines:
        matches = pattern.findall(line)
        for m in matches:
            tokens.add(m)

    total = len(tokens)
    if total == 0:
        print(f"{bad} No valid hashes found in file.")
        return

    # print scrambling eggs before starting cracking
    print(run)

    # process with threads
    threadpool = concurrent.futures.ThreadPoolExecutor(max_workers=thread_count)
    futures = (threadpool.submit(chef_threader, hv) for hv in tokens)
    for i, _ in enumerate(concurrent.futures.as_completed(futures), 1):
        print(f"{info} Progress: {i}/{total}")

    # Print final summary AFTER cracking
    print(f"{info} Hashes to crack: {len(tokens)} "
          f"(total {total}, unsupported {unsupported_count}, "
          f"unidentified {unidentified_count}, not found {notfound_count}, cracked {cracked_count})")
     
    # Close the thread pool cleanly   
    threadpool.shutdown(wait=True)

def single(args):
    status, res = crack(args.hash)
    if status == "cracked":
        plain, source = res
        print(f"{good} {args.hash} : {plain} (via {source})")


# ---------------- MAIN ---------------- #
if __name__ == "__main__":
    show_banner()

    if directory:
        try:
            egg_grepper(directory)
        except KeyboardInterrupt:
            pass

    elif file:
        try:
            egg_hunt(file)
        except KeyboardInterrupt:
            pass
        with open('cracked-%s' % file.split('/')[-1], 'w+') as f:
            for hashvalue, cracked in result.items():
                plain, source = cracked
                f.write(hashvalue + ':' + plain + f" (via {source})\n")
        print('%s Results saved in cracked-%s' % (info, file.split('/')[-1]))

    elif args.hash:
        single(args)

print(f"\n{yellow}crackAhash completed — kitchen closed.{end}")
