class PasswordManager():
    
    def __init__(self, keyword = None, username = None, password = None):
        self.keyword = keyword
        self.username = username
        self.password = password
        
        
    def view(self):
        with open("Password.txt", "r") as mainFile:
            for line in mainFile.readlines():
                print(line.rstrip())

    def add(self, info):
        self.keyword = info[0]
        self.username = info[1]
        self.password = info[2]
        with open("Password.txt", "a+") as mainFile:
            mainFile.write(f"\n{self.keyword}: {self.username} | {self.password}")
