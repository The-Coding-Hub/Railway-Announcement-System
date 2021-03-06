# Programme Topic: Making a Railway Announcement system using Python

import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS
import playsound

def textToSpeech(text, filename):
    myText = str(text)
    language = "hi"
    myobj = gTTS(text = myText, lang = language, slow = False)
    myobj.save(filename)

def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    # 1 - Kripya Dhyan Dein
    audio = AudioSegment.from_mp3("railway.mp3")
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3")

    # 2 - from city

    # 3 - se chalkar
    audio = AudioSegment.from_mp3("railway.mp3")
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3")

    # 4 - via city

    # 5 - ke raste
    audio = AudioSegment.from_mp3("railway.mp3")
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3")

    # 6 - to city

    # 7 - ko jane wali gadi sankhya
    audio = AudioSegment.from_mp3("railway.mp3")
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3")

    # 8 - train number and name

    # 9 - kuch hi samay mein platform sankhya
    audio = AudioSegment.from_mp3("railway.mp3")
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3")

    # 10 - platform number

    # 11 - per aa rahi hai
    audio = AudioSegment.from_mp3("railway.mp3")
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3")


def generateAnnouncement(filename):
    df = pd.read_csv(filename)
    print(df)
    for index, item in df.iterrows():
        # 2 - from city
        textToSpeech(item["from"], "2_hindi.mp3")

        # 4 - via city
        textToSpeech(item["via"], "4_hindi.mp3")

        # 6 - to city
        textToSpeech(item["to"], "6_hindi.mp3")

        # 8 - train number and name 
        textToSpeech(item["train_no"] + " " + item["train_name"], "8_hindi.mp3")
          
        # 10 - platform number
        textToSpeech(item["platform"], "10_hindi.mp3")

        audios = [f"{i}_hindi.mp3" for i in range(1, 12)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{index + 1}.mp3", format = "mp3")

if __name__ == "__main__":
    print("Gnerating Skeleton...")
    generateSkeleton()
    print("Now generating announcement...")
    generateAnnouncement("announce_hindi.csv")

# playing mp3 files

trains = int(input("Enter the number of trains which will be going today: "))

for i in range(1, trains + 1):
    playsound.playsound(f"announcement_{i}.mp3", True)