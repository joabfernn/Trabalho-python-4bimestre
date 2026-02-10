def relatorio_torcedores_por_periodo(ingressos, periodo):
    contador = 0
    for ingresso in ingressos:
        if ingresso["data"] == periodo:
            contador += 1
    print(f"Torcedores no período {periodo}: {contador}")
