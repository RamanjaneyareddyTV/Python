# import tkinter 
# m = tkinter.Tk() 
# m.mainloop()
# import tkinter as tk 
# r = tk.Tk() 
# r.title('venkat tkinter') 
# b = tk.Button(r, text='Stop', width=25, command=r.destroy) 
# b.pack()
# r.mainloop()
# ckeckbutton 
# from tkinter import *
# master = Tk() 
# var1 = IntVar() 
# a=Checkbutton(master, text='male', variable=var1).grid(sticky=W)
# var2 = IntVar() 
# b=Checkbutton(master, text='female', variable=var2).grid(sticky=W)

# mainloop()


# entry label 
# from tkinter import *
# master = Tk() 
# Label(master, text='First Name').grid(row=0) 
# Label(master, text='Last Name').grid(row=1) 
# e1 = Entry(master) 
# e2 = Entry(master) 
# e1.grid(row=0, column=1) 
# e2.grid(row=1, column=1) 
# mainloop() 






#radio Button
# from tkinter import *
# root = Tk() 
# v = IntVar() 
# Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W) 
# Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W) 
# mainloop() 




# from tkinter import *
# master = Tk() 
# w = Scale(master, from_=0, to=42) 
# w.pack() 
# w = Scale(master, from_=0, to=200, orient=HORIZONTAL) 
# w.pack() 
# mainloop() 

# from tkinter import *
# root = Tk() 
# scrollbar = Scrollbar(root) 
# scrollbar.pack( side = RIGHT, fill = Y ) 

# mainloop()





# from tkinter import *
# master = Tk() 
# w = Spinbox(master, from_ = 0, to = 10) 
# w.pack() 
# mainloop() 





# from tkinter import *
# from functools import partial

# def validateLogin(username, password):
# 	print("username entered :", username.get())
# 	print("password entered :", password.get())
# 	return

# #window
# tkWindow = Tk()  
# tkWindow.geometry('400x600')  
# tkWindow.title('Tkinter Login Form-pythonlife')

# #username label and text entry box
# usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
# username = StringVar()
# usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

# #password label and password entry box
# passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
# password = StringVar()
# passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

# validateLogin = partial(validateLogin, username, password)

# #login button
# loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

# tkWindow.mainloop()

# python
# oops-in-python
# webscraping
# opencv
# gui-programming(tkinter)
# vs-code
# github
# pandas
# matplotlib
# seaborn
# Mysql with python