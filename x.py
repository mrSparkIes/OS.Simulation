class OperSystem():
    def __init__(self, name, is_supported, version, company, price, weight):
        self.name = name
        self.is_supported = is_supported
        self.version = version
        self.company = company
        self.price = price
        self.weight = weight
        

#  ----------------------------------------------------------------------------  #
        
##  Classes for OS'es which will be used later on in main.py  ##
        
class Windows(OperSystem):
    def __init__(self, name, is_supported, version, company, price, weight):
        super().__init__(name, is_supported, version, company, price, weight)
        self.name = 'Windows 7'
        self.is_supported = True
        self.version = 7.0
        self.company = 'Microsoft'
        self.price = 0
        self.weight = 7200

class macOS(OperSystem):
    def __init__(self, name, is_supported, version, company, price, weight):
        super().__init__(name, is_supported, version, company, price, weight)
        self.name = 'MacOS'
        self.is_supported = True
        self.version = 'Sonoma'
        self.company = 'Apple Inc.'
        self.price = 49
        self.weight = 42000

class Kali(OperSystem):
    def __init__(self, name, is_supported, version, company, price, weight):
        super().__init__(name, is_supported, version, company, price, weight)
        self.name = 'Kali Linux'
        self.is_supported = False
        self.version = 'NaN'
        self.company = 'OffensiveSecurity'
        self.price = 0
        self.weight = 2700