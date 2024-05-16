from tkinter import*
from tkinter import messagebox
from PIL import ImageTk

def login():
   if usernameEntry.get()=='' or passwordEntry.get()=='':
       messagebox.showerror('Error','Fields cannot be empty')
   elif usernameEntry.get()=='a' and passwordEntry.get()=='a':
       messagebox.showinfo('Success','Welcome Asif Alim')
       window.destroy()
       import sms
   else:messagebox.showerror('Error','Please provide correct info')

window=Tk()
window.geometry('1200x700+0+0')
window.title('login system of student management system')
window.resizable(False,False)
background=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(window,image=background)
bgLabel.place(x=0,y=0)

loginFrame=Frame(window,bg='white')
loginFrame.place(x=400,y=150)
logoImage=PhotoImage(file='logo.png')
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

usernameImage=PhotoImage(file='user.png')
usernameLabel=Label(loginFrame,image=usernameImage,text='Username',compound=LEFT
                    ,font=('times new roman',20,'bold'),bg='white')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)
usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,pady=10,padx=20 )

passwordImage=PhotoImage(file='password.png')
passwordLabel=Label(loginFrame,image=passwordImage,text='Password',compound=LEFT
                    ,font=('times new roman',20,'bold'),bg='white')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)
passwordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
passwordEntry.grid(row=2,column=1,pady=10,padx=20 )

loginButton=Button(loginFrame,text='login',font=('times new roman',15,'bold'),width=15
                   ,fg='white',bg='cornflowerblue',activebackground='cornflowerblue',
                   activeforeground='white',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)


window.mainloop()