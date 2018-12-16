class Consumer:
    def __init__(self):
        self.hidden_key = ""
        self.hidden_secret = ""

    def get_Key(self):
        return self.hidden_key

    def set_Key(self, input_key):
        self.hidden_key = input_key

    def get_Secret(self):
        return self.hidden_secret

    def set_Secret(self, input_secret):
        self.hidden_secret = input_secret

    Key = property(get_Key, set_Key)
    Secret = property(get_Secret, set_Secret)