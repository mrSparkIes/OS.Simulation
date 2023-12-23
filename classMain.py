true = True
false = False

class RootApp():
    def __init__(self,fullPermission=true):
        self.fullPermission = fullPermission

class OSManager(RootApp):
    def __init__(self, fullPermission=true):
        super().__init__(fullPermission)

class App():
    def __init__(self, weight, type, wifi_required, support_all, fullPermission=false):
        self.weight = weight
        self.type = type
        self.wifi_required = wifi_required
        self.support_all = support_all
        self.fullPermission = fullPermission

class Discord(App):
    def __init__(self, weight, type, wifi_required, support_all, fullPermission=false):
        super().__init__(weight, type, wifi_required, support_all, fullPermission)
        self.weight = 76
        self.type = 'Chatting'
        self.wifi_required = true
        self.support_all = true

class Roblox(App):
    def __init__(self, weight, type, wifi_required, support_all, fullPermission=false):
        super().__init__(weight, type, wifi_required, support_all, fullPermission)
        self.weight = 159
        self.type = 'Platform'
        self.wifi_required = true
        self.support_all = false

class Chrome(App):
    def __init__(self, weight, type, wifi_required, support_all, fullPermission=false):
        super.__init__(weight,type,wifi_required,support_all, fullPermission)
        self.weight = 36
        self.type = 'Browser'
        self.wifi_required = true
        self.support_all = true

class Twitter(App):
    def __init__(self, weight, type, wifi_required, support_all, fullPermission=false):
        super().__init__(weight, type, wifi_required, support_all, fullPermission)
        self.weight = 85
        self.type = 'ToxicShit'
        self.wifi_required = true
        self.support_all = true
