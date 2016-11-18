import PIL, os, time
from PIL import Image, ImageDraw, ImageFont
from random import randint

newlineCharacters = 25
randomPhrases =[
    "balkanska w zylach plynie krew, kobiety wino taniec spiew, zasady proste w zyciu mam, nie rob drugiemu tego, czego ty nie chcesz sam !!",
    "muzyka, przyjazn radosc, smiech, zycie latwiejsze staje sie przyniescie dla mnie wina dzban, potem ruszamy razem w tan !!",
    "bedzie bedzie zabawa! Bedzie sie dzialo, I znowu nocy bdzie malo bedzie glosno, bedzie radosnie znow przetanczymy razem cala noc !!",
    "orkiestra nie oszczedza sil, juz troche im brakuje tchu, polejcie wina rowniez im znow na parkiecie bedzie dym!! !",
    "balkanskie rytmy polska moc , znow przetanczymy cala noc.. i jeszcze jeden, malutki wina dzban potem ruszymy razem w tan !!"
    
]
saveLocation = 'result.jpg'
frame = input('frame: ')

def convertToFit(phrase):
    for counter, char in enumerate(phrase):
        if counter % newlineCharacters == 0 and counter != 0:
            phrase = phrase[:counter] + "\n" + phrase[counter:]
    return phrase

def makeImage():
    img=Image.open(frame)
    phrase = randomPhrases[randint(0, len(randomPhrases)-1)]
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("segoesc.ttf", 25)
    draw.text((150,10), convertToFit(phrase), font=font, fill=(0,0,0,0))

    img.save(saveLocation)
makeImage()
