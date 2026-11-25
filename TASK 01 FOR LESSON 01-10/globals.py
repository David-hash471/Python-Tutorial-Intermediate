import tkinter as tk
import datetime





wc_objs = {}
st_objs = {}
root = tk.Tk()
session_timer = datetime.timedelta()
session_lenght_timer = datetime.timedelta()
not_paused = True
progressbar_value =0
pages = {}
date_today = datetime.date.today()
datetime_session_start = None
datetime_session_end = None
focus_area_txt = ''
notes_txt = ''
update_time_active = False
session_timer_upload = datetime.timedelta()
session_limit_set = False
start_session_pressed = False
set_session_len_pressed = False
set_study_time_pressed = False
run_progress_bar = False
extend_btn_pressed_in = False
session_is_indeterminate = True
extend_seconds = 0
extend_btn_is_made = False
seconds_of_timer = 0



session_data_structure = ['Date', 'Start Time', 'End Time', 'Session Lenght', 'Study Time', 'Break Time', 'Focus Area', 'Notes']

def calculate_times():
    session_timer_upload = session_timer
    session_length = datetime_session_end - datetime_session_start
    break_time = session_length - session_timer_upload
    s = int(session_length.total_seconds())
    b = int(break_time.total_seconds())
    session_len = datetime.timedelta(seconds = s - 1)
    break_t = datetime.timedelta(seconds= b)
    session_timer_upload += datetime.timedelta(seconds= -1)
    return [session_len, session_timer_upload, break_t]

def session_data():
    return [date_today,datetime_session_start,datetime_session_end,calculate_times()[0],calculate_times()[1],calculate_times()[2], focus_area_txt, notes_txt]


class Widget_container:
    def __init__(self, name = None, *args, **kwargs):
            self.name = name
            self.argtuple = args
            self.kwdict = kwargs
            store_obj(self,wc_objs,name)
            
    def add_values(self, *args, **kwargs):
        self.argtuple += args
        self.kwdict.update(kwargs)

    def __str__(self):
         return 'scoped'

    def return_arg_values(self):
        return self.argtuple

    def return_kwarg_values(self):
        return self.kwdict


     
def store_obj(obj, var_name, obj_name):
     var_name[obj_name] = obj


def return_obj(var_name, name):
    return var_name[name]






class Task:
    def __init__(self, name):
        self.frame_status = 'READY'
        self.name = name
        store_obj(self, st_objs,name)

    def change_st(self):
        
        if self.frame_status == 'READY':
            self.frame_status = 'IN_USE'
        elif self.frame_status == 'IN_USE':
            self.frame_status = 'USED'
        elif self.frame_status == 'USED':
            self.frame_status = 'READY'
        

    def return_st(self):
        if self.frame_status == 'READY':
            return 0
        elif self.frame_status == 'IN_USE':
            return 1
        elif self.frame_status == 'USED':
            return 2        
        



    

