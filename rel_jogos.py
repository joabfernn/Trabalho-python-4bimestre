def relatorio_jogos_realizados(jogos):
    print("Jogos realizados:")
    for jogo in jogos:
        print(f'{jogo["nome"]} - Data: {jogo["data"]}')
