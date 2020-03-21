import speech_recognition as sr


r = sr.Recognizer()

def process_voice_input(voice_input):
    try:
        text_input = r.recognize_google(voice_input, language="de-DE")
        return text_input
    except AssertionError:
        pass
    except sr.UnknownValueError as e:
         return " "
    return text_input


def query_microphone():
    with sr.Microphone(device_index=6) as source:
        print("Speak Anything :")
        audio = r.listen(source)
    return audio
