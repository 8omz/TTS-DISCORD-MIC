import keyboard as kb
from ui import open_popup
from tray import trayapp

kb.add_hotkey("ctrl+space", open_popup)

trayapp()  


kb.wait()

