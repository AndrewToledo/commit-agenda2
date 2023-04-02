from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox

from dados import *

# cores -----------------------------
co0 = "#f0f3f5"  # Preta
co1 = "#f0f3f5"  # cizenta / grey
co2 = "#feffff"  # branca
co3 = "#38576b"  # preta / black
co4 = "#403d3d"   # letra
co5 = "#6f9fbd"  # azul
co6 = "#ef5350"   # vermelha
co7 = "#93cd95"   # verde

# criando janela ----------------------

janela = Tk()
janela.title("")
janela.geometry("500x500")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use('clam')

############################ Frames #########################

frame_acima = Frame(janela, width=500, height=50, bg=co3, relief='flat')
frame_acima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=500, height=150, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_tabela = Frame(janela, width=500, height=100, bg=co2, relief='flat')
frame_tabela.grid(row=2, column=0, columnspan=2, padx=10, pady=1, sticky=NW)


# configurando frame cima

l_nome = Label(frame_acima, text="Agenda Telefonica", anchor=NE,
               font=("arial 20 bold"), bg=co3, fg=co1)
l_nome.place(x=5, y=5)


l_linha = Label(frame_acima, text=" ", width=500,
                anchor=NE, font=("arial 1"), bg=co2, fg=co1)
l_linha.place(x=0, y=46)


def mostrar_dados():

    global tree
    dados_h = ["Nome", "Sexo", "Telefone", "Email"]

    dados = ver_dados()

    tree = ttk.Treeview(frame_tabela, selectmode="extended",
                        columns=dados_h, show="headings")

    # Vertical scrollbar
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)

    # Horizontal scrollbar
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky="nsew")
    vsb.grid(column=1, row=0, sticky="ns")
    hsb.grid(column=0, row=1, sticky="ew")

    # tree cabecalho
    tree.heading(0, text="Nome", anchor=NW)
    tree.heading(1, text="Sexo", anchor=NW)
    tree.heading(2, text="Telefone", anchor=NW)
    tree.heading(3, text="Email", anchor=NW)

    # tree corpo
    tree.column(0, width=120, anchor="nw")
    tree.column(1, width=50, anchor="nw")
    tree.column(2, width=100, anchor="nw")
    tree.column(3, width=120, anchor="nw")

    for item in dados:
        tree.insert("", "end", values=item)


mostrar_dados()

# função inserir


def inserir():
    nome = e_nome.get()
    sexo = c_sexo.get()
    telefone = e_tel.get()
    email = e_email.get()

    dados = [nome, sexo, telefone, email]

    if nome == "" or sexo == "" or telefone == "" or email == "":
        messagebox.showwarning("Dados", "Por favor preencha todos os campos")
    else:
        adicionar_dados(dados)
        messagebox.showwarning(
            "Dados", "Os dados foram adicionados com sucesso")

        e_nome.delete(0, "end")
        c_sexo.delete(0, "end")
        e_tel.delete(0, "end")
        e_email.delete(0, "end")

    mostrar_dados()


# Atualizar
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        nome = str(treev_lista[0])
        sexo = str(treev_lista[1])
        telefone = str(treev_lista[2])
        email = str(treev_lista[3])

        e_nome.insert(0, nome)
        c_sexo.insert(0, sexo)
        e_tel.insert(0, telefone)
        e_email.insert(0, email)

        def confirmar():
            novo_nome = e_nome.get()
            novo_sexo = c_sexo.get()
            novo_telefone = e_tel.get()
            novo_email = e_email.get()

            dados = [telefone, novo_nome, novo_sexo, novo_telefone, novo_email]

            atualizar_dados(dados)

            messagebox.showinfo(
                'Sucesso', 'Os dados foram atualizados com sucesso')

            e_nome.delete(0, 'end')
            c_sexo.delete(0, 'end')
            e_tel.delete(0, 'end')
            e_email.delete(0, 'end')

            for widget in frame_tabela.winfo_children():
                widget.destroy()

            b_confirmar.destroy()

            mostrar_dados()

        b_confirmar = Button(frame_baixo, command=confirmar, text="Confirmar", width=10,
                             height=1, bg=co2, fg=co4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
        b_confirmar.place(x=290, y=110)

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')


# Remover
def remover():

    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = str(treev_lista[2])

        remover_dados(valor)

        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        mostrar_dados()

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')


def procurar():
    telefone = e_procurar.get()

    dados = procurar_dados(telefone)

    def delete_command():
        tree.delete(*tree.get_children())

    delete_command()

    for item in dados:
        tree.insert('', 'end', values=item)

    e_procurar.delete(0, "end")


# configurando frame baixo

l_nome = Label(frame_baixo, text="Nome *", anchor=NE,
               font=('Ivy 10 '), bg=co1, fg=co4)
l_nome.place(x=10, y=20)

e_nome = Entry(frame_baixo, width=25, justify='left', font=(
    "", 10), highlightthickness=1,)
e_nome.place(x=80, y=20)

l_sexo = Label(frame_baixo, text="Sexo *", anchor=NE,
               font=("Ivy 10 bold"), bg=co1, fg=co4)
l_sexo.place(x=10, y=75)

c_sexo = Combobox(frame_baixo, width=27)
c_sexo["value"] = ("", "F", "M")
c_sexo.place(x=80, y=75)


l_tel = Label(frame_baixo, text="Telefone*", anchor=NE,
              font=("Ivy 10 bold"), bg=co1, fg=co4)
l_tel.place(x=10, y=95)

e_tel = Entry(frame_baixo, width=25, justify="left",
              font=("", 10), highlightthickness=1,)
e_tel.place(x=80, y=95)


l_email = Label(frame_baixo, text="Email *", anchor=NE,
                font=("Ivy 10 bold"), bg=co1, fg=co4)
l_email.place(x=10, y=50)

e_email = Entry(frame_baixo, width=25, justify="left",
                font=("", 10), highlightthickness=1,)
e_email.place(x=80, y=50)


b_procurar = Button(frame_baixo, command=procurar, text="Procurar", anchor=NE,
                    font=("Ivy 8 bold"), bg=co1, fg=co4, relief=RAISED, overrelief=RIDGE)
b_procurar.place(x=290, y=20)

b_procurar = Entry(frame_baixo, width=16, justify="left",
                   font=("", 11), highlightthickness=1,)
b_procurar.place(x=347, y=21)


b_ver = Button(frame_baixo, command=mostrar_dados, text="Ver dados", width=10, font=(
    "Ivy 8 bold"), bg=co2, fg=co4, relief=RAISED, overrelief=RIDGE)
b_ver.place(x=290, y=50)

b_adicionar = Button(frame_baixo, command=inserir, text="Adicionar", width=10,
                     font=("Ivy 8 bold"), bg=co2, fg=co4, relief=RAISED, overrelief=RIDGE)
b_adicionar.place(x=400, y=50)

b_atualizar = Button(frame_baixo, command=atualizar, text="Atualizar", width=10,
                     font=("Ivy 8 bold"), bg=co2, fg=co4, relief=RAISED, overrelief=RIDGE)
b_atualizar.place(x=400, y=80)

b_deletar = Button(frame_baixo, command=remover, text="Deletar", width=10,
                   font=("Ivy 8 bold"), bg=co2, fg=co4, relief=RAISED, overrelief=RIDGE)
b_deletar.place(x=400, y=110)


janela.mainloop()
