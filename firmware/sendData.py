class SendData:
    def __init__(self, data):
        self.data = data

    def send(self):
        print(f"Sending data: {self.data}")
        return True