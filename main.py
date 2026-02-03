import CRUDtorcedor
import CRUDjogos
import CRUDshows
import vendaingresso

while True:
    print("\n=== SISTEMA DO ESTÁDIO ===")
    print("1 - Cadastrar torcedor")
    print("2 - Listar torcedores")
    print("3 - Cadastrar jogo")
    print("4 - Cadastrar show")
    print("5 - Vender ingresso")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        CRUDtorcedor.cadastrar_torcedor()
    elif op == "2":
        CRUDtorcedor.listar_torcedores()
    elif op == "3":
        CRUDjogos.cadastrar_jogo()
    elif op == "4":
        CRUDshows.cadastrar_show()
    elif op == "5":
        cpf = input("CPF: ")
        evento = input("Evento: ")
        tipo = input("Jogo ou Show: ")
        vendaingresso.vender_ingresso(cpf, evento, tipo)
    elif op == "0":
        break
    else:
        print("Opção inválida!")
