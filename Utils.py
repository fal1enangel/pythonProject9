from bs4 import BeautifulSoup
 class html_reader:
     __text==""
     def __init__(self, text):
         self.__text=text
    def change_text(self,text):
        self.__text=text
    def parser(self):
        soup=BeautifulSoup(self.__text)
        return soup
    def find_all(self,teg,cls):
        soup = BeautifulSoup(self.__text)
        parse_test=soup.find_all(teg, class=cls)
        return parse_test