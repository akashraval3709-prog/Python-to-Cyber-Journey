from abc import ABC, abstractmethod
class BaseScanner(ABC):
    @abstractmethod
    def run_scan(self):
        pass
    @abstractmethod
    def export_log(self):
        pass


class PortScanner(BaseScanner):
    def __init__(self,target):
        self.__url=target
    def run_scan(self):
        print(f"port scan thay che{self.__url}")
    def export_log(self):
        print("all save")

port=PortScanner("https://instagram.com/p/123")

port.run_scan()
port.export_log()
# Accessing private variable using name mangling (for learning purpose)
print(port._PortScanner__url)