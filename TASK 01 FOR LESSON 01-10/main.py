import tkinter as tk 
from tkinter import ttk
from tkinter.messagebox import showinfo
import datetime 
import  constants
import winsound


root = tk.Tk()
session_timer = datetime.timedelta()
stop_flag = True
progressbar =0
pages = {}






def root_setup():
    global root
    root.title("STUDY TRACKER")
    window_width = 400
    window_height = 250
    screen_width = root.winfo_screenwidth() 
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    root.resizable(False, False)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    root.iconbitmap(r'C:\Users\david\OneDrive\Documents\Personal\David\Projects\Python projects\Python Tutorial\Python-Tutorial-Intermediate\TASK 01 FOR LESSON 01-10\Assets\book_3725.ico')
    for i in range(3):
        root.rowconfigure(i, weight= 1)
        root.columnconfigure(i, weight= 1)

def update_time(label):
    global stop_flag, session_timer
    if stop_flag:
        session_timer += datetime.timedelta(seconds = 1)
    else:
        time_at_stop(session_timer)
    label.configure(text = session_timer) 
    label.after(999, lambda: update_time(label))


def bar(progress, s):
    global  progressbar, stop_flag
    if stop_flag:
        progress['value'] = progressbar
        progressbar += 1
        if progress['value'] != s:
            root.after(1000, lambda: bar(progress, s))
        else:
            winsound.Beep(1000, 1000)
            stop_flag = False
    elif s == 0 and not stop_flag:
        progress.stop()
        root.after(1000, lambda: bar(progress, s))
    elif s == 0 and stop_flag:
        progress.start()
        root.after(1000, lambda: bar(progress, s))
    else:
        root.after(1000, lambda: bar(progress, s))

        


    
def start_progressbar(hrs, mins):
    
    thrs = hrs.get()
    tmins = mins.get()
    seconds = int(session_timer.total_seconds())
    time_left_h = int(thrs) 
    time_left_s = int(tmins) 
    seconds_of_timer = time_left_h * 3600 + time_left_s * 60
    progress = ttk.Progressbar(pages['session'], mode= 'indeterminate', orient= 'horizontal')
    if seconds_of_timer != 0:
        progress.configure(mode ='determinate', maximum= seconds_of_timer)
        bar(progress, seconds_of_timer)
        
    else: 
        progress.start()

    progress.grid(row= 1, column= 2)
    

def time_at_stop(t):
    time = t

def stop_timer_pressed():
    global stop_flag
    
    if not stop_flag:
        stop_flag = True
        
    else: 
        stop_flag = False
    

def start_session_pressed(hrs, mins):
    global pages, session_timer
    
    timer_label = ttk.Label(pages['session'], text= session_timer)
    timer_label.grid(row= 1, column= 1, sticky= tk.N)
    timer_label.after(1000, lambda: update_time( timer_label))
    start_btn_frame = tk.Frame(pages['session'])
    start_btn_frame.grid(row= 0, column= 0 , sticky= tk.NSEW)
    stop_time_button = ttk.Button(start_btn_frame, text= 'Pause Session', command= stop_timer_pressed)
    stop_time_button.grid(row= 0, column= 0, sticky= tk.NSEW)
    #stop_time_button.pack() pack is an option if i have already made a frame
    start_btn_frame.tkraise()
    start_progressbar(hrs, mins)
    
    


def upload_session():
    pass


def show_pages(page_name):
    global pages
    pages[page_name].tkraise() 

def create_pages():
    global pages
    for name in ('session', 'home'):
        page = tk.Frame(root)
        page.grid(row = 1, column=0, sticky= tk.NSEW)
        pages[name] = page
        for i in range(4):
            pages[name].rowconfigure(i, weight= 1)
            pages[name].columnconfigure(i, weight= 1)


def setup_app():
    global pages
    ttk.Label(pages['home'], text='Study Tracker').grid(row=0, column=0, sticky= tk.NSEW)
    
    
    ttk.Label(pages["session"], text="Study session").grid(row= 0, column= 0, sticky= tk.NSEW)
    
    
    
    timer_entry_hour = ttk.Combobox(pages['session'], values =constants.combobox_hours)
    timer_entry_minutes = ttk.Combobox(pages['session'], values =constants.combobox_minutes)
    timer_entry_hour.set('0')
    timer_entry_minutes.set('00')
    timer_entry_hour.grid(row= 0, column= 1)
    timer_entry_minutes.grid(row= 0, column= 2)

    
    ttk.Button(pages['session'], text = 'start session', command= lambda: start_session_pressed(timer_entry_hour, timer_entry_minutes)).grid(row= 0, column= 0, sticky= tk.NSEW)
    ttk.Button(pages["session"],text="Back",command=lambda: show_pages("home")).grid(row= 3, column= 0, sticky= tk.NSEW)
    ttk.Button(pages['session'], text='Upload session', command=upload_session).grid(row=3, column=3, sticky= tk.NSEW)
    ttk.Button(pages['home'], text= 'Start a session', command= lambda: show_pages('session')).grid(row=3, column=0, sticky= tk.NSEW)
    

if __name__ == '__main__':
    
    root_setup()
    create_pages()
    setup_app()
    root.mainloop()
    