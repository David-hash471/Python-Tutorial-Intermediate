import tkinter as tk
import datetime



object_rvh_holder = {}
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
update_time_active = False

session_rvh_initialized = False

session_data_structure = ['Date', 'Start Time', 'End Time', 'Session Lenght', 'Study Time', 'Break Time', 'Focus Area', 'Notes']

def calculate_times():
    
    session_length = datetime_session_end - datetime_session_start
    break_time = session_length - session_timer

    return [session_length, break_time]

def session_data():
    return [date_today,datetime_session_start,datetime_session_end,(datetime_session_end - datetime_session_start),session_timer,((datetime_session_end - datetime_session_start) - session_timer), focus_area_txt, notes_txt]


class Reset_values_holder:
    def __init__(self, name = None, *args, **kwargs):
            self.name = name
            self.argtuple = args
            self.kwdict = kwargs
            store_rvh(self, name)
            
    def add_values(self, *args, **kwargs):
        self.argtuple += args
        self.kwdict.update(kwargs)

    def __str__(self):
         return 'scoped'

    def return_arg_values(self):
        return self.argtuple

    def return_kwarg_values(self):
        return self.kwdict

    def return_values(self):
        return {'arg': self.argtuple, 'kwdict': self.kwdict}

     
def store_rvh(obj, name):
     object_rvh_holder[name] = obj


def return_rvh_object(name):
    return object_rvh_holder[name]
     