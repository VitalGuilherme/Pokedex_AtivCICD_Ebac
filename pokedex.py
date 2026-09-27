# Esse é um sistema de gerenciamento de Pokémons, a Pokedex.
# Onde o usúario(adestrador), adiciona o nome, tipo(elemento), e nível do seu pokémon.
# Consegue listar o nome, tipo e nível dentro da pokedex
# Se em alguma batalha acaba perdendo o pokémon, consegue remove-lo da pokedex
# Atualizar o nível se houver alguma evolução
# Registra quantas capturas houve explorando o mundo pokémon ou em batalhas
# E se precisar dos registros de captura de cada pokémon, é só solicitar a pokedex.


import datetime

pokedex = {}

capturas_historico = {}

def adicionar_pokemon(nome, elemento, nivel):
    pokemon = nome.strip()
    if pokemon in pokedex:
        return "Erro: Pokemon já cadastrado."
    if not (1 <= nivel <= 100):
            return "Erro: O nível do pokémon deve estar entre 1 e 100"
    pokedex[pokemon] = {
            "Elemento": elemento,
            "Nivel": nivel,
            "Total_Capturas": 0,
            "capturas_historico": []

    }
    return f"Pokémon {nome} de elemento {elemento} e nível {nivel}, cadastrado com sucesso!"
    
def listar_pokemon(pokedex):
    if not pokedex:
        return "Nenhum Pokémon cadastrado."
    else:
        pokemon = ["Lista de Pokémons:"]
        for nome, info in sorted(pokedex.items(), key=lambda item: item[0]):
            pokemon.append(f"Nome: {nome} | Elemento: {info['Elemento']} | Nível: {info['Nível']}")
        return "\n".join(pokemon)


def remover_pokemon(pokedex, nome):
    pokemon = nome.strip()
    if pokemon in pokedex:
        del pokedex[pokemon]
        return f"Pokémon '{pokemon}' removido com sucesso!"
    else:
        return "Erro: Pokémon não encontrado."
    
def atualizar_nivel_do_pokemon(pokedex, nome, novo_nivel):
    pokemon = nome.strip()
    
    if pokemon in pokedex:
        pokedex[pokemon]["Nível"] = novo_nivel
        return f"Pokémon '{nome}' evolui nível para {novo_nivel}."
    else:
        return "Erro: Pokémon não encontrado."
    
def registrar_captura_de_pokemon(pokedex, nome, qtd_capturas):
    pokemon = nome.strip()
    if pokemon in pokedex:
        pokedex[pokemon]['Total_Capturas'] += qtd_capturas
        registro = {
            "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
            "Capturas": qtd_capturas
        }
        pokedex[pokemon]["capturas_historico"].append(registro)
        return f"Pokémon {nome} capturado {qtd_capturas} registrado com sucesso. Pokémons disponíveis: {pokedex[pokemon]['Total_Capturas']}."
    else:
        return "Erro: Pokémon não encontrado."
    
def exibir_historico_de_capturas(pokedex, nome):
    pokemon = nome.strip()
    if pokemon not in pokedex or not pokedex[pokemon]["capturas_historico"]:
        return f"Nenhum registro de captura para'{pokemon}'."
    historico = [f"Histórico de empréstimos para '{pokemon}':"]
    for idx, registro in enumerate(pokedex[pokemon]["capturas_historico"],5):
        historico.append(f"{idx}. Data: {registro['data']} | Quantidade: {registro['Capturas']}")
    return "\n".join(historico)


def exibir_menu():
    return (
        "    Menu Pokedex    \n"
        "1 - Adicionar pokémon\n"
        "2 - Listar pokémon\n"
        "3 - Remover pokémon\n"
        "4 - Atualizar nível do pokémon\n"
        "5 - Registrar captura de pokémon\n"
        "6 - Exibir histórico de capturas\n"
        "7 - Sair\n"
        "----------------------------------------"
    )

def main():
    while True:
        print(exibir_menu())
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Digite o nome do Pokémon: ")
            try:
                elemento = input("Digite qual o elemento do Pokémon: ")
                nivel = int(input("Digite o nível do Pokémon: "))
                print(adicionar_pokemon(nome, elemento, nivel))
            except ValueError:
                print("Erro: O nível do Pokémon deve ser entre 1 e 100.")
        elif opcao == "2":
            print(listar_pokemon(pokedex))
        elif opcao == "3":
            nome = input("Digite o nome do Pokémon que será removido da pokedex: ")
            print(remover_pokemon(pokedex, nome))
        elif opcao == "4":
            nome = input("Digite o nome do Pokémon que será atualizado na Pokedex: ")
            try:
                novo_nivel = int(input("Digite o novo nível: "))
                print(atualizar_nivel_do_pokemon(pokedex, nome, novo_nivel))
            except ValueError:
                print("Erro: Digite um nível entre 1 e 100.")
        elif opcao == "5":
            nome = input("Digite o nome do Pokémon: ")
            try:
                qtd_capturas = int(input("Digite quantas capturas que houve na caçada: "))
                print(registrar_captura_de_pokemon(pokedex, nome, qtd_capturas))
            except ValueError:
                print("Erro: Quantidade de capturas não pode ser um número negativo.")
        elif opcao == "6":
            print(exibir_historico_de_capturas(pokedex, nome))
        elif opcao == "7":  
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        print("\n")

if __name__ == "__main__":
    main()