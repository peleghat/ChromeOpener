import subprocess

URLS = [
    'https://web.whatsapp.com/',
    'https://mail.google.com/mail/u/0/#inbox',
    'https://mail.google.com/mail/u/1/#inbox',
    'https://mail.google.com/mail/u/2/#inbox',
    'https://www.instagram.com/',
    'https://www.facebook.com/',
    'https://www.linkedin.com/feed/',
    'https://calendar.google.com/calendar/u/0',
    'https://keep.google.com/u/0/'
]


def generic_open_urls(chrome_path: list[str]):
    def open_new_window(_chrome_path: list[str]):
        subprocess.Popen(_chrome_path).wait()  # Open a new window, wait for process to finish.

    def open_tabs(_chrome_path: list[str], url: str):
        subprocess.Popen(_chrome_path + [url]).wait()  # Open all tabs, wait for process to finish.

    open_new_window(chrome_path)
    list(map(lambda url: open_tabs(chrome_path, url), URLS))


def open_urls_for_macos():
    generic_open_urls(chrome_path=['open', '-na', 'Google Chrome'])


def open_urls_for_windows():
    windows_chrome_path = ["C:/Program Files/Google/Chrome/Application/chrome.exe"]
    icloud_url = "https://www.icloud.com/"
    generic_open_urls(chrome_path=windows_chrome_path)
    subprocess.Popen(windows_chrome_path + [icloud_url]).wait()  # Since it's windows, open ICloud as well.
