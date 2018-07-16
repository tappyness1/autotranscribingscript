import os
os.chdir('C:\\Users\\neoce\\Downloads')
wavfilename = 'Taste test McDonalds Ha Ha Cheong Gai menu  CNA Lifestyle.wav'

# for the next few lines, we use the soundfile package. 
# if dont have, just do pip install soundfile
# the number of seconds looks to be the est so far

import soundfile as sf
f = sf.SoundFile(wavfilename)
print('samples = {}'.format(len(f)))
print('sample rate = {}'.format(f.samplerate))
print('seconds = {}'.format(len(f) / f.samplerate))
seconds = int(float(format(len(f) / f.samplerate)))

# speech recognition!
# if don't have package - pip install SpeechRecognition
import speech_recognition as sr
r = sr.Recognizer()
aud = sr.AudioFile(wavfilename)
with aud as source:
    audio = r.record(source, offset = 4,duration = 19)
# build a dictionary to spread out the audiofile time

auddict = {}
counter = 1
offsetcounter = 0
timing = 10
audtime = 0
#build a loop to get a dict filled with duration files
while seconds > 0:
    audioname = 'audio' + str(counter)
    audtime += timing 
    m, s = divmod(audtime, 60)
    h, m = divmod(m, 60)
    totalaudtime = "%02d:%02d:%02d" % (h, m, s)
    with aud as source:
        auddict[audioname] = (r.record(source, offset = offsetcounter, duration = timing), totalaudtime)
    counter += 1
    offsetcounter += timing
    seconds -= timing
    
for key, value in auddict.items():
    try:
        print ("(" + auddict[key][1]+")")
        print(r.recognize_google(auddict[key][0]))
    except sr.UnknownValueError:
        print ("We have UnknownValueError")
        pass
        # seems like such an error gets thrown up when there is no speech at all
        
