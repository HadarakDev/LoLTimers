from src.input import assemble_sentence, assemble_timer, write_word
from src.speech import detect_voice_command, get_most_similar_summoner, get_most_similar_role
from playsound import playsound

if __name__ == '__main__':

    voice_command = detect_voice_command()
    splitted_command = voice_command.split(" ")
    if len(splitted_command) < 3:
        exit()
    summ = get_most_similar_summoner(splitted_command[0])
    role = get_most_similar_role(splitted_command[1])


    timer_sentence = assemble_timer(summ, splitted_command[2:])
    sentence = assemble_sentence(summ, role, timer_sentence)
    write_word(sentence)


