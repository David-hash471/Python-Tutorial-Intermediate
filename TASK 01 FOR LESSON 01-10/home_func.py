import globals as glob
import global_func
from tkinter import ttk
import tkinter as tk



def setup_home():
    ttk.Button(glob.pages['home'][0], text= 'Start a session', command= lambda: global_func.show_page('session')).grid(row=1, column=1, sticky= tk.NSEW, padx=12, pady=12)
