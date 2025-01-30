"""
A file that contains all of the user-defined exceptions
"""



class ItemNotFoundError(Exception):
    def __init__(self, item, location, msg=""):
        self.item = item
        self.location = location
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        if self.msg == "":
            return f"{self.item} was not found in {self.location}."
        return f'{self.item}, {self.location} - {self.msg}'