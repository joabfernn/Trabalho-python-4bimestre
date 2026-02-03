ingressos = []

def vender_ingresso():
    cpf = input("CPF do torcedor: ")
    evento = input("Evento (jogo ou show): ")
    tipo = input("Tipo (Jogo/Show): ")

    ingressos.append({
        "cpf": cpf,
        "evento": evento,
        "tipo": tipo
    })

    print("Ingresso vendido com sucesso!")

def listar_ingressos():
    for i in ingressos:
        print(i)

vender_ingresso()
listar_ingressos()
