import pickle
from datetime import date
import tkinter as tk
import tkinter.ttk as ttk
import time

def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

time_record = load_obj('record')

master = tk.Tk()
time_record_keys = time_record.keys()
for no, key in enumerate(time_record_keys):
    tk.Label(master, text = key).grid(row = no)
    globals()['entry%s'%no] = tk.Entry(master)
    globals()['entry%s'%no].insert(-1, 0.0)
    globals()['entry%s'%no].grid(row=no, column=1)
    globals()['progress_bar%s'%no] = ttk.Progressbar(master, orient="horizontal", mode="determinate", maximum=100, value=sum(time_record[key].values()) / 100.0)
    globals()['progress_bar%s'%no].grid(row=no, column=2)
    
def save_data_button(time_record):
    time_record_keys = time_record.keys()
    for no, key in enumerate(time_record_keys):
        time_record[key][date.today()] = float(globals()['entry%s'%no].get())
def update_progress(time_record):
    time_record_keys = time_record.keys()
    for no, key in enumerate(time_record_keys):
        globals()['progress_bar%s'%no].value=sum(time_record[key].values()) / 100.0 + 10

tk.Button(master, text='Save', command= lambda: save_data_button(time_record)).grid(row=len(time_record)+1, column=1, sticky=tk.W, pady=4)
tk.Button(master, text='Update', command= lambda: update_progress(time_record)).grid(row=len(time_record)+1, column=2, sticky=tk.W, pady=4)
tk.Button(master, text='Quit', command=master.quit).grid(row=len(time_record)+1, column=0, sticky=tk.W, pady=4)


tk.mainloop()

time.sleep(0.5)
save_obj(time_record, 'record')

