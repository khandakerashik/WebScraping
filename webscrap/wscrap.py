from urllib.request import urlopen
from bs4 import BeautifulSoup

#Global variable
url_amz="https://www.amazon.com/Protector-Charging-Station5ft-Extension-110-250V/dp/B07MPPMZMH/ref=lp_16225007011_1_7?s=computers-intl-ship&ie=UTF8&qid=1556350762&sr=1-7"
filepath="html/amz.html"

url_bkpk="https://backpackbang.com/item/BPXO8ODSCK?sid=34b47e37132eb734&spage=1&spos=18&track=eyJxdWVyeSI6ImFwcGxlIiwiaW5kZXgiOjE4LCJ3aXNobGlzdGVkSXRlbVNvdXJjZSI6InNlYXJjaCIsInBhZ2UiOjEsInNvdXJjZSI6Ii9zZWFyY2gifQ%3D%3D"
filepath="html/bkpk.html"

class HomeScraper:
    __url = ''
    __data = ''
    __wlog = None
    __soup = None

    def __init__(self,url,wlog):
        self.__url=url
        self.__wlog=wlog

    def retrieve_webpage(self):
        try:
            html=urlopen(self.__url)
        except Exception as e:
            print(e)
            self.__wlog.report(e)
        else:
            self.__data=html.read()
            if len(self.__data)>0:
                print("Retrieved Successfully!")  
    def write_webpage_as_html(self,filepath=filepath,data=''):
        try:
            with open(filepath,'wb') as fobj:
                if data:
                    fobj.write(data)
                else:
                    fobj.write(self.__data)
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))      
    
    def read_webpage_from_html(self,filepath=filepath):
        try:
            with open(filepath) as fobj:
                self.__data=fobj.read()
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))

    def change_url(self,url):
        self.__url= url
    
    def print_data(self):
        print(self.__data)

    def convert_data_to_bs4(self):
        self.__soup=BeautifulSoup(self.__data,"html.parser")

    def parse_soup_to_simple_html(self):
        product_list= self.__soup.find_all(['h1','h2','h3','h4'])

        print (product_list)