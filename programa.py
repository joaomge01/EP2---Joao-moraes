from funcoes import define_posicoes, preenche_frota, posicao_valida

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}

navios = [
    ("porta-aviões", 4, 1),
    ("navio-tanque", 3, 2),
    ("contratorpedeiro", 2, 3),
    ("submarino", 1, 4)
]

for nome, tamanho, quantidade in navios:
    for _ in range(quantidade):
        print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
        pos_valida = False
        while not pos_valida:
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            if nome == "submarino":
                orientacao = "vertical"
            else:
                orient_num = int(input("[1] Vertical [2] Horizontal >"))
                orientacao = "vertical" if orient_num == 1 else "horizontal"
            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                pos_valida = True
            else:
                print("Esta posição não está válida!")

print(frota)
