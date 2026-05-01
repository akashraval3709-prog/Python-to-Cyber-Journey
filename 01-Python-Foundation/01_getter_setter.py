class Download:
    def __init__(self,url):
        self.__url=url

    @property
    def link(self):
        return f"Checking: {self.__url}"

    @link.setter
    def link (self,value):
        if value and "instagram.com" in value:
            self.__url=value  
        else:
            raise ValueError("Invalid Instagram Link")

obj=Download("instagram.com")
print(obj.link)
obj.link="https://instagram.com/p/123"
print(obj.link)