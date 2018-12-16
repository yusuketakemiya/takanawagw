
from twitter import *
from . import Consumer

class Oauth:
    def __init__(self):
        self.hidden_token = None
        self.hidden_secret = None
        self.hidden_url = None

    def get_Token(self):
        return self.hidden_token

    def set_Token(self, input_token):
        self.hidden_token = input_token
        self.hidden_url = ('https://api.twitter.com/oauth/authorize?oauth_token=' +
            self.hidden_token)

    def get_Secret(self):
        return self.hidden_secret

    def set_Secret(self, input_secret):
        self.hidden_secret = input_secret

    def get_Url(self):
        return self.hidden_url

    def set_Url(self, input_url):
        self.hidden_url = input_url

    Token = property(get_Token, set_Token)
    Secret = property(get_Secret, set_Secret)
    Url = property(get_Url, set_Url)


    def Fill(self, result):
        for r in result.split('&'):
            k, v = r.split('=')
            if k == 'oauth_token':
                self.set_Token(v)
            elif k == 'oauth_token_secret':
                self.set_Secret(v)
    
    def Load(self, consumer :Consumer):
        if self.get_Token() is None:
            token, scret = oauth_dance("TweetStamp", 
                consumer.Key, 
                consumer.Secret,
                open_browser=False)
            self.set_Secret(scret)
            self.set_Token(token)
