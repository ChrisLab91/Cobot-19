#### Ubuntu installation
- python3.6
- `pip install SpeechRecognition`
- `apt-get install portaudio19-dev && sudo pip install pyaudio`
- `pip install pyaudio`
- `pip install git+https://github.com/nateshmbhat/pyttsx3`

#### Windows installation
- python3.6
- `pip install SpeechRecognition`
- `pip install pyaudio`
- `pip install git+https://github.com/nateshmbhat/pyttsx3`

#### Microphone Set-Up
At, the moment the microphone device index (i.e. the number of the relevant audioport) has to be specified manually in voice_input.py

The device index can be found via 
```
import speech_recognition as sr
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name)) 
```

#### Run
`python main.py`
