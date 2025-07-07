# TTS Discord Mic 🎙️
 

 Little TTs software i made pretty self explanatory, read the description bellow

---

## 🚀 Features

- 🔥 System tray icon with menu to:  
  - Open the text input popup  
  - Switch between offline (`pyttsx3`) and neural (`Coqui TTS`) speech engines  
  - Exit the application

- ✍️ Minimal, centered popup window to type messages and press Enter to speak aloud

- 🗣️ Support for multiple TTS engines and voice selection (pyttsx3 voices supported, voice menu can be enabled)

- 🎧 (Planned) Route audio output to a virtual microphone (e.g., VB-Cable) for use in apps like Discord, Zoom, etc.

---

## 🛠️ Tech Stack

- [customtkinter](https://github.com/TomSchimansky/CustomTkinter) — modern Tkinter UI for the popup  
- [pyttsx3](https://pyttsx3.readthedocs.io/en/latest/) — offline text-to-speech engine  
- [Coqui TTS](https://github.com/coqui-ai/TTS) — neural TTS models for natural voice synthesis  
- [sounddevice](https://python-sounddevice.readthedocs.io/en/latest/) — audio playback of neural TTS  
- [pystray](https://github.com/moses-palmer/pystray) — system tray icon and menu

---

## 🎧 Routing Audio through VB-Cable (Virtual Mic)

To use your TTS audio as a microphone input in Discord, Zoom, or other voice apps, you can route audio through a virtual audio device like [VB-Audio Cable](https://vb-audio.com/Cable/).

### Steps:

1. **Install VB-Cable** from the official website.

2. **Set your system output device to VB-Cable**:  
   - On Windows, open Sound Settings > Output, select **VB-Audio Virtual Cable** as the output device.  
   - This sends all audio played by your system (including TTS) into the virtual cable.

3. **Set your communication app input to VB-Cable**:  
   - In Discord, Zoom, etc., choose **VB-Audio Virtual Cable** as your microphone/input device.

4. **Optional: Monitor audio** by enabling “Listen to this device” in Windows sound settings or using VB-Cable control panel.

---

## ⚙️ Usage

- Run the application; the system tray icon will appear.

- Click **Open** in the tray menu or press the configured global hotkey (if implemented) to open the text input popup.

- Type your message and press Enter — your text will be spoken aloud.

- Use the tray menu to switch TTS engines or exit the app.

---

## 📝 Acknowledgements

This project leverages the following open-source resources:

- [Coqui TTS](https://github.com/coqui-ai/TTS) — for high-quality neural TTS models  
- [pyttsx3](https://pyttsx3.readthedocs.io/en/latest/) — offline speech synthesis  
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter) — modern UI components for Tkinter  
- [sounddevice](https://python-sounddevice.readthedocs.io/en/latest/) — audio playback backend  
- [pystray](https://github.com/moses-palmer/pystray) — system tray integration  
- [VB-Audio Cable](https://vb-audio.com/Cable/) — virtual audio routing for mic input

---

Feel free to open issues or contribute!

---


