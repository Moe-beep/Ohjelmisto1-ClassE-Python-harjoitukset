class Player:
    def __init__(self,name,location):
        self.name = name
        self.items = []
        self.location = location

    def move(self, new_location):
        self.location = new_location

    def collect_item(self, item):
        self.items.append(item)