from voice_input import process_voice_input, query_microphone
from voice_output import process_voice_output
from brain import find_answer

if __name__=="__main__":
    voice_input = query_microphone()
    text_input = process_voice_input(voice_input)
    print("Sie sagten: {}".format(text_input))
    text_output = find_answer(text_input)
    voice_output = process_voice_output(text_output)