from tkinter import *


class Layout:
    __tk = Tk()
    __width = __tk.winfo_screenwidth()
    __height = __tk.winfo_screenheight()
    __y = 0
    __x = 0
    __title = 'Control Panel'
    __topFrame = None
    __sidebarFrame = None
    __centerFrame = None

    def setTitle(self, title):
        self.__title = title
        return self

    def getTopFrame(self):
        if (self.__topFrame == None):
            self.__topFrame = Frame(self.__tk, bg='green', width=self.__width, height=150).grid(row=0, column=0,
                                                                                                columnspan=2)
        return self.__topFrame

    def getSidebarFrame(self):
        if (self.__sidebarFrame == None):
            height = self.__height - 150
            self.__sidebarFrame = Frame(self.__tk, bg='blue', width=300, height=height).grid(row=1, column=0)

        return self.__sidebarFrame

    def getCenterFrame(self):
        if (self.__centerFrame == None):
            width = self.__width - 300
            height = self.__height - 150
            self.__centerFrame = Frame(self.__tk, bg='cyan', width=width, height=height).grid(row=1, column=1)

        return self.__centerFrame

    def run(self):
        self.__tk.title(self.__title)
        self.__tk.geometry('%dx%d+%d+%d' % (self.__width, self.__height, self.__y, self.__x))
        self.__tk.mainloop()
