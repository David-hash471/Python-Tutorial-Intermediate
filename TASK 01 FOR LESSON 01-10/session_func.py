import globals as glob
import datetime, winsound
import session_func, global_func, uploadSession_func, home_func, globals
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import time

combobox_hours = ['0', '1', '2', '3']
combobox_minutes = [ f'{minute:02d}' for minute in range(0, 60, 5)]
update_time_initial_wait = True


    
def update_time(label):
    if glob.update_time_active:
        if glob.stop_flag:
            glob.session_timer += datetime.timedelta(seconds = 1)
        label.configure(text = glob.session_timer) 
        label.after(999, lambda: update_time(label))

def session_complete():
    winsound.Beep(1000, 1000)
    glob.stop_flag = False
    glob.return_obj(glob.rvh_objs, 'session').return_kwarg_values()['pause_time_btn'].destroy()  
    glob.datetime_session_end = datetime.datetime.now()  
    glob.session_timer_upload = glob.session_timer
    glob.return_obj(glob.st_objs, 'session_st').change_st()
    glob.update_time_active = False
    glob.stop_flag = False    
    global_func.show_page('upload session')

def bar(progress, s):
    
    if glob.stop_flag:
        progress['value'] = glob.progressbar
        glob.progressbar += 1
        if progress['value'] != s:
            glob.root.after(1000, lambda: bar(progress, s))
        else:
            stop_session()
    elif s == 0 and not glob.stop_flag:
        progress.stop()
        glob.root.after(1000, lambda: bar(progress, s))
    elif s == 0 and glob.stop_flag:
        progress.start()
        glob.root.after(1000, lambda: bar(progress, s))
    else:
        glob.root.after(1000, lambda: bar(progress, s))


def start_progressbar(seconds_of_timer):
    

    progress = ttk.Progressbar(glob.pages['session'][0], mode= 'indeterminate', orient= 'horizontal')
    if seconds_of_timer != 0:
        progress.configure(mode ='determinate', maximum= seconds_of_timer)
        bar(progress, seconds_of_timer)
        
    else: 
        progress.start()

    progress.place(x = 110, y = 6, width = 280,height = 44)
    glob.return_obj(glob.rvh_objs, 'session').add_values(progress = progress)

def stop_session():
    
    if tk.messagebox.askyesno(message = 'Stop session?'):
        session_complete()
        
    else: 
        pass    

def clear_session():
    glob.update_time_active = False
    glob.return_obj(glob.rvh_objs, 'session').return_kwarg_values()['time_pased_label'].destroy()
    glob.return_obj(glob.rvh_objs, 'session').return_kwarg_values()['time_left_label'].destroy()
    glob.return_obj(glob.rvh_objs, 'session').return_kwarg_values()['progress'].place_forget()
    glob.return_obj(glob.rvh_objs, 'session').return_kwarg_values()['timer_label'].destroy()
    glob.return_obj(glob.rvh_objs, 'session').return_kwarg_values()['abandon_session_btn'].destroy()
    glob.return_obj(glob.rvh_objs, 'session').return_kwarg_values()['finish_upload_session_btn'].destroy()
    glob.return_obj(glob.rvh_objs, 'session').return_kwarg_values()['pause_time_btn'].destroy()
    glob.return_obj(glob.rvh_objs, 'session').return_kwarg_values()['finish_upload_session_btn'].destroy()
    glob.session_timer = datetime.timedelta()
    glob.progressbar =0
    

def abandon_session():

    if messagebox.askokcancel(None, message= 'Abandon Session'):
        glob.return_obj(glob.st_objs, 'session_st').change_st()
        global_func.show_page('home')
    else:
        pass

