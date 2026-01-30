print('Bem vindo a pokedex hoenn')

pokedex = {"treecko": {
    "tipo": "grass",
    "abilities": "Overgrow e unburden",
    "attack": "45",
    "defense": "35", 
    "descrição": "Faz seu ninho em uma árvore gigante na floresta. "
    "guarda ferozmente contra qualquer coisa que se aproxime de seu território. "
    "Diz-se que é o protetor das árvores da floresta."},
    
    "torchic": {"tipo": "fire",
                "abilities": "blaze e speed boost",
                "attack": "60",
                "defense": "40",
                "descrição": "Se for atacado, ele contra-ataca cuspindo bolas de fogo que forma em seu estômago. "
                "UM TORCHIC não gosta da escuridão porque não consegue ver o seu redor."}}
while True:

        pokemon = input('Digite o nome do seu pokémon ou digite sair para finalizar o programa:').lower()

        if pokemon == 'sair':
            print('Pokedex finalizada.')
            break

        if pokemon in pokedex:
            dados = pokedex[pokemon]
            print(f'Tipo: {dados['tipo']}')
            print(f'abilities: {dados['abilities']}')
            print(f'Attack: {dados['attack']}')
            print(f'Defense: {dados['defense']}')
            print(f'Descrição da pokedex de Hoenn: {dados['descrição']}')

        else:
             print('Pokemon não encontrado.')