from tkinter import *

def conversor_numerico(escolha):
   global num
   numero = int(num.get())
   if escolha == 1:
        numero = bin(numero)[2:]
   elif escolha == 2:
        numero = oct(numero)[2:]
   elif escolha == 3:
        numero = hex(numero)[2:]
   
   texto_convertido["text"] = numero
    

janela = Tk()
janela.title("Conversor de números")


texto_orientacao = Label(janela, text="Insira o numero que deseja ser convertido:")
texto_orientacao.grid(column=0, row=0, padx=5, pady=5)


num = Entry(janela)
num.grid(column=0, row=1, padx=5, pady=5)
num.focus_set()


botao_bin = Button(janela, text='Conversão Binária', command=lambda: conversor_numerico(1))
botao_oct = Button(janela, text='Conversão Octagonal', command=lambda: conversor_numerico(2))
botao_hex = Button(janela, text='Conversão Hexadecimal', command=lambda: conversor_numerico(3))

botao_bin.grid(column=0, row=2, padx=5, pady=5)
botao_oct.grid(column=0, row=3, padx=5, pady=5)
botao_hex.grid(column=0, row=4, padx=5, pady=5)

texto_convertido = Label(janela, text= "Número convertido irá aparecer aqui")
texto_convertido.grid(column=0,row=5, padx=5, pady=5)


lista_objetos = [texto_orientacao, num, botao_bin, botao_hex, botao_oct, texto_convertido]

janela.columnconfigure(index= 0,  weight= 1)
linha = 0
for objeto in lista_objetos:
     janela.rowconfigure(linha, weight= 1)
     linha += 1
    
janela.mainloop()