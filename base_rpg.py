# Sistema com 5 classes 
# Pequeno sistema rpg

class Item:
    def __init__(self, nome, bonus):
        self.nome = nome
        self.bonus = bonus

    def __str__(self):
        return f"{self.nome} (+ {self.bonus} ATQ)"

class Inventario:
    #O inventario pertence ao personagem. Se o personagem for destruido, o inventario também será destruido
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)

    def listar_itens(self):
        for item in self.itens:
            print(item)

class Personagem:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe

        self.inventario = Inventario()

    def calcular_bonus(self):
        total = 0 
        for item in self.inventario.itens:
            total += item.bonus
        return total

    def __str__(self):
        return f"{self.nome} ({self.classe})"

class Guilda:
    # Personagens existem idempendentes da guilda, mas a guilda pode ter vários personagens
    def __init__(self, nome):
        self.nome = nome
        self.membros = []

    def adicionar_membro(self, personagem):
        self.membros.append(personagem)

    def listar_membros(self):
        print(f"Membros da guilda {self.nome}:")
        for membro in self.membros:
            print(membro)


class Batalha:
    def lutar(self, personagem1, personagem2):
        print(f"{personagem1.nome} está lutando contra {personagem2.nome}!")

        bonus1 = personagem1.calcular_bonus()
        bonus2 = personagem2.calcular_bonus()

        if bonus1 > bonus2:
            vencedor = personagem1
        elif bonus2 > bonus1:
            vencedor = personagem2
        else:
            vencedor = None

        print("A batalha terminou!")

        if vencedor:
            print(f"Vencedor: {vencedor.nome}")
        else:
            print("Empate!")


class SistemaRPG:
    def executar(self):

        #cadastro personagem
        heroi = Personagem("Aragorn", "Guerreiro")
        mago = Personagem("Gandalf", "Mago")

        #cadastro itens
        espada = Item("Espada Longa", 10)
        cajado = Item("Cajado Mágico", 25)

        heroi.inventario.adicionar_item(espada)
        mago.inventario.adicionar_item(cajado)

        #cadastro guilda
        guilda = Guilda("sonserina")
        guilda.adicionar_membro(heroi)
        guilda.adicionar_membro(mago)

        guilda.listar_membros()

        print(f"\nInventário de {heroi.nome}:")
        heroi.inventario.listar_itens()

        print(f"\nInventário de {mago.nome}:")
        mago.inventario.listar_itens()

        #batalha
        batalha = Batalha()
        batalha.lutar(heroi, mago)


sistema = SistemaRPG()
sistema.executar()

personagens = {}
itens = {}
guildas = {}

while True:
    print("\n Bem-vindo ao Sistema RPG!")
    print("\n MENU RPG")
    print("1. Criar Personagem")
    print("2. Criar Item")
    print("3. Adicionar Item ao Personagem")
    print("4. Listar Itens do Personagem")
    print("5. Criar Guilda")
    print("6. Adicionar Membro à Guilda")
    print("7. Listar Membros da Guilda")
    print("8. Realizar Batalha")
    print("9. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do personagem: ")
        classe = input("Digite a classe do personagem: ")

        if nome in personagens:
            print("Já existe um personagem com esse nome.")
        else:
            personagem = Personagem(nome, classe)
            personagens[nome] = personagem
            print(f"Personagem {personagem} criado com sucesso!")

    elif opcao == "2":
        nome = input("Digite o nome do item: ")
        bonus = int(input("Digite o bônus do item: "))

        if nome in itens:
            print("Já existe um item com esse nome.")

        else:
            item = Item(nome, bonus)
            itens[nome] = item
            print(f"Item {item} criado com sucesso!")

    elif opcao == "3":
        nome_personagem = input("Digite o nome do personagem: ")
        nome_item = input("Digite o nome do item: ")

        if nome_personagem not in personagens:
            print("Personagem não encontrado.")
            continue
        if nome_item not in itens:
            print("Item não encontrado.")
            continue

        personagem = personagens[nome_personagem]
        item = itens[nome_item]
        personagem.inventario.adicionar_item(item)
        print(f"Item {item} adicionado ao inventário de {personagem}.")

    elif opcao == "4":
        nome_personagem = input("Digite o nome do personagem: ")

        if nome_personagem not in personagens:
            print("Personagem não encontrado.")
            continue

        personagem = personagens[nome_personagem]

        print(f"\nInventário de {personagem.nome}:")
        personagem.inventario.listar_itens()
        
    elif opcao == "5":
        nome_guilda = input("Digite o nome da guilda: ")

        if nome_guilda in guildas:
            print("Já existe uma guilda com esse nome.")
        else:
            guilda = Guilda(nome_guilda)
            guildas[nome_guilda] = guilda
            print(f"Guilda {guilda.nome} criada com sucesso!")
        
    elif opcao == "6":
        nome_guilda = input("Digite o nome da guilda: ")
        nome_personagem = input("Digite o nome do personagem: ")
        
        if nome_guilda not in guildas:
            print("Guilda não encontrada.")
            continue
        if nome_personagem not in personagens:
            print("Personagem não encontrado.")
            continue

        guilda = guildas[nome_guilda]
        personagem = personagens[nome_personagem]
        guilda.adicionar_membro(personagem)
        print(f"Personagem {personagem} adicionado à guilda {guilda}.")

    elif opcao == "7":
        nome_guilda = input("Digite o nome da guilda: ")

        if nome_guilda not in guildas:
            print("Guilda não encontrada.")
            continue

        guilda = guildas[nome_guilda]
        guilda.listar_membros()

    elif opcao == "8":
        nome_personagem1 = input("Digite o nome do primeiro personagem: ")
        nome_personagem2 = input("Digite o nome do segundo personagem: ")

        if nome_personagem1 not in personagens:
            print("Primeiro personagem não encontrado.")
            continue
        if nome_personagem2 not in personagens:
            print("Segundo personagem não encontrado.")
            continue

        personagem1 = personagens[nome_personagem1]
        personagem2 = personagens[nome_personagem2]
        
        batalha = Batalha()
        batalha.lutar(personagem1, personagem2)

    elif opcao == "9":
        print("Saindo do sistema RPG. Até logo!")
        break

    else:
        print("Opção inválida.")