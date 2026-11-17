import tkinter as tk
import datetime




root = tk.Tk()
session_timer = datetime.timedelta()
stop_flag = True
progressbar =0
pages = {}


combobox_hours = ['0', '1', '2', '3']
combobox_minutes = [ f'{minute:02d}' for minute in range(0, 60, 5)]
