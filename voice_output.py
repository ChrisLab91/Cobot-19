import pyttsx3
engine = pyttsx3.init()
engine.setProperty('voice', "german")

# voices = engine.getProperty('voices')
# for voice in voices:
#     print("Voice: %s" % voice.name)
#     print(" - ID: %s" % voice.id)
#     print(" - Languages: %s" % voice.languages)
#     print(" - Gender: %s" % voice.gender)
#     print(" - Age: %s" % voice.age)
#     print("\n")
#
# exit()

def process_voice_output(text_output):
    engine.say(text_output)
    engine.runAndWait()
    return
