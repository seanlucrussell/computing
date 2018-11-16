import time

def create_entity(type):
    new_entity = type()
    new_entity.begin = True
    entities.append(new_entity)
    return new_entity

def send_message(entity,message):
    if not entity in entities:
        return
    message_queue.append((entity,message))

class Entity():
    def __init__(self):
        self.messages = []
    def get_message(self):
        return self.messages.pop() if len(self.messages) != 0 else None

entities = []
message_queue = []
    
def main_loop():
    global message_queue
    while True:
        for entity in entities:
            print('updating',entity)
            if entity.begin == True:
                entity.start()
                entity.begin = False
            entity.update()
        time.sleep(.5)
        for message in message_queue:
            message[0].messages.append(message[1])
        message_queue = []
