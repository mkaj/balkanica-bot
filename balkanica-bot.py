import PIL, os
from PIL import Image, ImageDraw, ImageFont
from random import randint

newlineCharacters = 25
saveLocation = 'result.jpg'
phrasesFileName = 'balkanica.txt'
res = (560,300)
legoManRes = (165,300)

def getAllImagesInDirectory():
    fileList = []
    for dirpath, dirnames, filenames in os.walk('.'):
        for filename in [f for f in filenames if f.endswith('.jpg') or f.endswith('.png')]:
            fileList.append(filename)
    return fileList

def getContentsOfFile(filename):
    with open(filename) as file:
        content = file.read().splitlines()
    return content

def getPhrase():
    contents = getContentsOfFile(phrasesFileName)
    return contents[randint(0,len(contents)-1)]

def getRandomMan(fileList):
    filename = fileList[randint(0,len(fileList)-1)]
    result = Image.open(filename)
    return result

def pasteMan():
    blankImage = Image.new('RGB',res,'white')
    legoMan = getRandomMan(getAllImagesInDirectory())
    legoMan = legoMan.resize(legoManRes)
    blankImage.paste(legoMan,(0,0,legoManRes[0],legoManRes[1]))
    return blankImage

def convertToFit(phrase):
    for counter, char in enumerate(phrase):
        if counter % newlineCharacters == 0 and counter != 0:
            phrase = phrase[:counter] + "\n" + phrase[counter:]
    return phrase

def makeImage():
    img = pasteMan()
    phrase = getPhrase()
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("segoesc.ttf", 25)
    draw.text((150,10), convertToFit(phrase), font=font, fill=(0,0,0,0))
                    
    img.save(saveLocation)

                    
makeImage()
