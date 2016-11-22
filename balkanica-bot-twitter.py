import PIL, tweepy, os, time
from PIL import Image, ImageDraw, ImageFont
from random import randint

newlineCharacters = 25
phrasesFileName = 'balkanica.txt'
res = (560,300)
legoManRes = (165,300)
statusList = ['kobiety wino taniec spiew', 'czego ty nie chcesz sam', 'bedzie sie dzialo']
saveLocation = 'post.jpg'


# loads images in directory
def getAllImagesInDirectory():
    fileList = []
    for dirpath, dirnames, filenames in os.walk('.'):
        for filename in [f for f in filenames \
                         if f.endswith('.jpg') \
                         or f.endswith('.png')]:
            fileList.append(filename)
    return fileList

# gets contents of file
def getContentsOfFile(filename):
    with open(filename) as file:
        content = file.read().splitlines()
    return content

# takes random line from phrasesFileName
def getPhrase():
    contents = getContentsOfFile(phrasesFileName)
    return contents[randint(0,len(contents)-1)]

# randomly chooses lego man image
def getRandomMan(fileList):
    filename = fileList[randint(0,len(fileList)-1)]
    result = Image.open(filename)
    return result

# places lego man on the left side of the blank image
def pasteMan():
    blankImage = Image.new('RGB',res,'white')
    legoMan = getRandomMan(getAllImagesInDirectory())
    legoMan = legoMan.resize(legoManRes)
    blankImage.paste(legoMan,(0,0,legoManRes[0],legoManRes[1]))
    return blankImage

# crappy text wrap function
# TODO: stop splitting words
def convertToFit(phrase):
    for counter, char in enumerate(phrase):
        if counter % newlineCharacters == 0 and counter != 0:
            phrase = phrase[:counter] + '\n' + phrase[counter:]
    return phrase

# draws text on image
def makeImage():
    img = pasteMan()
    phrase = getPhrase()
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("segoesc.ttf", 25)
    draw.text((150,10), convertToFit(phrase), font=font, fill=(0,0,0,0))
    img.save(saveLocation)

# uploads the image to twitter with a random status from statusList
# fill up manually CONSUMER_KEY, CONSUMER_SECRET etc.
def uploadImage():
    status = statusList[randint(0,len(statusList)-1)]

    imageLocation = 'post.jpg'
    CONSUMER_KEY = 'key'
    CONSUMER_SECRET = 'secret'
    ACCESS_KEY = 'token'
    ACCESS_SECRET = 'secret'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.secure = True
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    fn = os.path.abspath(imageLocation)
    api.update_with_media(fn, status=status)

if __name__ == '__main__':
    makeImage()
    uploadImage()
