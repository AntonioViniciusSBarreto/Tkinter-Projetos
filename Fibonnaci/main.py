from tkinter import *

def fib(tamanho):
   
    global entrada
    tamanho = int(entrada.get())

    seq_fib = [0,1]

    for i in range(2,tamanho):
        prox_num = seq_fib[-1] + seq_fib[-2]
        seq_fib.append(prox_num)

    texto_sequencia["text"] = seq_fib


janela = Tk()
janela.title("Sequência Fibonacci")

texto_orintacao = Label(janela, text="Insira o tamanho desejado para sequência Fibonacci")
texto_orintacao.pack()

entrada = Entry()
entrada.pack()
entrada.focus_set()

botao_fib = Button(janela, text="Construir sequência", command= lambda: fib(entrada))
botao_fib.pack()

texto_sequencia = Label(janela,text="")
texto_sequencia.pack()

botao_graf = Button(janela, text="Ver gráfico")
botao_graf.pack()

lista_objetos =[texto_orintacao,texto_sequencia,entrada, botao_fib, botao_graf]

janela.columnconfigure(index = 0, weight= 2)
linha = 0

for objeto in lista_objetos:
     janela.rowconfigure(linha, weight= 2)
     linha += 1

janela.mainloop()