import speech_recognition as sr
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

r = sr.Recognizer()

def process_voice_input(voice_input):
    try:
        text_input = r.recognize_google(voice_input, language="de-DE")
        return text_input.lower()
    except AssertionError:
        pass
    except sr.UnknownValueError as e:
         return " "


def query_microphone():
    with sr.Microphone(device_index=1) as source:
        print("Jetzt Sprechen :")
        audio = r.listen(source)
    return audio

def query_user():
    voice_input = query_microphone()
    return process_voice_input(voice_input)