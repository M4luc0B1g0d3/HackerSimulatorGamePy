from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import time
import threading

class Compartilhar:
    def __init__(self):
        self.dinheiro = 0
        self.nivel = 0

share = Compartilhar()

class Janela:
    def __init__(self, dados):
        self.root = Tk()
        self.root.title('Hacker Simulator')
        self.root.geometry('800x500')
        self.dados = dados



        Button(self.root, text='Hackear Arvores', command=self.step,width=30).grid(row=0, column=0, padx=10, pady=10)
        self.pb = Progressbar(self.root, length=300, mode='determinate')
        self.pb.grid(row=0, column=1)
        Label(self.root, text='2s').grid(row=0, column=2, padx=10, pady=10)

        self.money = Label(self.root, text=self.dados.dinheiro)
        self.money.grid(row=0, column=3, padx=5)
        Label(self.root, text='Reais').grid(row=0, column=4, padx=10)

        Button(self.root, text='Mercadão da deep webs', command=self.comprar, width=30).grid(row=800, column=0, padx=10, pady=10)
        self.att()

        self.root.mainloop()

    def step(self):
        for i in range(2):
            self.root.update_idletasks()
            self.pb['value'] += 50

            time.sleep(1)

        if self.pb['value'] == 100:
            self.dados.dinheiro += 5
            #print(self.dinheiro)
            self.money['text'] = self.dados.dinheiro
            self.pb['value'] = 0

    def step1(self):
        for i in range(4):
            self.root.update_idletasks()
            self.pb1['value'] += 25

            time.sleep(1)

        if self.pb1['value'] == 100:
            self.dados.dinheiro += 8
            #print(self.dinheiro)
            self.money['text'] = self.dados.dinheiro
            self.pb1['value'] = 0

    def step2(self):
        for i in range(5):
            self.root.update_idletasks()
            self.pb2['value'] += 20

            time.sleep(1)

        if self.pb2['value'] == 100:
            self.dados.dinheiro += 15
            #print(self.dinheiro)
            self.money['text'] = self.dados.dinheiro
            self.pb2['value'] = 0

