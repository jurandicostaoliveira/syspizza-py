from app.view.layout import Layout
from tkinter import *

class Home(Layout):

    __topFrame = None
    __sidebarFrame = None
    __centerFrame = None

    def __init__(self):
        self.__topFrame = self.getTopFrame()
        self.__sidebarFrame = self.getSidebarFrame()
        self.__centerFrame = self.getCenterFrame()

    def index(self):
        self.setTitle('Testando')
        Label(self.__topFrame, text="Painel", font=('Arial', 14), fg='red', bg='green').grid(row=0, column=0, pady=0, padx=0)
        Entry(self.__topFrame, width=400).grid(row=0, column=1, pady=0, padx=0)
        Label(self.__sidebarFrame, text="Menu de navegação").grid(row=0, column=0)
        Label(self.__centerFrame, text='lalala').grid(row=0, column=0)
        self.run()


h = Home()
h.index()