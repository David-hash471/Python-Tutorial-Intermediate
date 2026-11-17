import globals as glob
import datetime




    
def update_time(label):
    
    if glob.stop_flag:
        glob.session_timer += datetime.timedelta(seconds = 1)
    label.configure(text = glob.session_timer) 
    label.after(999, lambda: update_time(label))


