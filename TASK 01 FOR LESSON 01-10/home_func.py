import globals as glob
import global_func
from tkinter import ttk
import tkinter as tk



def setup_home():
    ttk.Button(glob.pages['home'], text= 'Start a session', command= lambda: global_func.show_page('session')).grid(row=3, column=0, sticky= tk.NSEW)