import tkinter as tk 
from tkinter import ttk
from tkinter.messagebox import showinfo
import datetime 
import  constants
import winsound
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




def bar(progress, s):
    
    if glob.stop_flag:
        progress['value'] = glob.progressbar
        glob.progressbar += 1
        if progress['value'] != s:
            glob.root.after(1000, lambda: bar(progress, s))
        else:
            winsound.Beep(1000, 1000)
            glob.stop_flag = False
    elif s == 0 and not glob.stop_flag:
        progress.stop()
        glob.root.after(1000, lambda: bar(progress, s))
    elif s == 0 and glob.stop_flag:
        progress.start()
        glob.root.after(1000, lambda: bar(progress, s))
    else:
        glob.root.after(1000, lambda: bar(progress, s))

        


    
def start_progressbar(hrs, mins):
    
    thrs = hrs.get()
    tmins = mins.get()
    seconds = int(glob.session_timer.total_seconds())
    time_left_h = int(thrs) 
    time_left_s = int(tmins) 
    seconds_of_timer = time_left_h * 3600 + time_left_s * 60
    progress = ttk.Progressbar(glob.pages['session'], mode= 'indeterminate', orient= 'horizontal')
    if seconds_of_timer != 0:
        progress.configure(mode ='determinate', maximum= seconds_of_timer)
        bar(progress, seconds_of_timer)
        
    else: 
        progress.start()

    progress.grid(row= 1, column= 2)
    


def stop_timer_pressed():
    
    
    if not glob.stop_flag:
        glob.stop_flag = True
        
    else: 
        glob.stop_flag = False
    

def start_session_pressed(hrs, mins):
    
    
    timer_label = ttk.Label(glob.pages['session'], text= glob.session_timer)
    timer_label.grid(row= 1, column= 1, sticky= tk.N)
    timer_label.after(1000, lambda: session_func.update_time( timer_label))
    start_btn_frame = tk.Frame(glob.pages['session'])
    start_btn_frame.grid(row= 0, column= 0 , sticky= tk.NSEW)
    stop_time_button = ttk.Button(start_btn_frame, text= 'Pause Session', command= stop_timer_pressed)
    stop_time_button.grid(row= 0, column= 0, sticky= tk.NSEW)
    #stop_time_button.pack() pack is an option if i have already made a frame
    start_btn_frame.tkraise()
    start_progressbar(hrs, mins)
    
    


def upload_session():
    pass


def show_pages(page_name):
    
    glob.pages[page_name].tkraise() 

def create_pages():
    
    for name in ('session', 'home'):
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

    
    ttk.Button(glob.pages['session'], text = 'start session', command= lambda: start_session_pressed(timer_entry_hour, timer_entry_minutes)).grid(row= 0, column= 0, sticky= tk.NSEW)
    ttk.Button(glob.pages["session"],text="Back",command=lambda: show_pages("home")).grid(row= 3, column= 0, sticky= tk.NSEW)
    ttk.Button(glob.pages['session'], text='Upload session', command=upload_session).grid(row=3, column=3, sticky= tk.NSEW)
    ttk.Button(glob.pages['home'], text= 'Start a session', command= lambda: show_pages('session')).grid(row=3, column=0, sticky= tk.NSEW)
    

if __name__ == '__main__':
    
    root_setup()
    create_pages()
    setup_app()
    glob.root.mainloop()
    