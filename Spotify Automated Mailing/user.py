from decouple import config

class User:
    def __init__(self):
        self.EMAIL_ADDRESS = config("EMAIL_ADDRESS")
        self.EMAIL_PASSWORD = config("EMAIL_PASSWORD")
        self.receiver_list = config("TO")
 
    def getDetail(self):
        return self.EMAIL_ADDRESS, self.EMAIL_PASSWORD
    
    def getList(self):
        return self.receiver_list