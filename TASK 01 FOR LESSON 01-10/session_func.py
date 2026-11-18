import globals as glob
import datetime, winsound
import session_func, global_func, uploadSession_func, home_func, globals
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

combobox_hours = ['0', '1', '2', '3']
combobox_minutes = [ f'{minute:02d}' for minute in range(0, 60, 5)]


    
def update_time(label):
    
    if glob.stop_flag:
        glob.session_timer += datetime.timedelta(seconds = 1)
    label.configure(text = glob.session_timer) 
    label.after(999, lambda: update_time(label))

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

def stop_session(stop_session_btn, stop_time_btn):
    
    ttk.Button(glob.pages['session'], text='Upload session', command= lambda: global_func.show_page('upload session')).grid(row=3, column=3, sticky= tk.NSEW)
    if tk.messagebox.askyesno(message = 'Stop session?'):
        stop_session_btn.grid_remove()
        stop_time_btn.grid_remove()
        glob.datetime_session_end = datetime.datetime.now()
        glob.stop_flag = False
        winsound.Beep(1000, 1000)
    else: 
        pass    

def start_session_pressed(hrs, mins):
    
    glob.datetime_session_start = datetime.datetime.now()
    timer_label = ttk.Label(glob.pages['session'], text= glob.session_timer)
    timer_label.grid(row= 1, column= 1, sticky= tk.N)
    timer_label.after(1000, lambda: update_time( timer_label))
    start_btn_frame = tk.Frame(glob.pages['session'])
    start_btn_frame.grid(row= 0, column= 0 , sticky= tk.NSEW)
    stop_time_button = ttk.Button(start_btn_frame, text= 'Pause', command= lambda: pause_timer_pressed(stop_time_button))
    stop_time_button.grid(row= 0, column= 0, sticky= tk.NSEW)
    stop_session_btn = ttk.Button(glob.pages['session'], text='stop session', command= lambda: stop_session(stop_session_btn, stop_time_button))
    stop_session_btn.grid(row=2, column=3, sticky= tk.NSEW)
    #stop_time_button.pack() pack is an option if i have already made a frame
    start_btn_frame.tkraise()
    start_progressbar(hrs, mins)


def pause_timer_pressed(stp_time_btn = None):
    
    if not glob.stop_flag:
        glob.stop_flag = True
        if stp_time_btn != None:
            stp_time_btn.configure(text = 'Pause')
      
    else: 
        glob.stop_flag = False
        if stp_time_btn != None:
            stp_time_btn.configure(text = 'Resume')

def setup_session():
    global combobox_hours, combobox_minutes
    timer_entry_hour = ttk.Combobox(glob.pages['session'], values =combobox_hours)
    timer_entry_minutes = ttk.Combobox(glob.pages['session'], values =combobox_minutes)
    timer_entry_hour.set('0')
    timer_entry_minutes.set('00')
    timer_entry_hour.grid(row= 0, column= 1)
    timer_entry_minutes.grid(row= 0, column= 2)
    
    ttk.Button(glob.pages['session'], text = 'start session', command= lambda: session_func.start_session_pressed(timer_entry_hour, timer_entry_minutes)).grid(row= 0, column= 0, sticky= tk.NSEW)
    ttk.Button(glob.pages["session"],text="Back",command=lambda: global_func.show_page("home")).grid(row= 3, column= 0, sticky= tk.NSEW)
    
    