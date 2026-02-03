torcedores = []

def cadastrar_torcedor():
    nome = input("Nome do torcedor: ")
    cpf = input("CPF: ")
    torcedores.append({"nome": nome, "cpf": cpf})
    print("Torcedor cadastrado com sucesso!")

def listar_torcedores():
    for t in torcedores:
        print(t)

def atualizar_torcedor():
    cpf = input("CPF do torcedor a atualizar: ")
    for t in torcedores:
        if t["cpf"] == cpf:
            t["nome"] = input("Novo nome: ")
            print("Torcedor atualizado!")
            return
    print("Torcedor não encontrado.")

def excluir_torcedor():
    cpf = input("CPF do torcedor a excluir: ")
    for t in torcedores:
        if t["cpf"] == cpf:
            torcedores.remove(t)
            print("Torcedor excluído!")
            return
    print("Torcedor não encontrado.")

cadastrar_torcedor()
listar_torcedores()
atualizar_torcedor()
excluir_torcedor()