#100/20 = 20s (ou seja se o valor for igual a 1 é 20 segundos)
    def step3(self):
        for i in range(7):
            self.root.update_idletasks()
            self.pb3['value'] += 15

            time.sleep(1)

        if self.pb3['value'] == 100:
            self.dados.dinheiro += 25
            #print(self.dinheiro)
            self.money['text'] = self.dados.dinheiro
            self.pb3['value'] = 0

    def step4(self):
        for i in range(10):
            self.root.update_idletasks()
            self.pb4['value'] += 10

            time.sleep(1)

        if self.pb4['value'] == 100:
            self.dados.dinheiro += 60
            #print(self.dinheiro)
            self.money['text'] = self.dados.dinheiro
            self.pb4['value'] = 0

    def step5(self):
        for i in range(13):
            self.root.update_idletasks()
            self.pb5['value'] += 8

            time.sleep(1)

        if self.pb5['value'] == 100:
            self.dados.dinheiro += 100
            #print(self.dinheiro)
            self.money['text'] = self.dados.dinheiro
            self.pb5['value'] = 0

    def step6(self):
        for i in range(15):
            self.root.update_idletasks()
            self.pb6['value'] += 7

            time.sleep(1)

        if self.pb6['value'] == 100:
            self.dados.dinheiro += 250
            #print(self.dinheiro)
            self.money['text'] = self.dados.dinheiro
            self.pb6['value'] = 0

    def step7(self):
        for i in range(20):
            self.root.update_idletasks()
            self.pb7['value'] += 5

            time.sleep(1)

        if self.pb7['value'] == 100:
            self.dados.dinheiro += 400
            #print(self.dinheiro)
            self.money['text'] = self.dados.dinheiro
            self.pb7['value'] = 0

    def step8(self):
        for i in range(25):
            self.root.update_idletasks()
            self.pb8['value'] += 4

            time.sleep(1)

        if self.pb8['value'] == 100:
            self.dados.dinheiro += 750
            #print(self.dinheiro)
            self.money['text'] = self.dados.dinheiro
            self.pb8['value'] = 0

    def step9(self):
        for i in range(33.4):
            self.root.update_idletasks()
            self.pb9['value'] += 3

            time.sleep(1)

        if self.pb9['value'] == 100:
            self.dados.dinheiro += 1000
            #print(self.dinheiro)
            self.money['text'] = self.dados.dinheiro
            self.pb9['value'] = 0

    def step10(self):
        for i in range(50):
            self.root.update_idletasks()
            self.pb10['value'] += 0.5

            time.sleep(1)

        if self.pb10['value'] == 100:
            self.dados.dinheiro += 100000
            #print(self.dinheiro)
            self.money['text'] = self.dados.dinheiro
            self.pb10['value'] = 0

    def play2(self):
            self.dados.dinheiro += 10
            #print(self.dinheiro)
            self.money['text'] = self.dados.dinheiro

    def comprar(self):
        Loja(share)


    def atualizar(self):
        while True:
            if self.dados.nivel >= 1:
                Button(self.root, text='Passar trote', command=self.step1, width=30).grid(row=1, column=0, padx=10,
                                                                                          pady=10)
                self.pb1 = Progressbar(self.root, length=300, mode='determinate')
                self.pb1.grid(row=1, column=1)
                Label(self.root, text='8 reais').grid(row=1, column=2, padx=10, pady=10)

            if self.dados.nivel >= 2:
                Button(self.root, text='Fazer ligações e desligar quando alguem atende', command=self.step2,
                       width=30).grid(row=2, column=0, padx=10, pady=10)
                self.pb2 = Progressbar(self.root, length=300, mode='determinate')
                self.pb2.grid(row=2, column=1)
                Label(self.root, text='15 reais').grid(row=2, column=2, padx=10, pady=10)

            if self.dados.nivel >= 3:
                Button(self.root, text='Ameaçar vender o notebook em uma loja', command=self.step3,
                       width=30).grid(row=3, column=0, padx=10, pady=10)
                self.pb3 = Progressbar(self.root, length=300, mode='determinate')
                self.pb3.grid(row=3, column=1)
                Label(self.root, text='25 reais').grid(row=3, column=2, padx=10, pady=10)

            if self.dados.nivel >= 4:
                Button(self.root, text='Espalhar spans por emails', command=self.step4,
                       width=30).grid(row=4, column=0, padx=10, pady=10)
                self.pb4 = Progressbar(self.root, length=300, mode='determinate')
                self.pb4.grid(row=4, column=1)
                Label(self.root, text='60 reais').grid(row=4, column=2, padx=10, pady=10)

            if self.dados.nivel >= 5:
                Button(self.root, text='Crackear o sistema operacional janelas 9', command=self.step5,
                       width=30).grid(row=5, column=0, padx=10, pady=10)
                self.pb5 = Progressbar(self.root, length=300, mode='determinate')
                self.pb5.grid(row=5, column=1)
                Label(self.root, text='100 reais').grid(row=5, column=2, padx=10, pady=10)

            if self.dados.nivel >= 6:
                Button(self.root, text='Entrar no sistema da prefeitura e desviar dinheiro', command=self.step6,
                       width=30).grid(row=6, column=0, padx=10, pady=10)
                self.pb6 = Progressbar(self.root, length=300, mode='determinate')
                self.pb6.grid(row=6, column=1)
                Label(self.root, text='250 reais').grid(row=6, column=2, padx=10, pady=10)

            if self.dados.nivel >= 7:
                Button(self.root, text='Vender hacks de jogos famosos', command=self.step7,
                       width=30).grid(row=7, column=0, padx=10, pady=10)
                self.pb7 = Progressbar(self.root, length=300, mode='determinate')
                self.pb7.grid(row=7, column=1)
                Label(self.root, text='400 reais').grid(row=7, column=2, padx=10, pady=10)

                Button(self.root, text='Vender jogos de ps2 3 por 10', command=self.play2,
                       width=30).grid(row=7, column=5, padx=10, pady=10)
                Label(self.root, text='10 reais').grid(row=7, column=2, padx=10, pady=10)

            if self.dados.nivel >= 8:
                Button(self.root, text='Invadir sistemas complexos', command=self.step8,
                       width=30).grid(row=8, column=0, padx=10, pady=10)
                self.pb8 = Progressbar(self.root, length=300, mode='determinate')
                self.pb8.grid(row=8, column=1)
                Label(self.root, text='750 reais').grid(row=8, column=2, padx=10, pady=10)

            if self.dados.nivel >= 9:
                Button(self.root, text='Hackear o banco central', command=self.step9,
                       width=30).grid(row=9, column=0, padx=10, pady=10)
                self.pb9 = Progressbar(self.root, length=300, mode='determinate')
                self.pb9.grid(row=9, column=1)
                Label(self.root, text='1000 reais').grid(row=9, column=2, padx=10, pady=10)

            if self.dados.nivel >= 10:
                Button(self.root, text='Quebrar o sistema de blockchains', command=self.step10,
                       width=30).grid(row=10, column=0, padx=10, pady=10)
                self.pb10 = Progressbar(self.root, length=300, mode='determinate')
                self.pb10.grid(row=10, column=1)
                Label(self.root, text='100000 reais').grid(row=10, column=2, padx=10, pady=10)


            print(self.dados.nivel)
            time.sleep(1)  # Aguarde 1 segundo


    def att(self):
        # Crie uma thread para executar a função
        thread = threading.Thread(target=self.atualizar)
        thread.daemon = True

        # Inicie a thread
        thread.start()

