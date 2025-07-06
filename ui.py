# screen_width and height, then calculate x and y to center
import customtkinter as ctk

class TTSpopup(ctk.CTk):
    def __init__(self):
        super().__init__()
        SWIDTH = self.winfo_screenwidth()
        SHEIGHT = self.winfo_screenheight()
        WINWIDTH = 400
        WINHEIGHT = 80
        
        self.overrideredirect(True)
        
        x = (SWIDTH - WINWIDTH) //2
        y = (SHEIGHT - WINHEIGHT) //2
        
        self.geometry(f"{WINWIDTH}x{WINHEIGHT}+{x}+{y}")