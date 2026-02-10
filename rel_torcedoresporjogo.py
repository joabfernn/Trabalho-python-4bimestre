def relatorio_torcedores_por_jogo(jogos, ingressos):
    for jogo in jogos:
        contador = 0
        for ingresso in ingressos:
            if ingresso["evento"] == jogo["nome"] and ingresso["tipo"] == "Jogo":
                contador += 1
        print(f'Jogo: {jogo["nome"]} | Torcedores: {contador}')
