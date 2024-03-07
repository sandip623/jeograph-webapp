class AzureDBconfig:
    def __init__(self):
        self.config = {
            "server" : "<overwrite>.database.windows.net",
            "database" : "<overwrite>",
            "username" : "<overwrite>",
            "password" : "<overwrite>",
            "driver" : "<overwrite>"
        }

    def getconfig(self) -> dict:
        return self.config