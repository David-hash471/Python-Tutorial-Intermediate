import globals as glob
from tkinter import ttk
import tkinter as tk
import csv, global_func
from tkinter import messagebox
import datetime 


def setup_uploadSession():
    ttk.Label(glob.pages['upload session'][0], text= f'Date:{glob.date_today}').grid(row=0, column=0, columnspan=3, sticky=tk.W, padx=8, pady=4)
    st_time = ttk.Label(glob.pages['upload session'][0], text=  f'Start Time:{glob.datetime_session_start.strftime('%I:%M %p')}')
    st_time.grid(row=1, column=0, sticky=tk.W, padx=8, pady=4)
    end_time = ttk.Label(glob.pages['upload session'][0], text= f'End Time:{glob.datetime_session_end.strftime('%I:%M %p')}')
    end_time.grid(row=2, column=0, sticky=tk.W, padx=8, pady=4)
    sess_leng = ttk.Label(glob.pages['upload session'][0], text= f'Session Lenght:{glob.calculate_times()[0]}')
    sess_leng.grid(row=3, column=0, sticky=tk.W, padx=8, pady=4)
    study_time = ttk.Label(glob.pages['upload session'][0], text= f'Study Time:{glob.session_timer_upload}')
    study_time.grid(row=4, column=0, sticky=tk.W, padx=8, pady=4)
    break_time = ttk.Label(glob.pages['upload session'][0], text= f'Break Time:{glob.calculate_times()[1]}')
    break_time.grid(row=5, column=0, sticky=tk.W, padx=8, pady=4)
    ttk.Label(glob.pages['upload session'][0], text= 'Focus Area').grid(row=1, column= 1, sticky=tk.E, padx=6, pady=4)
    ttk.Label(glob.pages['upload session'][0], text= 'Notes').grid(row=2, column= 1, sticky=tk.E, padx=6, pady=4)
    focus_area = ttk.Entry(glob.pages['upload session'][0], textvariable='Focus Area')
    focus_area.grid(row= 1, column=2, sticky=tk.EW, padx=6, pady=4)
    notes = ttk.Entry(glob.pages['upload session'][0])
    notes.grid(row= 2, column=2, sticky=tk.EW, padx=6, pady=4)
    ttk.Button(glob.pages['upload session'][0], text= 'Save', command= lambda: save_session(focus_area, notes)).grid(row=6,column=2, sticky=tk.E, padx=6, pady=8)
    glob.return_obj(glob.rvh_objs,'session').return_kwarg_values()['timer_label'].grid_remove()
    glob.return_obj(glob.rvh_objs,'session').return_kwarg_values()['finish_upload_session_btn'].grid_remove()


def save_session(focus_area, notes):
    glob.focus_area_txt = focus_area.get()
    glob.notes_txt = notes.get()


    if messagebox.askokcancel(None, message=  'Save Session?'):
       with open('session_data.csv', 'a', newline= '') as file_handle_append:
            append_object = csv.writer(file_handle_append)
            append_object.writerow(glob.session_data()) 
            global_func.show_page('home')
            glob.session_timer = datetime.timedelta()
    else:
        global_func.show_page('home')
        glob.session_timer = datetime.timedelta()
