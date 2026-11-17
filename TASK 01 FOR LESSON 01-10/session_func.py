import globals as glob
import datetime
import winsound
from tkinter import ttk
import tkinter as tk



    
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


def start_session_pressed(hrs, mins):
    
    
    timer_label = ttk.Label(glob.pages['session'], text= glob.session_timer)
    timer_label.grid(row= 1, column= 1, sticky= tk.N)
    timer_label.after(1000, lambda: update_time( timer_label))
    start_btn_frame = tk.Frame(glob.pages['session'])
    start_btn_frame.grid(row= 0, column= 0 , sticky= tk.NSEW)
    stop_time_button = ttk.Button(start_btn_frame, text= 'Pause', command= lambda: stop_timer_pressed(stop_time_button))
    stop_time_button.grid(row= 0, column= 0, sticky= tk.NSEW)
    #stop_time_button.pack() pack is an option if i have already made a frame
    start_btn_frame.tkraise()
    start_progressbar(hrs, mins)


def stop_timer_pressed(stp_time_btn):
    
    
    if not glob.stop_flag:
        glob.stop_flag = True
        stp_time_btn.configure(text = 'Pause')
        
    else: 
        glob.stop_flag = False
        stp_time_btn.configure(text = 'Resume')

    