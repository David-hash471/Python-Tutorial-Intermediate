import tkinter as tk 
from tkinter import ttk
import  constants
import globals as glob
import session_func







def root_setup():
    
    glob.root.title("STUDY TRACKER")
    window_width = 400
    window_height = 250
    screen_width = glob.root.winfo_screenwidth() 
    screen_height = glob.root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    glob.root.resizable(False, False)
    glob.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    glob.root.iconbitmap(r'C:\Users\david\OneDrive\Documents\Personal\David\Projects\Python projects\Python Tutorial\Python-Tutorial-Intermediate\TASK 01 FOR LESSON 01-10\Assets\book_3725.ico')
    for i in range(3):
        glob.root.rowconfigure(i, weight= 1)
        glob.root.columnconfigure(i, weight= 1)


def upload_session():
    pass


def show_pages(page_name):
    glob.pages[page_name].tkraise() 

def create_pages():
    for name in ('session', 'home' ):
        page = tk.Frame(glob.root)
        page.grid(row = 1, column=0, sticky= tk.NSEW)
        glob.pages[name] = page
        for i in range(4):
            glob.pages[name].rowconfigure(i, weight= 1)
            glob.pages[name].columnconfigure(i, weight= 1)



def setup_app():
    ttk.Label(glob.pages['home'], text='Study Tracker').grid(row=0, column=0, sticky= tk.NSEW)
    ttk.Label(glob.pages["session"], text="Study session").grid(row= 0, column= 0, sticky= tk.NSEW)
    
    timer_entry_hour = ttk.Combobox(glob.pages['session'], values =constants.combobox_hours)
    timer_entry_minutes = ttk.Combobox(glob.pages['session'], values =constants.combobox_minutes)
    timer_entry_hour.set('0')
    timer_entry_minutes.set('00')
    timer_entry_hour.grid(row= 0, column= 1)
    timer_entry_minutes.grid(row= 0, column= 2)

    ttk.Button(glob.pages['session'], text = 'start session', command= lambda: session_func.start_session_pressed(timer_entry_hour, timer_entry_minutes)).grid(row= 0, column= 0, sticky= tk.NSEW)
    ttk.Button(glob.pages["session"],text="Back",command=lambda: show_pages("home")).grid(row= 3, column= 0, sticky= tk.NSEW)
    ttk.Button(glob.pages['session'], text='Upload session', command=upload_session).grid(row=3, column=3, sticky= tk.NSEW)
    ttk.Button(glob.pages['home'], text= 'Start a session', command= lambda: show_pages('session')).grid(row=3, column=0, sticky= tk.NSEW)
    

if __name__ == '__main__':
    
    root_setup()
    create_pages()
    setup_app()
    glob.root.mainloop()
    