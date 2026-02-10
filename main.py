import CRUDtorcedor
import CRUDjogos
import CRUDshows
import vendaingresso

import rel_torcedoresporjogo
import rel_jogos
import rel_torcedoresporperiodo
import rel_calendario

while True:
    print("\n=== SISTEMA DE GERENCIAMENTO DO ESTÁDIO ===")
    print("1 - Cadastrar torcedor")
    print("2 - Listar torcedores")
    print("3 - Cadastrar jogo")
    print("4 - Cadastrar show")
    print("5 - Vender ingresso")
    print("6 - Relatório: Torcedores por jogo")
    print("7 - Relatório: Jogos realizados")
    print("8 - Relatório: Torcedores por período")
    print("9 - Calendário de jogos e shows")
    print("0 - Sair")

    op = input("Escolha uma opção: ")

    if op == "1":
        CRUDtorcedor.cadastrar_torcedor()

    elif op == "2":
        CRUDtorcedor.listar_torcedores()

    elif op == "3":
        CRUDjogos.cadastrar_jogo()

    elif op == "4":
        CRUDshows.cadastrar_show()

    elif op == "5":
        cpf = input("CPF do torcedor: ")
        evento = input("Nome do evento: ")
        tipo = input("Tipo (Jogo ou Show): ")
        vendaingresso.vender_ingresso(cpf, evento, tipo)

    elif op == "6":
        rel_torcedoresporjogo.relatorio_torcedores_por_jogo(
            CRUDjogos.jogos,
            vendaingresso.ingressos
        )

    elif op == "7":
        rel_jogos.relatorio_jogos_realizados(
            CRUDjogos.jogos
        )

    elif op == "8":
        periodo = input("Digite a data (ex: 10/06/2026): ")
        rel_torcedoresporperiodo.relatorio_torcedores_por_periodo(
            vendaingresso.ingressos,
            periodo
        )

    elif op == "9":
        rel_calendario.calendario_jogos_e_shows(
            CRUDjogos.jogos,
            CRUDshows.shows
        )

    elif op == "0":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")
