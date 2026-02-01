from Database import adicionar_produto, buscar_produto, listar_produtos as listar_produtos_db


def cadastrar_produto(nome, preco, quantidade, promocao):
    adicionar_produto(nome, preco, quantidade, promocao)


def calcular_desconto(preco, promocao):
    desconto = 0

    if promocao:
        desconto = preco * 0.20
    elif preco >= 100:
        desconto = max(desconto, preco * 0.20)

    return desconto


def consultar_produto(nome):
    produto = buscar_produto(nome)

    if produto:
        nome, preco, quantidade, promocao = produto
        desconto = calcular_desconto(preco, promocao)
        preco_final = preco - desconto

        return {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade,
            "desconto": desconto,
            "preco_final": preco_final
        }

    return None

def listar_produtos():
    produtos = listar_produtos_db()

    lista_formatada = []

    for produto in produtos:
        nome, preco, quantidade, promocao = produto
        lista_formatada.append({
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade,
            "promocao": promocao
        })

    return lista_formatada