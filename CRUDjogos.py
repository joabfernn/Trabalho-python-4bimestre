jogos = []

def cadastrar_jogo():
    jogo = input("Nome do jogo (ex: Flamengo x Vasco): ")
    data = input("Data: ")
    jogos.append({"jogo": jogo, "data": data})
    print("Jogo cadastrado!")

def listar_jogos():
    for j in jogos:
        print(j)

def excluir_jogo():
    jogo = input("Nome do jogo a excluir: ")
    for j in jogos:
        if j["jogo"] == jogo:
            jogos.remove(j)
            print("Jogo removido!")
            return
    print("Jogo não encontrado.")

cadastrar_jogo()
listar_jogos()
excluir_jogo()