def start_session_pressed(hrs, mins):
    glob.return_obj(glob.rvh_objs, 'session').return_kwarg_values()['st_session_btn'].destroy()
    if hrs.get() == '' and mins.get() == '':
        glob.session_limit_set = False
    glob.stop_flag = True
    glob.update_time_active = True
    glob.datetime_session_start = datetime.datetime.now()


    timer_label = ttk.Label(glob.pages['session'][0], text= glob.session_timer)
    timer_label.place(x = 202, y = 116)
    abandon_session_btn = ttk.Button(glob.pages['session'][0], text= 'Abandon Session', command= abandon_session)
    abandon_session_btn.place(x = 5, y = 102 , width= 100, height=46)
    pause_time_btn = ttk.Button(glob.pages['session'][0], text= 'Pause', command= lambda: pause_timer_pressed(pause_time_btn))
    pause_time_btn.place(x = 5, y= 5, width= 100, height= 45)
    finish_upload_session_btn = ttk.Button(glob.pages['session'][0], text='Finish & Upload', command= stop_session)
    finish_upload_session_btn.place(x = 300, y=149, width= 95, height= 46)
    time_left_label = ttk.Label(glob.pages['session'][0], text= 'Time Left:')
    time_left_label.place(x = 110, y= 52, width= 90 , height= 48)
    time_pased_label = ttk.Label(glob.pages['session'][0], text= 'Time Pased:')
    time_pased_label.place(x = 110, y= 102, width= 90 , height= 48)

    #thrs = hrs.get()
    #tmins = mins.get()
    time_left_h = int(hrs.get()) 
    time_left_s = int(mins.get()) 
    seconds_of_timer = time_left_h * 3600 + time_left_s * 60    
    start_progressbar(seconds_of_timer)

    glob.return_obj(glob.rvh_objs, 'session').add_values(pause_time_btn=pause_time_btn,
                                                        time_left_label = time_left_label,
                                                        time_pased_label = time_pased_label,
                                                        abandon_session_btn = abandon_session_btn,
                                                        finish_upload_session_btn = finish_upload_session_btn,
                                                        timer_label = timer_label)
    
    glob.return_obj(glob.rvh_objs, 'session').return_kwarg_values()['combobox1'].destroy()
    glob.return_obj(glob.rvh_objs, 'session').return_kwarg_values()['combobox2'].destroy()

    timer_label.after(1000, lambda: update_time(timer_label))
    
        


def pause_timer_pressed(stp_time_btn = None):
    
    if not glob.stop_flag:
        glob.stop_flag = True
        
        if not glob.session_limit_set:
            glob.return_obj(glob.rvh_objs, 'session').return_kwarg_values()['progress'].start()
        if stp_time_btn != None:
            stp_time_btn.configure(text = 'Pause')
      
    else: 
        glob.stop_flag = False
        if not glob.session_limit_set:
            glob.return_obj(glob.rvh_objs, 'session').return_kwarg_values()['progress'].stop()
        if stp_time_btn != None:
            stp_time_btn.configure(text = 'Resume')

def setup_session():
    global combobox_hours, combobox_minutes
    timer_entry_hour = ttk.Combobox(glob.pages['session'][0], values =combobox_hours)
    timer_entry_minutes = ttk.Combobox(glob.pages['session'][0], values =combobox_minutes)
    timer_entry_hour.set('0')
    timer_entry_minutes.set('00')
    timer_entry_hour.place(x = 110, y = 6, width= 140 , height= 44)
    timer_entry_minutes.place(x = 250, y = 6, width= 140 , height= 44)
    glob.return_obj(glob.rvh_objs, 'session').add_values(combobox1 = timer_entry_hour, combobox2 = timer_entry_minutes)
    st_session_btn = ttk.Button(glob.pages['session'][0], text = 'start session', command= lambda: session_func.start_session_pressed(timer_entry_hour, timer_entry_minutes))
    st_session_btn.place(x = 5, y= 5, width= 100, height= 45)
    glob.return_obj(glob.rvh_objs, 'session').add_values(st_session_btn = st_session_btn)
    ttk.Button(glob.pages["session"][0],text="Back",command=lambda: global_func.show_page("home")).place(x= 5, y= 150, width=100, height= 45)
    
        
