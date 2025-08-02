import requests

url = "http://example.com"
path_to_wordlist = "wordlist.txt"

headers = {
    "User-Agent": "Mozilla/5.0 (CTF-Dirbuster)"
}

def web_directory_brute_force():

    # open the file and store each line of the wordlist in an array
    with open(path_to_wordlist, "r", encoding="utf-8", errors="ignore") as file:
        wordlist = [line.strip() for line in file]

    # loop over the list and make request
    for word in wordlist: 
        full_url = f"{url}/{word}/"
        try: 
            # makes request
            response = requests.get(full_url, headers=headers, timeout=5)
            # print found if url returns 200 status code
            if response.status_code == 200:
                print(f"[+] Found: {full_url}")
            # print forbidden if url returns 403 status code
            elif response.status_code == 403: 
                print(f"[!] Forbidden (403): {full_url}")
        except requests.RequestException:
            print(f"[-] Error requesting: {full_url}")

if __name__ == "__main__":
    web_directory_brute_force()