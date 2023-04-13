import tkinter as tk

usuarios = []
def cadastrar_usuario():
    nome = nome_entry.get()
    email = email_entry.get()
    # Adiciona o usuário à lista
    usuarios.append({'nome': nome, 'email': email})
    # Limpa os campos de entrada
    nome_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    # Exibe uma mensagem de sucesso
    status_label.config(text="Usuário cadastrado com sucesso!")
    
def mostrar_usuarios():
    if not usuarios:
        status_label.config(text="Não há usuários cadastrados.")
    else:
        
        janela_usuarios = tk.Toplevel()
        janela_usuarios.title("Usuários cadastrados")
        
        quadro_usuarios = tk.Frame(janela_usuarios)
        quadro_usuarios.pack(padx=10, pady=10)
        
        for i, usuario in enumerate(usuarios):
            nome_label = tk.Label(quadro_usuarios, text=usuario['nome'])
            nome_label.grid(row=i, column=0, padx=5, pady=5)
            email_label = tk.Label(quadro_usuarios, text=usuario['email'])
            email_label.grid(row=i, column=1, padx=5, pady=5)

janela_principal = tk.Tk()
janela_principal.title("Cadastro de usuários")

nome_label = tk.Label(janela_principal, text="Nome:")
nome_label.grid(row=0, column=0, padx=5, pady=5)
nome_entry = tk.Entry(janela_principal)
nome_entry.grid(row=0, column=1, padx=5, pady=5)

email_label = tk.Label(janela_principal, text="Email:")
email_label.grid(row=1, column=0, padx=5, pady=5)
email_entry = tk.Entry(janela_principal)
email_entry.grid(row=1, column=1, padx=5, pady=5)

cadastrar_botao = tk.Button(janela_principal, text="Cadastrar", command=cadastrar_usuario)
cadastrar_botao.grid(row=2, column=0, padx=5, pady=5)

mostrar_botao = tk.Button(janela_principal, text="Mostrar usuários", command=mostrar_usuarios)
mostrar_botao.grid(row=2, column=1, padx=5, pady=5)

status_label = tk.Label(janela_principal, text="")
status_label.grid(row=3, column=0, columnspan=2)

janela_principal.mainloop()
