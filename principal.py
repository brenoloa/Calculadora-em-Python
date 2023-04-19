from tkinter import *
from tkinter import ttk
#cores

cor1 = '#1e1f1e'    # preto
cor2 = '#f0f1f2'    # branco
cor3 = '#0549b5'    # azul
cor4 = '#736767'    # cinza
cor5 = '#f7632d'    # laranja

#criação da janela
janela = Tk()
janela.title('Calculadora')
janela.geometry('235x330')
janela.config(bg=cor1)

#divisão de quadros dentro da janela
frame_tela = Frame(janela, width=235, height=50, bg=cor2)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268, bg=cor1)
frame_corpo.grid(row=1, column=0)

#variaveis
todos_valores = ''

# criando função
def entrar_valores(event):
    global todos_valores

    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)



#Criando Display
valor_texto = StringVar()
valor_texto.set('')
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7,
                  relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy', 17, 'bold'), bg=cor3, fg=cor2) #anchor = direção bussola
app_label.place(x=0, y=0)

def calcular():
    global  todos_valores
    resultado = str(eval(todos_valores))
    valor_texto.set(resultado)
    todos_valores = ''

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set('')
#BOTOES.
# -=-=-=-=-=
b_apagar = Button(frame_corpo,command = lambda: limpar_tela(),  text="C", width=11, height=2, bg=cor4, fg=cor2,
                  font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_apagar.place(x=0, y=0)
b_porc = Button(frame_corpo, command = lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor4, fg=cor2,
                font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_porc.place(x=118, y=0)
b_div = Button(frame_corpo, command = lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2,
               font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_div.place(x=177, y=0)
# -=-=-=-=-=
b_sete = Button(frame_corpo, command = lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor4, fg=cor2,
                font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_sete.place(x=0, y=52)
b_oito = Button(frame_corpo, command = lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor4, fg=cor2,
                font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_oito.place(x=59, y=52)
b_nove = Button(frame_corpo, command = lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor4, fg=cor2,
                font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_nove.place(x=118, y=52)
b_mult = Button(frame_corpo, command = lambda: entrar_valores('*'), text="x", width=5, height=2, bg=cor5, fg=cor2,
                font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_mult.place(x=177, y=52)
# -=-=-=-=-=
b_quatro = Button(frame_corpo, command = lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor4, fg=cor2,
                  font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_quatro.place(x=0, y=104)
b_cinco = Button(frame_corpo, command = lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor4, fg=cor2,
                 font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_cinco.place(x=59, y=104)
b_seis = Button(frame_corpo, command = lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor4, fg=cor2,
                font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_seis.place(x=118, y=104)
b_menos = Button(frame_corpo, command = lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2,
                 font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_menos.place(x=177, y=104)
# -=-=-=-=-=
b_um = Button(frame_corpo, command = lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cor4, fg=cor2,
              font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_um.place(x=0, y=156)
b_dois = Button(frame_corpo, command = lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor4, fg=cor2,
                font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_dois.place(x=59, y=156)
b_tres = Button(frame_corpo, command = lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor4, fg=cor2,
                font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_tres.place(x=118, y=156)
b_mais = Button(frame_corpo, command = lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2,
                font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_mais.place(x=177, y=156)
# -=-=-=-=-=-=-=
b_zero = Button(frame_corpo, command = lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cor4, fg=cor2,
                  font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_zero.place(x=0, y=208)
b_virg = Button(frame_corpo, command = lambda: entrar_valores('.'), text=",", width=5, height=2, bg=cor4, fg=cor2,
                font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_virg.place(x=118, y=208)
b_igual = Button(frame_corpo, command = lambda: calcular(), text="=", width=5, height=2, bg=cor5, fg=cor2,
               font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_igual.place(x=177, y=208)
## -=-=-=-=-=-=-=
texto = Text(janela, bg=cor1, fg=cor2, font=("Arial", 8, 'bold'))
texto.insert(INSERT, "Desenvolvido por Breno")
texto.place(x=0, y=310)
# -=-=-=-=-=-=-=



entrar_valores("")
janela.mainloop()
