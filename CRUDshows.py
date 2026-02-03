shows = []

def cadastrar_show():
    artista = input("Artista/Banda: ")
    data = input("Data do show: ")
    shows.append({"artista": artista, "data": data})
    print("Show cadastrado!")

def listar_shows():
    for s in shows:
        print(s)

def excluir_show():
    artista = input("Artista do show a excluir: ")
    for s in shows:
        if s["artista"] == artista:
            shows.remove(s)
            print("Show removido!")
            return
    print("Show não encontrado.")

cadastrar_show()
listar_shows()
excluir_show()