import tkinter
import random
from tkinter import messagebox
# import tkMessageBox
top = tkinter.Tk()
top.configure(bg="white")

top.title("RESOLUTIONS-2019")
top.geometry("325x275")
tasks = []
#tasks = ["get Inked!","buy a camera","Visit Goa"]



def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end",task)

def clear_listbox():
    lb_tasks.delete(0,"end")


def add_task():
     #get the task
     task = txt_input.get()
     if task !="":
       #add it to list
       tasks.append(task)
       #update
       update_listbox()
     else:
         messagebox.showwarning("Warning","Please add the task to display")
         #lbl_display["text"]= "Please enter the task."
         txt_input.delete(0,"end")

def delete_task():
     #get text of current selected item
     task = lb_tasks.get("active")
     #confirm if its list
     if task in tasks:
          tasks.remove(task)
          #update
          update_listbox()

def delete_all():
      if messagebox.askokcancel("Please Confirm", "Do you really wanna delete all tasks?? "):
       global tasks
     #clear the list box and update
       tasks = []
       update_listbox()

def sort_asc():
     tasks.sort()
     update_listbox()

def sort_dsc():
     tasks.sort()
     tasks.reverse()
     update_listbox()


def Choose_random():
#choose a random task
     task = random.choice(tasks)
     #uddate the label
     lbl_display["text"]=task

def number_of_tasks():
     #to get no of tasks
     number_of_tasks= len(tasks)
     #create the msg
     msg="number of tasks: %s" %number_of_tasks
     #display the msg
     lbl_display["text"]=msg


def exit():
     pass


lbl_title = tkinter.Label(top, text = "New Year To_Do List " , bg= "white")
lbl_title.grid(row=0,column=0)


lbl_display = tkinter.Label(top, text = " " , bg= "white")
lbl_display.grid(row=0,column=1)

txt_input = tkinter.Entry(top,width=15)
txt_input.grid(row=1,column=1)

btn_add_task = tkinter.Button(top, text="ADD TASKS", fg="green" ,bg="white" , command = add_task)
btn_add_task.grid(row=1,column=0)


btn_delete_task = tkinter.Button(top, text="DELETE TASKS", fg="green" ,bg="white" , command = delete_task)
btn_delete_task.grid(row=2,column=0)


btn_del_all_task = tkinter.Button(top, text="DELETE ALL TASKS", fg="green" ,bg="white" , command =delete_all )
btn_del_all_task.grid(row=3,column=0)


btn_sort_task_asc = tkinter.Button(top, text="SORT_ASC", fg="green" ,bg="white" , command = sort_asc)
btn_sort_task_asc.grid(row=4,column=0)


btn_add_task_dsc = tkinter.Button(top, text=" SORT_DSC", fg="green" ,bg="white" , command = sort_dsc)
btn_add_task_dsc.grid(row=5,column=0)


btn_random_task = tkinter.Button(top, text="CHOOSE RANDOM", fg="green" ,bg="white" , command = Choose_random)
btn_random_task.grid(row=6,column=0)


btn_total_task = tkinter.Button(top, text="TOTAL TASKS", fg="green" ,bg="white" , command = number_of_tasks)
btn_total_task.grid(row=7,column=0)


btn_exit_task = tkinter.Button(top, text="EXIT TASKS", fg="green" ,bg="white" , command =exit )
btn_exit_task.grid(row=8,column=0)

lb_tasks= tkinter.Listbox(top)
lb_tasks.grid(row=2,column=1,rowspan=7)




top.mainloop()
