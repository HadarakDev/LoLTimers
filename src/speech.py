import speech_recognition as sr
from time import *
from fuzzywuzzy import fuzz
from playsound import playsound


def detect_voice_command():
    voice_command = "No Audio"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak")
        try:
            playsound("C:\\Users\\nico_\\Documents\\Project\\LoLTimers\\dist\\bip.wav")
            sleep(0.25)
            audio = r.listen(source, 1, 3)
            voice_command = r.recognize_google(audio, language='fr-FR')
            print("You said " + voice_command)
        except Exception:
            print("No Audio detected")
        return voice_command


def get_most_similar_summoner(text):
    ratios_summoners = []
    match_summoners = {0: "flash",
                       1: "teleport",
                       2: "exhaust",
                       3: "fire"}

    ratios_summoners.append(fuzz.token_set_ratio(text, "flash"))
    ratios_summoners.append(fuzz.token_set_ratio(text, "teleport"))
    ratios_summoners.append(fuzz.token_set_ratio(text, "fatique"))
    ratios_summoners.append(fuzz.token_set_ratio(text, "feu"))

    summoners = ratios_summoners.index(max(ratios_summoners))
    print(match_summoners[summoners])
    return match_summoners[summoners]

def get_most_similar_role(text):
    ratios_role = []
    match_role = {0: "top",
                  1: "jungle",
                  2: "mid",
                  3: "adc",
                  4: "supp"}

    ratios_role.append(fuzz.token_set_ratio(text, "top"))
    ratios_role.append(fuzz.token_set_ratio(text, "jungle"))
    ratios_role.append(fuzz.token_set_ratio(text, "mid"))
    ratios_role.append(fuzz.token_set_ratio(text, "adc"))
    ratios_role.append(fuzz.token_set_ratio(text, "supp"))

    role = ratios_role.index(max(ratios_role))
    print(match_role[role])
    return match_role[role]
