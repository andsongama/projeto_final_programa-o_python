import tkinter

class appimc_tk(tkinter.Tk):
 def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

 def initialize(self):
     self.grid()

    #titulo
     titulo = tkinter.Label(self, text="Índice de massa corporal",font=("Arial 14 bold"),anchor="center", fg="black" ,bg="white")
     titulo.grid(column=0,row=0,columnspan=2, sticky='EW')
     espaco = tkinter.Label(self, text="",anchor="center",bg="white")
     espaco.grid(column=0, row=1, columnspan=2, sticky='EW')

     #Configuração do layout
     peso=tkinter.Label(self,text="Peso (Kg): ", font=("Times 12"),anchor="w",fg="black" ,bg="white")
     peso.grid(column=0, row=2, columnspan=1, sticky='EW')

     altura = tkinter.Label(self, text="Altura (m): ", font=("Times 12"),anchor="w", fg="black",bg="white")
     altura.grid(column=0, row=3, columnspan=1, sticky='EW')
     espaco1 = tkinter.Label(self, text="", anchor="center", bg="white")
     espaco1.grid(column=0, row=4, columnspan=2, sticky='EW')

    # Dados
     self.kg = tkinter.DoubleVar()
     quilos = tkinter.Entry(self, textvariable=self.kg)
     quilos.grid(column=1, row=2, sticky='EW')

     self.mt = tkinter.DoubleVar()
     metros = tkinter.Entry(self, textvariable=self.mt)
     metros.grid(column=1, row=3, sticky='EW')

    #Botão
     btn = tkinter.Button (self, text="Saiba o seu IMC clicando aqui",command=self.btnclick)
     btn.grid(column=0,row=5,columnspan=2)

     self.rimc = tkinter.StringVar()
     resultado = tkinter.Label(self, textvariable=self.rimc)
     resultado.grid(column=1, row=6, sticky='EW')
     textoresultado = tkinter.Label(self, textvariable=self,text="Seu Índice de Massa Corporal é ")
     textoresultado.grid(column=0, row=6, sticky='EW')

     self.grid_columnconfigure(0, weight=1)
     self.resizable(True, True)

 def btnclick(self):
     p = self.kg.get()
     a = self.mt.get()
     e=a*a
     mpg =(p/e)
     return self.rimc.set(mpg)

if __name__ == "__main__":
     app = appimc_tk(None)
     app.title('Calculadora do índice de'
               ' massa corporal (IMC)')

app.mainloop()