import tkinter

raiz = None
janelas = []

def criar():
    last = len(janelas)
    janela = tkinter.Toplevel(raiz)
    janela.title("janela  {}".format(last))
    janelas.append(janela)

    if(last > 0):
        janelas[last -1].destroy()

def destruir():
    janelas.pop(0).destroy()

def principal():
    global raiz
    raiz = tkinter.Tk()
    bt_criar = tkinter.Button(raiz, text="criar", command=criar)
    bt_destruir = tkinter.Button(raiz, text="destruir", command=destruir)
    bt_criar.pack(side="left")
    bt_destruir.pack(side="right")

principal()
tkinter.mainloop()