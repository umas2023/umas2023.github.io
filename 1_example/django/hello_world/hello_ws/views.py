from channels.generic.websocket import WebsocketConsumer
class WebsocketTest(WebsocketConsumer):
    '''websocket test'''
    def connect(self):
        self.accept()
    def disconnect(self, close_code):
        pass
    def receive(self, text_data):
        print(text_data)
        for i in range(10):
            self.send(str(i))