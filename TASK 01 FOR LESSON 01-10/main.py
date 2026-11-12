import tkinter as tk 
from tkinter import ttk
from tkinter.messagebox import showinfo
import datetime 

root = tk.Tk()
stop_flag = True
for i in range(3):
    root.rowconfigure(i, weight= 1)
    root.columnconfigure(i, weight= 1)

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
    

def update_time(time ,label):
    global stop_flag
    if stop_flag:
        time += datetime.timedelta(seconds = 1)
    else:
        time_at_stop(time)
    label.configure(text = time) 
    label.after(1000, lambda: update_time(time, label))
    

    
def time_at_stop(t):
    time = t

def stop_timer_pressed():
    global stop_flag
    stop_flag = False
    

def start_timer_pressed():
    global pages
    time_start = datetime.timedelta()
    timer_label = ttk.Label(pages['session'], text= time_start)
    timer_label.grid(row= 1, column= 1, sticky= tk.NSEW)
    timer_label.after(1000, lambda: update_time(time_start, timer_label))
    start_btn_frame = tk.Frame(pages['session'])
    start_btn_frame.grid(row= 0, column= 0 , sticky= tk.NSEW)
    stop_time_button = ttk.Button(start_btn_frame, text= 'Stop timer', command= stop_timer_pressed)
    stop_time_button.grid(row= 0, column= 0, sticky= tk.NSEW)
    #stop_time_button.pack() pack is an option if i have already made a frame
    start_btn_frame.tkraise()

def set_timer_btn_pressed(time):
    print(time)

    
def set_session_timer():
    global pages
    timer_entry_frame = ttk.Frame(pages['session'])
    timer_entry_frame.grid(row= 2, column= 1, sticky= tk.NSEW)
    timer_entry = ttk.Entry(timer_entry_frame)
    timer_entry.grid(row= 1, column= 1, sticky= tk.NSEW)
    timer_entry_frame.tkraise()
    enter_entry_frame = ttk.Frame(pages['session'])
    enter_entry_frame.grid(row= 2, column= 2, sticky= tk.NSEW)
    time = timer_entry.get()
    enter_entry_btn = ttk.Button(enter_entry_frame, text = 'Enter', command= lambda: set_timer_btn_pressed(time))
    enter_entry_btn.grid(row= 2, column= 2, sticky= tk.NSEW)
    




def show_pages(page_name):
    global pages
    pages[page_name].tkraise() 

def create_pages():
    global pages
    for name in ('session', 'home'):
        page = tk.Frame(root)
        page.grid(row = 1, column=0, sticky= tk.NSEW)
        pages[name] = page


def setup_app():
    global pages
    ttk.Label(pages['home'], text='Study Tracker').grid(row=0, column=0, sticky= tk.NSEW)
    ttk.Button(pages['home'], text= 'Start a session', command= lambda: show_pages('session')).grid(row=3, column=0, sticky= tk.NSEW)
    
    ttk.Label(pages["session"], text="Study session").grid(row= 0, column= 1, sticky= tk.NSEW)
    ttk.Button(pages["session"],text="Back",command=lambda: show_pages("home")).grid(row= 3, column= 0, sticky= tk.NSEW)

    ttk.Button(pages['session'], text = 'start timer', command= start_timer_pressed).grid(row= 0, column= 0, sticky= tk.NSEW)
    ttk.Button(pages['session'], text = 'set a session timer', command= set_session_timer).grid(row= 2, column= 0, sticky= tk.NSEW)
    
    

if __name__ == '__main__':
    root_setup()
    create_pages()
    setup_app()
    root.mainloop()
    