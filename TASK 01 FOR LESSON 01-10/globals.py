import tkinter as tk
import datetime




root = tk.Tk()
session_timer = datetime.timedelta()
stop_flag = True
progressbar =0
pages = {}
date_today = datetime.date.today()
datetime_session_start = None
datetime_session_end = None
focus_area_txt = ''
notes_txt = ''
page_been_setup = {}

session_data_structure = ['Date', 'Start Time', 'End Time', 'Session Lenght', 'Study Time', 'Break Time', 'Focus Area', 'Notes']

def calculate_times():
    
    session_length = datetime_session_end - datetime_session_start
    break_time = session_length - session_timer

    return [session_length, break_time]

def session_data():
    return [date_today,datetime_session_start,datetime_session_end,(datetime_session_end - datetime_session_start),session_timer,((datetime_session_end - datetime_session_start) - session_timer), focus_area_txt, notes_txt]

