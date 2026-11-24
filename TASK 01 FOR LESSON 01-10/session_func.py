import globals as glob
import datetime, winsound
import session_func, global_func, uploadSession_func, home_func, globals
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from playsound3 import playsound
combobox_hours = ['0', '1', '2', '3']
combobox_minutes = [ f'{minute:02d}' for minute in range(0, 60, 5)]
update_time_initial_wait = True


    
def update_time():
    if glob.update_time_active:
        if glob.not_paused:
            glob.session_timer += datetime.timedelta(seconds = 1)
            
            if glob.set_study_time_pressed and not glob.session_is_indeterminate:
                glob.session_lenght_timer += datetime.timedelta(seconds= -1)
                glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['session_length_timer_label'].configure(text = glob.session_lenght_timer)
        glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['timer_label'].configure(text = glob.session_timer) 
        if glob.set_session_len_pressed and not glob.session_is_indeterminate:
            glob.session_lenght_timer += datetime.timedelta(seconds= -1)
            glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['session_length_timer_label'].configure(text = glob.session_lenght_timer)           
        glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['timer_label'].after(999, update_time)

def session_complete():
    playsound(r"C:\Users\david\OneDrive\Documents\Personal\David\Projects\Python projects\Python Tutorial\Python-Tutorial-Intermediate\TASK 01 FOR LESSON 01-10\Assets\chime.wav")
    
    glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['pause_time_btn'].destroy()  
    glob.datetime_session_end = datetime.datetime.now()  
    glob.session_timer_upload = glob.session_timer
    glob.return_obj(glob.st_objs, 'session_st').change_st()
    glob.not_paused = False
    glob.update_time_active =False    
    global_func.show_page('upload session')

def bar(s):
    if glob.run_progress_bar:
        if glob.set_session_len_pressed:
            glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['progress']['value'] = glob.progressbar_value
            glob.progressbar_value += 1
            if glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['progress']['value'] != (s-1):
                glob.root.after(1000, lambda: bar(s))
            else:
                 session_complete()
        elif glob.not_paused:
            glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['progress']['value'] = glob.progressbar_value
            glob.progressbar_value += 1
            if glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['progress']['value'] != (s-1):
                glob.root.after(1000, lambda: bar(s))
            else:
                session_complete()
        elif s == 0 and not glob.not_paused:
            glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['progress'].stop()
            glob.root.after(1000, lambda: bar(s))
        elif s == 0 and glob.not_paused:
            glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['progress'].start()
            glob.root.after(1000, lambda: bar(s))
        else:
            glob.root.after(1000, lambda: bar(s))
    

def start_progressbar(seconds_of_timer = None):
    glob.run_progress_bar = True
    progress = ttk.Progressbar(glob.pages['session'][0], mode= 'indeterminate', orient= 'horizontal')
    glob.return_obj(glob.wc_objs, 'session').add_values(progress = progress)
    if glob.session_is_indeterminate:
        progress.start()
    else: 
        progress.configure(mode ='determinate', maximum= seconds_of_timer)
        glob.session_is_indeterminate = False
        bar(seconds_of_timer)
    progress.place(x = 110, y = 6, width = 285,height = 44)
    

def stop_session():
    if tk.messagebox.askyesno(message = 'Stop session?'):
        session_complete()    

def clear_session():
    glob.not_paused = False
    glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['time_pased_label'].destroy()
    glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['time_left_label'].destroy()
    glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['progress'].destroy()
    glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['timer_label'].destroy()
    glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['abandon_session_btn'].destroy()
    glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['finish_upload_session_btn'].destroy()
    glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['pause_time_btn'].destroy()
    glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['finish_upload_session_btn'].destroy()
    glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['session_length_timer_label'].destroy()
    glob.session_timer = datetime.timedelta()
    glob.session_lenght_timer = datetime.timedelta()
    glob.update_time_active = False
    glob.progressbar_value =0
    glob.set_session_len_pressed = False
    glob.set_study_time_pressed = False
    glob.start_session_pressed = False
    glob.run_progress_bar =False
    
     
    

def abandon_session():

    if messagebox.askokcancel(None, message= 'Abandon Session'):
        glob.return_obj(glob.st_objs, 'session_st').change_st()
        global_func.show_page('home')
    else:
        pass



