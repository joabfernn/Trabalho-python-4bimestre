def calendario_jogos_e_shows(jogos, shows):
    print("\n--- CALENDÁRIO DO ESTÁDIO ---")

    print("\nJogos:")
    for jogo in jogos:
        print(f'{jogo["data"]} - {jogo["nome"]}')

    print("\nShows:")
    for show in shows:
        print(f'{show["data"]} - {show["artista"]}')
