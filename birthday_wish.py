from gtts import gTTS # pip install gtts
import playsound # pip install playsound
import os

with open('lang.txt',encoding='utf8') as f:
    index = -2
    lang_list = f.readline().split(',')
    # try:
    for item in range(len(lang_list)//2):
        file_name = str("output" + str(item) + ".mp3")
        obj = gTTS(text=lang_list[index+2],lang=lang_list[index+3],slow=False) #0,1 -- 2,3 -- 4,5
        obj.save(file_name)
        playsound.playsound(file_name)
        os.remove(file_name)
        index +=2
    print('Bye...Bye...')