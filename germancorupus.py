import tweepy
import csv #Import csv


class Listener(tweepy.StreamListener):
    def on_status(self, status):
        csvFile = open('berlintweets.csv', 'ab')
        csvWriter = csv.writer(csvFile)
    
        user = status.author.screen_name.encode("utf-8", 'backslashreplace')
        #user = unicode(status.author.screen_name)
        tweet = status.text.encode("utf-8", 'backslashreplace')
        #tweet = unicode(status.text)
        coords = status.coordinates
        #coords = unicode(status.coordinates)
        locale = status.source
        #locale = unicode(status.source)
        try:
            csvWriter.writerow([user,tweet,coords,locale])
            print "screen_name='%s' tweet='%s'"%(status.author.screen_name, status.text)
            csvFile.close()

        except Exception:
            csvFile.close()
            return True
def login():
    auth = tweepy.OAuthHandler('var1', 'var2')
    auth.set_access_token('var1', 'var2')
    return auth
try:
    auth = login()
    streaming_api = tweepy.streaming.Stream(auth, Listener(), timeout=60)
    # Berlin Germany
    streaming_api.filter(follow=None, locations=[12.952881,52.331982,13.94165,52.739618]) 
except KeyboardInterrupt:
    print "got keyboardinterrupt"
