import random
from tkinter import Tk, Label, Button, Entry, Listbox, messagebox

def mega_sena():
    return random.sample(range(1, 61), 6)

def quina():
    return random.sample(range(1, 81), 5)

def lotofacil():
    return random.sample(range(1, 26), 15)

def verificar_acertos(numeros_sorteados, numeros_usuario):
    acertos = len(set(numeros_sorteados).intersection(set(numeros_usuario)))
    return acertos

def jogar_loteria():
    
    tipo_selecionado = tipo_loteria.curselection()
    if not tipo_selecionado:
        messagebox.showerror("Erro", "Selecione um tipo de loteria válido")
        return
    
    tipo = tipo_loteria.get(tipo_selecionado[0])  
    
 
    if tipo == 'Mega Sena':
        numeros_sorteados = mega_sena()
    elif tipo == 'Quina':
        numeros_sorteados = quina()
    elif tipo == 'Lotofácil':
        numeros_sorteados = lotofacil()
    else:
        messagebox.showerror("Erro", "Selecione um tipo de loteria válido")
        return
    
    try:
        numeros_usuario = [int(num) for num in numeros_entry.get().split()]
        if len(numeros_usuario) != len(numeros_sorteados):
            raise ValueError("Quantidade incorreta de números")
        if not all(1 <= num <= (60 if tipo == 'Mega Sena' else 80 if tipo == 'Quina' else 25) for num in numeros_usuario):
            raise ValueError(f"Os números devem estar entre 1 e {60 if tipo == 'Mega Sena' else 80 if tipo == 'Quina' else 25}")
    except ValueError as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}")
        return

    acertos = verificar_acertos(numeros_sorteados, numeros_usuario)
    

    resultado = f"Números sorteados: {numeros_sorteados}\n" \
                f"Números do usuário: {numeros_usuario}\n" \
                f"Quantidade de acertos: {acertos}"
    
    if acertos == len(numeros_sorteados):
        resultado += "\nParabéns, você acertou todos os números!"

    messagebox.showinfo("Resultado", resultado)


root = Tk()
root.title("Simulador de Loteria")
root.config(bg="#f0f0f0")


def atualizar_entrada():
    tipo_selecionado = tipo_loteria.curselection()
    if tipo_selecionado:
        tipo = tipo_loteria.get(tipo_selecionado[0])
        if tipo == 'Mega Sena':
            label_instrucoes.config(text="Insira 6 números entre 1 e 60:")
        elif tipo == 'Quina':
            label_instrucoes.config(text="Insira 5 números entre 1 e 80:")
        elif tipo == 'Lotofácil':
            label_instrucoes.config(text="Insira 15 números entre 1 e 25:")


tipo_loteria = Listbox(root, height=3)
tipo_loteria.insert(1, "Mega Sena")
tipo_loteria.insert(2, "Quina")
tipo_loteria.insert(3, "Lotofácil")
tipo_loteria.pack(pady=10)

label_instrucoes = Label(root, text="Selecione o tipo de loteria", bg="#f0f0f0", font=("Arial", 12,"bold"))
label_instrucoes.pack(pady=10)

numeros_entry = Entry(root, font=("Arial", 12))
numeros_entry.pack(pady=10)

botao_jogar = Button(root, text="Jogar", bg="#7cfc00", fg="black", font=("Arial", 15, "bold"), command=jogar_loteria)
botao_jogar.pack(pady=10)


tipo_loteria.bind("<<ListboxSelect>>", lambda e: atualizar_entrada())

root.mainloop()
