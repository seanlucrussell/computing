import Entities

class Goblin(Entities.Entity):
    def start(self):
        environment = self.get_message()
        Entities.send_message(environment,"goblin says hi")
    
    def update(self):
        while self.get_message():
            print('new message for goblin!')
        print('goblin updated!')
