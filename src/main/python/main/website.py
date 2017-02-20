from main import *
from main.keystroke import printer, press
from main.log import my_log


class WebSite:
    def __init__(self, url):
        self.url = url


def ika(log):
    run(web_browser)
    web_site = WebSite("https://www.facebook.com/")
    printer(web_site.url)
    press("enter")


if __name__ == '__main__':
    ika(my_log)
