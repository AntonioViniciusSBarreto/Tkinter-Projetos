from tkinter import *
from turtle import *
import math 

def fib_interface(tamanho):
   
    global entrada
    tamanho = int(entrada.get())


    seq_fib = [0,1]
    prox_num = seq_fib[-1] + seq_fib[-2]
    seq_fib.append(prox_num)

    for i in range(2,tamanho):
        prox_num = seq_fib[-1] + seq_fib[-2]
        seq_fib.append(prox_num)

    texto_sequencia["text"] = seq_fib


def fib_graf(tamanho):
    
    global entrada
    tamanho = int(entrada.get())
    a = 0
    b = 1
    quad_a = a
    quad_b = b

    lapis.pencolor("black")
    lapis.forward(b*fator)
    lapis.left(90)
    lapis.forward(b*fator)
    lapis.left(90)
    lapis.forward(b*fator)
    lapis.left(90)
    lapis.forward(b*fator)
   

    temp = quad_b
    quad_b = quad_b + quad_a
    quad_a = temp

    for i in range(1,tamanho):
        lapis.backward(quad_a*fator)
        lapis.right(90)
        lapis.forward(quad_b*fator)
        lapis.left(90)
        lapis.forward(quad_b*fator)
        lapis.left(90)
        lapis.forward(quad_b*fator)

    
        temp = quad_b
        quad_b = quad_b + quad_a
        quad_a = temp

    lapis.penup()
    lapis.setposition(fator,0)
    lapis.seth(0)
    lapis.pendown()

    lapis.left(90)
    for i in range(tamanho):
        print(b)
        fdwd = math.pi * b * fator/2
        fdwd /= 90
        for j in range(90):
            lapis.forward(fdwd)
            lapis.left(1)
        temp = a
        a = b
        b = temp + b
        
    
 
janela = Tk()
janela.title("Sequência Fibonacci")

texto_orintacao = Label(janela, text="Insira o tamanho desejado para sequência Fibonacci")
texto_orintacao.pack()

entrada = Entry()
entrada.pack()
entrada.focus_set()

botao_fib = Button(janela, text="Construir sequência", command= lambda: fib_interface(entrada))
botao_fib.pack()

texto_sequencia = Label(janela,text="")
texto_sequencia.pack()

lapis = Turtle()
lapis.speed(200)
fator = 1
botaoClicado = 1
botao_graf = Button(janela, text="Ver gráfico", command=lambda:fib_graf(entrada))
botao_graf.pack()

lista_objetos =[texto_orintacao,texto_sequencia,entrada, botao_fib, botao_graf]

janela.columnconfigure(index = 0, weight= 1)
linha = 0

for objeto in lista_objetos:
     janela.rowconfigure(linha, weight= 1)
     linha += 1

janela.mainloop()