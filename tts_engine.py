import pyttsx3 as tts
engine = tts.init()

def get_voices():
    return engine.getProperty("voices")
def set_voice(voice):
    engine.setProperty('voice',voice.id)
