import requests
class HttpConnector:
    __api=""
    __data=""
    __r=None
    def __init__(self,urel):
        self.__url=urel
    def requester(self):
        self.__r=requests.get(self.__url)
        self.__data=self.__r.text
    def requester_post(self):
        self.__r.requests.post(self.__url,param)
    def last_data(self):
        return self.__data
