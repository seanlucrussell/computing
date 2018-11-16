import Entities
import GoblinEntity

class Environment(Entities.Entity):
    def start(self):
        goblin = Entities.create_entity(GoblinEntity.Goblin)
        Entities.send_message(goblin,self)
    
    def update(self):
        while self.get_message():
            print('new message for environment!')
        print('environment updated!')

