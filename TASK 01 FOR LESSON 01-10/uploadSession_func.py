import globals as glob
from tkinter import ttk
import tkinter as tk
import csv, global_func
from tkinter import messagebox
import datetime 


def setup_uploadSession():
    ttk.Label(glob.pages['upload session'][0], text= f'Date:  {glob.date_today}').place(x= 8, y= 8)
    st_time = ttk.Label(glob.pages['upload session'][0], text=  f'Start Time:  {glob.datetime_session_start.strftime('%I:%M %p')}')
    st_time.place(x= 8, y= 40)
    end_time = ttk.Label(glob.pages['upload session'][0], text= f'End Time:  {glob.datetime_session_end.strftime('%I:%M %p')}')
    end_time.place(x= 8, y= 72)
    sess_leng = ttk.Label(glob.pages['upload session'][0], text= f'Session Lenght:  {glob.calculate_times()[0]}')
    sess_leng.place(x= 8, y= 104)
    study_time = ttk.Label(glob.pages['upload session'][0], text= f'Study Time:  {glob.calculate_times()[1]}')
    study_time.place(x= 8, y= 136)
    break_time = ttk.Label(glob.pages['upload session'][0], text= f'Break Time:  {glob.calculate_times()[2]}')
    break_time.place(x= 8, y= 168)
    ttk.Label(glob.pages['upload session'][0], text= 'Focus Area:').place(x= 140,y= 8, width= 65, height= 20)
    ttk.Label(glob.pages['upload session'][0], text= 'Notes:').place(x= 165,y= 40, width= 50, height= 20)
    focus_area = ttk.Entry(glob.pages['upload session'][0])
    focus_area.place(x= 210,y= 5, width= 185, height= 20)
    notes = ttk.Entry(glob.pages['upload session'][0])
    notes.place(x= 210,y= 37, width= 185, height= 20)
    ttk.Button(glob.pages['upload session'][0], text= 'Save', command= lambda: save_session(focus_area, notes)).place(x= 295, y=150 ,width= 100, height= 45)



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
        glob.session_lenght_timer = datetime.timedelta()
