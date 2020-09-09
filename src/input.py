import ctypes
import re

import time
from ctypes import wintypes

import win32con

user32 = ctypes.WinDLL('user32', use_last_error=True)

keyboard_summoners_dict = {"flash": [0x46, 0x4C, 0x41, 0x53, 0x48],
                           "teleport": [0x54, 0x45, 0x4C, 0x45, 0x50, 0x4F, 0x52, 0x54],
                           "feu": [0x49, 0x47, 0x4E, 0x49, 0x54, 0x45],
                           "exhaust": [0x45, 0x58, 0x48, 0x41, 0x55, 0x53, 0x54, 0x45]
                           }

keyboard_role_dict = {
    "top": [0x54, 0x4F, 0x50],
    "jungle": [0x4A, 0x55, 0x4E, 0x47, 0x4C, 0x47],
    "mid": [0x4D, 0x49, 0x44],
    "supp": [0x53, 0x55, 0x50, 0x50],
    "adc": [0x41, 0x44, 0x43]

}

keyboard_number_dict = {
    "0": 0x30,
    "1": 0x31,
    "2": 0x32,
    "3": 0x33,
    "4": 0x34,
    "5": 0x35,
    "6": 0x36,
    "7": 0x37,
    "8": 0x38,
    "9": 0x39,
}

cooldown_summoner = {
    "flash": 500,
    "exhaust": 210,
    "ignite": 180,
    "teleport": 240,
}


# def history():

def assemble_timer(summ, voice_command):
    timer_raw = re.sub("[^0-9]", "", str(voice_command))
    print("timer raw", timer_raw)
    timer_raw = str(int(timer_raw) + cooldown_summoner[summ])
    timer_sentence = []
    print("timer raw", timer_raw)
    for t in timer_raw:
        print(t)
        if keyboard_number_dict[t]:
            timer_sentence.append(keyboard_number_dict[t])
    return timer_sentence


def assemble_sentence(summoners, role, timer):  # <Summoner Spell> <Role> <Timer>
    summoner_input_code = keyboard_summoners_dict[summoners]
    role_input_code = keyboard_role_dict[role]
    space_input = [0x20]
    sentence = summoner_input_code + space_input + role_input_code + space_input + timer
    return sentence


def write_word(sentence):
    user32.keybd_event(0x0D, 0, 2, 0)
    user32.keybd_event(0x0D, 0, 0, 0)
    for input in sentence:
        user32.keybd_event(input, 0, 2, 0)
        user32.keybd_event(input, 0, 0, 0)
    time.sleep(0.20)
    user32.keybd_event(0x0D, 0, 2, 0)
    user32.keybd_event(0x0D, 0, 0, 0)