def start_session_pressed():
    glob.start_session_pressed = True
    session_length_timer_label = ttk.Label(glob.pages['session'][0], text= glob.session_lenght_timer)
    timer_label = ttk.Label(glob.pages['session'][0], text= glob.session_timer)
    glob.not_paused = True
    if glob.set_session_len_pressed:
        time_left_h = int(glob.return_obj(glob.wc_objs,'session').return_kwarg_values()['combobox_hr'].get()) 
        time_left_s = int(glob.return_obj(glob.wc_objs,'session').return_kwarg_values()['combobox_min'].get()) 
        seconds_of_timer = time_left_h * 3600 + time_left_s * 60  
        if seconds_of_timer != 0:
            glob.session_is_indeterminate = False 
            start_progressbar(seconds_of_timer)
            glob.session_lenght_timer = datetime.timedelta(seconds= seconds_of_timer)
            glob.update_time_active = True 
            timer_label.after(1000,  update_time)
        else:
            glob.session_is_indeterminate = True
            glob.update_time_active =True
            timer_label.after(1000, update_time)
            start_progressbar(seconds_of_timer)
    elif glob.set_study_time_pressed:    
        time_left_h = int(glob.return_obj(glob.wc_objs,'session').return_kwarg_values()['combobox_hr'].get()) 
        time_left_s = int(glob.return_obj(glob.wc_objs,'session').return_kwarg_values()['combobox_min'].get()) 
        seconds_of_timer = time_left_h * 3600 + time_left_s * 60  
        if seconds_of_timer != 0:
            glob.session_is_indeterminate = False 
            start_progressbar(seconds_of_timer) 
            glob.update_time_active =True
            session_length_timer_label.after(1000, update_time)
            glob.session_lenght_timer = datetime.timedelta(seconds= seconds_of_timer)
        else:
            glob.session_is_indeterminate = True
            start_progressbar(seconds_of_timer)
            session_length_timer_label.after(1000, update_time)
            glob.update_time_active =True
    else:
        glob.session_is_indeterminate = True
        start_progressbar()   
        glob.update_time_active =True
        timer_label.after(1000, update_time)

    if glob.session_is_indeterminate:
        session_length_timer_label.configure(text= 'Undetermined')
    glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['st_session_btn'].destroy()

    
    glob.datetime_session_start = datetime.datetime.now()

    session_length_timer_label.place(x= 172, y= 66)
    timer_label.place(x = 212, y = 116)
    abandon_session_btn = ttk.Button(glob.pages['session'][0], text= 'Abandon Session', command= abandon_session)
    abandon_session_btn.place(x = 5, y = 102 , width= 100, height=46)
    pause_time_btn = ttk.Button(glob.pages['session'][0], text= 'Pause', command= pause_timer_pressed)
    pause_time_btn.place(x = 5, y= 5, width= 100, height= 45)
    finish_upload_session_btn = ttk.Button(glob.pages['session'][0], text='Finish & Upload', command= stop_session)
    finish_upload_session_btn.place(x = 295, y=149, width= 100, height= 46)
    time_left_label = ttk.Label(glob.pages['session'][0], text= 'Time Left:')
    time_left_label.place(x = 110, y= 52, width= 58 , height= 48)
    time_pased_label = ttk.Label(glob.pages['session'][0], text= 'Time Studying:')
    time_pased_label.place(x = 110, y= 102, width= 90 , height= 48)

    if glob.set_session_len_pressed or glob.set_study_time_pressed:
        glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['combobox_hr'].destroy()
        glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['combobox_min'].destroy()
    glob.return_obj(glob.wc_objs, 'session').add_values(pause_time_btn=pause_time_btn,
                                                        time_left_label = time_left_label,
                                                        time_pased_label = time_pased_label,
                                                        abandon_session_btn = abandon_session_btn,
                                                        finish_upload_session_btn = finish_upload_session_btn,
                                                        timer_label = timer_label,
                                                        session_length_timer_label = session_length_timer_label)
    
    
    
        


def pause_timer_pressed():
    if not glob.not_paused:
        glob.not_paused = True
        glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['pause_time_btn'].configure(text = 'Pause')
        if glob.session_is_indeterminate:
            glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['progress'].start()       
        
    else: 
        glob.not_paused = False
        glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['pause_time_btn'].configure(text = 'Resume')
        if glob.session_is_indeterminate:
            glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['progress'].stop()

def reset_set_choice():
    if not glob.start_session_pressed:
        if glob.set_study_time_pressed or glob.set_session_len_pressed:
            glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['combobox_hr'].destroy()
            glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['combobox_min'].destroy()
            glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['st_session_btn'].destroy()
            glob.return_obj(glob.st_objs, 'session_st').change_st()
            glob.return_obj(glob.st_objs, 'session_st').change_st()




def setup_session():
    
    set_session_len_btn = ttk.Button(glob.pages['session'][0], text= 'Set Session Lenght', command= lambda: set_session_w_limit(True))
    set_session_len_btn.place(x = 110, y=5 , width= 137, height= 45)
    set_study_time_btn = ttk.Button(glob.pages['session'][0], text= 'Set Study Time', command= lambda: set_session_w_limit(False))
    set_study_time_btn.place(x = 252, y=5, width= 138, height= 45)
    st_session_btn = ttk.Button(glob.pages['session'][0], text = 'Start a Session', command= start_session_pressed)
    st_session_btn.place(x = 5, y= 5, width= 100, height= 45)
    ttk.Button(glob.pages["session"][0],text="Back",command=lambda: global_func.show_page("home")).place(x= 5, y= 150, width=100, height= 45)
    glob.return_obj(glob.wc_objs, 'session').add_values(st_session_btn = st_session_btn,
                                                        set_session_len_btn = set_session_len_btn,
                                                        set_study_time_btn = set_study_time_btn)
        
def set_session_w_limit(type):
    if type:
        glob.set_session_len_pressed = True
        glob.set_study_time_pressed = False
    elif not type:
        glob.set_study_time_pressed = True
        glob.set_session_len_pressed = False

    global combobox_hours, combobox_minutes
    combobox_hr = ttk.Combobox(glob.pages['session'][0], values =combobox_hours)
    combobox_min = ttk.Combobox(glob.pages['session'][0], values =combobox_minutes)
    combobox_hr.set('0')
    combobox_min.set('00')
    glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['set_session_len_btn'].destroy()
    glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['set_study_time_btn'].destroy()
    combobox_hr.place(x = 110, y = 6, width= 140 , height= 44)
    combobox_min.place(x = 250, y = 6, width= 140 , height= 44) 
    glob.return_obj(glob.wc_objs, 'session').add_values(combobox_hr = combobox_hr,
                                                        combobox_min = combobox_min)
    glob.return_obj(glob.wc_objs, 'session').return_kwarg_values()['st_session_btn'].configure(text = 'Start Session')


