from PIL import Image
import string
import sys
import speech_recognition as sr
from typing import Dict, List
letter_to_img = {}
alpha = list(string.ascii_lowercase)
for i in alpha:
    letter_to_img[i] = '/Users/nithilanpugal/PycharmProjects/Speachto/venv/Signs/{}.jpg'.format(i.upper())


def word_to_image(sentence: str):

    wordtoimg = {}
    for word in sentence.split():
        list_im = []
        for ch in word:
            list_im.append(letter_to_img[ch])
            print(list_im)
        images = [Image.open(x) for x in list_im]
        widths, heights = zip(*(i.size for i in images))

        total_width = sum(widths)
        max_height = max(heights)

        new_im = Image.new('RGB', (total_width, max_height))

        x_offset = 0
        for im in images:
            new_im.paste(im, (x_offset,0))
            x_offset += im.size[0]
        wordtoimg[word] = new_im
        new_im.save('test.jpg')

    return wordtoimg


def voice_to_words(filename: str) -> str:
    r = sr.Recognizer()

    file_audio = sr.AudioFile(filename)

    with file_audio as source:
        audio_text = r.record(source)

    print(type(audio_text))
    return (r.recognize_google(audio_text))


def captions(fulltext: str):
    w2i = word_to_image(fulltext)
    images = list(w2i[i] for i in w2i)
    widths, heights = zip(*(i.size for i in images))
    sum_width = sum(widths) + 32*len(w2i)

    max_height = max(heights)

    new_im = Image.new('RGB', (sum_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset,0))
        x_offset += (im.size[0]+32)

    new_im.save('test.jpg')
    return new_im

captions('my name is nithilan')
#words = word_to_image(voice_to_words('2try.wav'))

#for key in words:
#    words[key].save('test{}.jpg'.format(key))
