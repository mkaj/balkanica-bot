import tweepy
from balkanicagenerator import *

saveLocation = 'result.jpg'

def saveImage():
    img = pasteMan()
    phrase = getPhrase()
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("segoesc.ttf", 25)
    draw.text((150,10), convertToFit(phrase), font=font, fill=(0,0,0,0))
    
    img.save(saveLocation)

# uploads the image to twitter with a random status from text file
# fill up manually CONSUMER_KEY, CONSUMER_SECRET etc.
def uploadImage():
    status = getPhrase()

    CONSUMER_KEY = 'key'
    CONSUMER_SECRET = 'secret'
    ACCESS_KEY = 'token'
    ACCESS_SECRET = 'secret'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.secure = True
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    fn = os.path.abspath(saveLocation)
    api.update_with_media(fn, status=status)

def deleteImage():
    os.remove(saveLocation)

if __name__ == '__main__':
    saveImage()
    uploadImage()
    deleteImage()
