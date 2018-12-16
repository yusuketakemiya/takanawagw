import os
from models.Consumer import Consumer
from models.Oauth import Oauth
from twitter import *

class TwitterService:
    def __init__(self, consumer :Consumer, oauth :Oauth):
        self.Consumer = consumer
        self.Oauth = oauth

    def get_twitter(self):
        return self.hidden_twitter
    def set_twitter(self, settwitter):
        self.hidden_twitter = settwitter

    twitter = property(get_twitter, set_twitter)

    def oauth(self):
        print("oauth call")
        twitter = Twitter(
            auth = OAuth('', '', self.Consumer.Key, self.Consumer.Secret),
            format='', api_version=None)
        request = twitter.oauth.request_token()
        self.Oauth.Fill(request)
        return self.Oauth

    def oauth_verifier(self, oauth_verifier):
        twitter = Twitter(
            auth=OAuth(
                self.Oauth.Token,
                self.Oauth.Secret,
                self.Consumer.Key,
                self.Consumer.Secret),
            format='',
            api_version=None)
        request = twitter.oauth.access_token(oauth_verifier=oauth_verifier)
        self.Oauth.Fill(request)
    
    def home_alltimeline(self):
        tweets = self.twitter.statuses.home_timeline()
        self.__wrighttweet(tweets)
    
    def home_timeline(self, count):
        tweets = self.twitter.statuses.home_timeline(count=count)
        self.__wrighttweet(tweets)

    def user_timeline(self, screen_name):
        tweets = self.twitter.statuses.user_timeline(screen_name=screen_name)
        self.__wrighttweet(tweets)
    
    def __wrighttweet(self,tweets):
        for tweet in tweets:
            print(tweet['user']['name']+'::'+tweet['text'])
            print(tweet['created_at'])
            print('----------------------------------------------------')

    def oembed(self, _id):
        oembedtweet = self.twitter.statuses.oembed(_id=_id)
        print(oembedtweet)

    def tweet(self, status):
        self.twitter.statuses.update(
            status=status)
    
    def sendmessage(self, touser, message):
        self.twitter.direct_messages.new(
            user=touser,
            text=message)

    def listsmembers(self, owner_screen_name, slug):
        lists = self.twitter.lists.members(
            owner_screen_name=owner_screen_name, 
            slug=slug)
        print(lists)

    def imageupload(self, message, imagelist):
        t_upload = Twitter(domain='upload.twitter.com',
            auth=OAuth(
                self.Oauth.Token, 
                self.Oauth.Secret, 
                self.Consumer.Key, 
                self.Consumer.Secret))
        id_imgs = []
        for imagedata in imagelist:
            id_imgs.append(
                t_upload.media.upload(media=imagedata)["media_id_string"])
        
        self.twitter.statuses.update(status=message, media_ids=",".join(id_imgs))

# twitter = ManageTwitter()
# print("twitter.load()")
# twitter.load()
# print("OAUTH_TOKEN:" + twitter.OAUTH_TOKEN)
# print("OAUTH_SECRET:" + twitter.OAUTH_SECRET)
# twitter.oauth()
# # twitter.home_alltimeline()
# # twitter.home_timeline(5)
# # twitter.user_timeline(screen_name="billybob")
# # twitter.oembed(_id=1234567890)
# # twitter.tweet("テストです!!")
# # twitter.sendmessage("tomosuke13b", "テストです!!")
# # twitter.listsmembers("tamtar","things-that-are-rad")
# # twitter.users() # 不完全

# # 画像テストここから
# with open("C:\\Users\\tomosuke\\Desktop\\yama.jpg", "rb") as imagefile:
#     imagedata = imagefile.read()

# imagelist = []
# imagelist.append(imagedata)
# imagelist.append(imagedata)
# twitter.imageupload("画像テスト", imagelist)
# # 画像テストここまで