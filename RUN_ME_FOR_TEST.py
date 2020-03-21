from voice_input import process_voice_input
from voice_output import process_voice_output
from brain import find_answer

if __name__=="__main__":
    voice_input = "will einkaufen"
    text_input = process_voice_input(voice_input)
    text_output = find_answer(voice_input)
    voice_output = process_voice_output(text_output)
    print(voice_output)