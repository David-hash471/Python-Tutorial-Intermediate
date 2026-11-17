import globals as glob
from tkinter import ttk
import tkinter as tk
import csv



def setup_uploadSession():
    ttk.Label(glob.pages['upload session'], text= f'Date:{glob.date_today}').grid(row=0, column=0)
    st_time = ttk.Label(glob.pages['upload session'], text=  f'Start Time:{glob.datetime_session_start.strftime('%I:%M %p')}')
    st_time.grid(row=1, column=0)
    end_time = ttk.Label(glob.pages['upload session'], text= f'End Time:{glob.datetime_session_end.strftime('%I:%M %p')}')
    end_time.grid(row=2, column=0)
    sess_leng = ttk.Label(glob.pages['upload session'], text= f'Session Lenght:{glob.calculate_times()[0]}')
    sess_leng.grid(row=3, column=0)
    study_time = ttk.Label(glob.pages['upload session'], text= f'Study Time:{glob.session_timer}')
    study_time.grid(row=4, column=0)
    break_time = ttk.Label(glob.pages['upload session'], text= f'Break Time:{glob.calculate_times()[1]}')
    break_time.grid(row=5, column=0)

    focus_area = ttk.Entry(glob.pages['upload session'], textvariable='Focus Area')
    focus_area.grid(row= 1, column=1)
    glob.focus_area_txt = focus_area.get()
    notes = ttk.Notebook(glob.pages['upload session'])
    notes.grid(row= 2, column= 2, sticky= tk.NSEW)
    ttk.Button(glob.pages['upload session'], text= 'Save', command=save_session).grid(row=3,column=3)


def save_session():


    with open('session_data.csv', 'a', newline= '') as file_handle_append:
        append_object = csv.writer(file_handle_append)