class Loja:
    def __init__(self, dados):
        self.dados = dados
        self.loja = Tk()
        self.loja.title('Loja Epica da Deeep Webb')
        self.loja.geometry('800x500')

        Label(self.loja, text='Radio da motorola, talvez não funcione, 50R$').grid(row=0,column=0)
        Button(self.loja, text='Comprar Radio', command=self.radio).grid(row=0, column=1)

        Label(self.loja, text='Celular da NOquiah tijolão, 200R$').grid(row=1, column=0)
        Button(self.loja, text='Comprar celular', command=self.noquiah).grid(row=1, column=1)

        Label(self.loja, text='Lepitopi da xixa, 500R$').grid(row=2, column=0)
        Button(self.loja, text='Comprar lepitopi', command=self.xixa).grid(row=2, column=1)

        Label(self.loja, text='Celular com android, 800R$').grid(row=3, column=0)
        Button(self.loja, text='Comprar android', command=self.androidee).grid(row=3, column=1)

        Label(self.loja, text='Nótibooqui Negativo, 1500R$').grid(row=4, column=0)
        Button(self.loja, text='Comprar nótiboqui',command=self.negativo).grid(row=4, column=1)

        Label(self.loja, text='Nótiboki em promoção nas casas paraibas, 2000R$').grid(row=5, column=0)
        Button(self.loja, text='Comprar nótiboki', command=self.paraiba).grid(row=5, column=1)

        Label(self.loja, text='Pc da brecky fraude, 3000R$').grid(row=6, column=0)
        Button(self.loja, text='Comprar pc', command=self.fraude).grid(row=6, column=1)

        Label(self.loja, text='Pc medio, 5000R$').grid(row=7, column=0)
        Button(self.loja, text='Comprar Pc medio', command=self.medio).grid(row=7, column=1)

        Label(self.loja, text='Pc da NASA, 10000R$').grid(row=8, column=0)
        Button(self.loja, text='Comprar PC DA NASA', command=self.nasa).grid(row=8, column=1)

        Label(self.loja, text='Pc Quantico, 100000R$').grid(row=9, column=0)
        Button(self.loja, text='Comprar PC Quantico', command=self.quantico).grid(row=9, column=1)

        self.money = Label(self.loja, text=self.dados.dinheiro)
        self.money.grid(row=0, column=2, padx=10)

        self.attloja()


        self.loja.mainloop()

    def radio(self):
        if self.dados.dinheiro >= 50 and self.dados.nivel == 0:
                self.dados.nivel += 1
                self.dados.dinheiro -= 50
        elif self.dados.dinheiro < 50:
            messagebox.showinfo('Pobre', 'Vc não tem dinheiro, vai hacker mais para parar de ser pobre')
        else:
            messagebox.showinfo('Tu ja tem', 'Tu já tem esse bagulho, vai comprar algo diferente')

    def noquiah(self):
        if self.dados.dinheiro >= 200 and self.dados.nivel == 1:
            self.dados.nivel += 1
            self.dados.dinheiro -= 200
        elif self.dados.dinheiro < 200:
            messagebox.showinfo('Pobre', 'Vc não tem dinheiro, vai hacker mais para parar de ser pobre')
        elif self.dados.nivel >= 1:
            messagebox.showinfo('Tu ja tem', 'Tu já tem esse bagulho, vai comprar algo diferente')
        else:
            messagebox.showinfo('Ué', 'Compra o item anterior antes doidão')

    def xixa(self):
        if self.dados.dinheiro >= 500 and self.dados.nivel == 2:
            self.dados.nivel += 1
            self.dados.dinheiro -= 500
        elif self.dados.dinheiro < 500:
            messagebox.showinfo('Pobre', 'Vc não tem dinheiro, vai hacker mais para parar de ser pobre')
        elif self.dados.nivel >= 1:
            messagebox.showinfo('Tu ja tem', 'Tu já tem esse bagulho, vai comprar algo diferente')
        else:
            messagebox.showinfo('Ué', 'Compra o item anterior antes doidão')

    def androidee(self):

        if self.dados.dinheiro >= 800 and self.dados.nivel == 3:
            self.dados.nivel += 1
            self.dados.dinheiro -= 800
        elif self.dados.dinheiro < 800:
            messagebox.showinfo('Pobre', 'Vc não tem dinheiro, vai hacker mais para parar de ser pobre')
        elif self.dados.nivel >= 1:
            messagebox.showinfo('Tu ja tem', 'Tu já tem esse bagulho, vai comprar algo diferente')
        else:
            messagebox.showinfo('Ué', 'Compra o item anterior antes doidão')

    def negativo(self):
        if self.dados.dinheiro >= 1500 and self.dados.nivel == 4:
            self.dados.nivel += 1
            self.dados.dinheiro -= 1500
        elif self.dados.dinheiro < 1500:
            messagebox.showinfo('Pobre', 'Vc não tem dinheiro, vai hacker mais para parar de ser pobre')
        elif self.dados.nivel >= 1:
            messagebox.showinfo('Tu ja tem', 'Tu já tem esse bagulho, vai comprar algo diferente')
        else:
            messagebox.showinfo('Ué', 'Compra o item anterior antes doidão')

    def paraiba(self):
        if self.dados.dinheiro >= 2000 and self.dados.nivel == 5:
            self.dados.nivel += 1
            self.dados.dinheiro -= 2000
        elif self.dados.dinheiro < 2000:
            messagebox.showinfo('Pobre', 'Vc não tem dinheiro, vai hacker mais para parar de ser pobre')
        elif self.dados.nivel >= 1:
            messagebox.showinfo('Tu ja tem', 'Tu já tem esse bagulho, vai comprar algo diferente')
        else:
            messagebox.showinfo('Ué', 'Compra o item anterior antes doidão')

    def fraude(self):
        if self.dados.dinheiro >= 3000 and self.dados.nivel == 6:
            self.dados.nivel += 1
            self.dados.dinheiro -= 3000
        elif self.dados.dinheiro < 3000:
            messagebox.showinfo('Pobre', 'Vc não tem dinheiro, vai hacker mais para parar de ser pobre')
        elif self.dados.nivel >= 1:
            messagebox.showinfo('Tu ja tem', 'Tu já tem esse bagulho, vai comprar algo diferente')
        else:
            messagebox.showinfo('Ué', 'Compra o item anterior antes doidão')

    def medio(self):
        if self.dados.dinheiro >= 5000 and self.dados.nivel == 7:
            self.dados.nivel += 1
            self.dados.dinheiro -= 5000
        elif self.dados.dinheiro < 5000:
            messagebox.showinfo('Pobre', 'Vc não tem dinheiro, vai hacker mais para parar de ser pobre')
        elif self.dados.nivel >= 1:
            messagebox.showinfo('Tu ja tem', 'Tu já tem esse bagulho, vai comprar algo diferente')
        else:
            messagebox.showinfo('Ué', 'Compra o item anterior antes doidão')

    def nasa(self):
        if self.dados.dinheiro >= 10000 and self.dados.nivel == 8:
            self.dados.nivel += 1
            self.dados.dinheiro -= 10000
        elif self.dados.dinheiro < 10000:
            messagebox.showinfo('Pobre', 'Vc não tem dinheiro, vai hacker mais para parar de ser pobre')
        elif self.dados.nivel >= 1:
            messagebox.showinfo('Tu ja tem', 'Tu já tem esse bagulho, vai comprar algo diferente')
        else:
            messagebox.showinfo('Ué', 'Compra o item anterior antes doidão')

    def quantico(self):
        if self.dados.dinheiro >= 100000 and self.dados.nivel == 9:
            self.dados.nivel += 1
            self.dados.dinheiro -= 100000
        elif self.dados.dinheiro < 100000:
            messagebox.showinfo('Pobre', 'Vc não tem dinheiro, vai hacker mais para parar de ser pobre')
        elif self.dados.nivel >= 1:
            messagebox.showinfo('Tu ja tem', 'Tu já tem esse bagulho, vai comprar algo diferente')
        else:
            messagebox.showinfo('Ué', 'Compra o item anterior antes doidão')



    def atualizarloja(self):
        while True:
            self.money['text'] = self.dados.dinheiro
            time.sleep(1)  # Aguarde 1 segundo

    def attloja(self):
        # Crie uma thread para executar a função
        thread = threading.Thread(target=self.atualizarloja)
        thread.daemon = True


        # Inicie a thread
        thread.start()


Janela(share)