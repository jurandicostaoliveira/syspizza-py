from tkinter import *
from functools import partial

class LoginForm:

    __tk = Tk()
    __labelLogin = None
    __inputLogin = None
    __buttonOk = None

    def index(self):
        self.labelLogin()
        self.inputLogin()
        self.buttonOk()

        self.__tk.title('Tela de Login')
        w = self.__tk.winfo_screenwidth()
        h = self.__tk.winfo_screenheight()
        y = 0
        x = 0

        self.__tk['bg'] = 'green'
        self.__tk.geometry('%dx%d+%d+%d' %(w,h,y,x))
        self.__tk.mainloop()

    def labelLogin(self):
        self.__labelLogin = Label(self.__tk, text='Login: ')
        self.__labelLogin.grid(row=0, column=0)

    def inputLogin(self):
        self.__inputLogin = Entry(self.__tk)
        self.__inputLogin.grid(row=0, column=1)

    def buttonOk(self):
        self.__buttonOk = Button(self.__tk, text="OK")
        self.__buttonOk['command'] = partial(self.btClick, self.__inputLogin)
        self.__buttonOk.grid(row=1, column=1)

    def btClick(self, value):
        self.__labelLogin['text'] = value.get()
        #print('lalalalal')



