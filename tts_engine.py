import pyttsx3 as tts
from pyttsx3 import speak as pytts_speak
import sounddevice as sd
from TTS.api import TTS
import torch
import numpy as np

use_gpu = torch.cuda.is_available()
engine = tts.init()

# Default mode
tts_mode = "pyttsx3"

# Coqui instance
#coqui_tts = TTS(model_name="tts_models/en/ljspeech/speedy-speech")
#coqui_tts.to("cuda" if torch.cuda.is_available() else "cpu")
#coqui_tts = TTS(model_name="tts_models/en/ljspeech/fast_pitch")

coqui_tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")



def set_tts_mode(mode):
    global tts_mode
    tts_mode = mode

def speak(text):
    if tts_mode == "pyttsx3":
        pytts_speak(text)
    elif tts_mode == "coqui":
        volume = 1.8
        audio = coqui_tts.tts(text) 
        audio = np.array(audio)  # convert to numpy array
        audio = audio * volume   # multiply by float volume
        audio = np.clip(audio, -1.0, 1.0)  # avoid clipping
        sd.play(audio, samplerate=coqui_tts.synthesizer.output_sample_rate)
        sd.wait()
def get_voices():
    return engine.getProperty("voices")
def set_voice(voice):
    engine.setProperty('voice',voice.id)

