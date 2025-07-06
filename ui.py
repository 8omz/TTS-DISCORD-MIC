# screen_width and height, then calculate x and y to center
import customtkinter as ctk

class TTSpopup(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        # constants for screen width and height
        SWIDTH = self.winfo_screenwidth()
        SHEIGHT = self.winfo_screenheight()
        # and window width and height
        WINWIDTH = 700
        WINHEIGHT = 80
        x = (SWIDTH - WINWIDTH) //2
        y = (SHEIGHT - WINHEIGHT) //4
        
        self.overrideredirect(True)
        
        # Set the geometry of the window
        # to center it on the screen
        self.geometry(f"{WINWIDTH}x{WINHEIGHT}+{x}+{y}")
        self.config(bg="black")
        self.attributes("-transparentcolor", "black")
        
        # Create a custom entry widget
        self.entry = ctk.CTkEntry(self, placeholder_text="Input your message...",width=700,height=80)
        self.entry.pack(padx= 10, pady = 10)
        self.after(100, self._force_focus)
        
        # returns string written in the Entry
       
        self.entry.bind("<Return>",self.on_enter)

    #no clue what this does 
    def _force_focus(self):
        self.lift()               
        self.entry.focus_force()  
     
    def on_enter(self,event):
        string = self.entry.get()
        print(string)
        self.destroy()
        return string
def open() :  
    app = TTSpopup()       
    app.mainloop()