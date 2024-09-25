#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
    except IndexError:
        pass

def complete_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.itemconfig(selected_task, {'bg':'light green', 'fg':'black'})
    except IndexError:
        pass

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, font=("Helvetica", 14))
entry.pack(side=tk.LEFT)

add_button = tk.Button(frame, text="Add Task", font=("Helvetica", 12), command=add_task)
add_button.pack(side=tk.LEFT)

remove_button = tk.Button(root, text="Remove Task", font=("Helvetica", 12), command=remove_task)
remove_button.pack(pady=10)

complete_button = tk.Button(root, text="Complete Task", font=("Helvetica", 12), command=complete_task)
complete_button.pack(pady=5)

task_list = tk.Listbox(root, selectmode=tk.SINGLE, font=("Helvetica", 12), selectbackground="yellow")
task_list.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()


# In[ ]:





# In[ ]:




