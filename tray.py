from pystray import Icon, Menu, MenuItem
from tts_engine import get_voices,set_voice
from ui import open_popup
import threading
import os
from PIL import Image, ImageDraw

def trayapp():
    iconimg = Image.new(mode="RGB",size=(64,64),)

    draw = ImageDraw.Draw(iconimg)

    draw.rectangle((64 // 2, 0, 64, 64 // 2), fill="black")

    draw.rectangle((0, 64 // 2, 64 // 2, 64), fill="grey")

    def on_exit(icon, item):
        icon.stop()
        os._exit(0)
    def create_items():
        items = []
        voices = get_voices()
        def make_action(voice):
            def on_click(icon, item):
                set_voice(voice)
            return on_click

        for voice in voices:
            items.append(MenuItem(
                voice.name,
                make_action(voice)
            ))
        return items
    icon = Icon('TTSMIC', iconimg, menu=Menu(
        MenuItem('Open', open_popup),
        MenuItem('Voices', Menu(*create_items())),
        MenuItem('Close', on_exit)
    ))


    icon.run()
