# Pequeno sistema rpg


class Item:
    def __init__(self, nome, bonus):
        self.nome = nome
        self.bonus = bonus

    def __str__(self):
        return f"{self.nome} (+ {self.bonus} ATQ)"


class Inventario:
    # Composicao: o inventario pertence ao personagem.
    # Se o personagem for destruido, seu inventario tambem sera destruido.

    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
            print(f"Item {item.nome} removido do inventario.")
        else:
            print("Esse item nao esta no inventario.")

    def listar_itens(self):
        if not self.itens:
            print("Inventario vazio.")
            return

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
    # Agregacao: personagens existem independentemente da guilda.
    # Uma guilda pode possuir varios membros.

    def __init__(self, nome):
        self.nome = nome
        self.membros = []

    def adicionar_membro(self, personagem):
        if personagem in self.membros:
            return False

        self.membros.append(personagem)
        return True

    def listar_membros(self):
        print(f"\nMembros da guilda {self.nome}:")

        if not self.membros:
            print("Nenhum membro cadastrado.")
            return

        for membro in self.membros:
            print(f"- {membro}")


class Batalha:
    def lutar(self, personagem1, personagem2):
        print(
            f"\n{personagem1.nome} esta lutando "
            f"contra {personagem2.nome}!"
        )

        bonus1 = personagem1.calcular_bonus()
        bonus2 = personagem2.calcular_bonus()

        print(f"{personagem1.nome}: {bonus1} ATQ")
        print(f"{personagem2.nome}: {bonus2} ATQ")

        if bonus1 > bonus2:
            vencedor = personagem1
        elif bonus2 > bonus1:
            vencedor = personagem2
        else:
            vencedor = None

        print("\nA batalha terminou!")

        if vencedor:
            print(f"Vencedor: {vencedor.nome}")
        else:
            print("Empate!")


class SistemaRPG:
    def __init__(self):
        # Dicionarios que armazenam todos os objetos do sistema.
        self.personagens = {}
        self.itens = {}
        self.guildas = {}

        # Carrega os personagens e itens de exemplo.
        self.carregar_dados_iniciais()

    def carregar_dados_iniciais(self):
        # Cadastro inicial de personagens.
        heroi = Personagem("Aragorn", "Guerreiro")
        mago = Personagem("Gandalf", "Mago")

        self.personagens[heroi.nome] = heroi
        self.personagens[mago.nome] = mago

        # Cadastro inicial de itens.
        espada = Item("Espada Longa", 10)
        cajado = Item("Cajado Magico", 25)

        self.itens[espada.nome] = espada
        self.itens[cajado.nome] = cajado

        # Associacao dos itens aos inventarios.
        heroi.inventario.adicionar_item(espada)
        mago.inventario.adicionar_item(cajado)

        # Cadastro inicial da guilda.
        guilda = Guilda("Sonserina")
        guilda.adicionar_membro(heroi)
        guilda.adicionar_membro(mago)

        self.guildas[guilda.nome] = guilda

    def mostrar_dados_iniciais(self):
        print("\n========== DADOS INICIAIS ==========")

        self.listar_personagens()
        self.listar_todos_itens()
        self.listar_guildas()

        print("\nOs dados iniciais foram carregados!")
        print("Voce ja pode jogar pelo menu.")

    def criar_personagem(self):
        nome = input("Digite o nome do personagem: ").strip()
        classe = input("Digite a classe do personagem: ").strip()

        if not nome or not classe:
            print("Nome e classe nao podem ficar vazios.")
            return

        if nome in self.personagens:
            print("Ja existe um personagem com esse nome.")
            return

        personagem = Personagem(nome, classe)
        self.personagens[nome] = personagem

        print(f"Personagem {personagem} criado com sucesso!")

    def criar_item(self):
        nome = input("Digite o nome do item: ").strip()

        if not nome:
            print("O nome do item nao pode ficar vazio.")
            return

        if nome in self.itens:
            print("Ja existe um item com esse nome.")
            return

        try:
            bonus = int(input("Digite o bonus de ataque do item: "))
        except ValueError:
            print("Digite um numero inteiro para o bonus.")
            return

        item = Item(nome, bonus)
        self.itens[nome] = item

        print(f"Item {item} criado com sucesso!")

    def adicionar_item_personagem(self):
        nome_personagem = input(
            "Digite o nome do personagem: "
        ).strip()

        nome_item = input("Digite o nome do item: ").strip()

        if nome_personagem not in self.personagens:
            print("Personagem nao encontrado.")
            return

        if nome_item not in self.itens:
            print("Item nao encontrado.")
            return

        personagem = self.personagens[nome_personagem]
        item = self.itens[nome_item]

        personagem.inventario.adicionar_item(item)

        print(
            f"Item {item.nome} adicionado ao inventario "
            f"de {personagem.nome}."
        )

    def listar_itens_personagem(self):
        nome = input("Digite o nome do personagem: ").strip()

        if nome not in self.personagens:
            print("Personagem nao encontrado.")
            return

        personagem = self.personagens[nome]

        print(f"\nInventario de {personagem.nome}:")
        personagem.inventario.listar_itens()

        print(
            f"Bonus total de ataque: "
            f"{personagem.calcular_bonus()}"
        )

    def criar_guilda(self):
        nome = input("Digite o nome da guilda: ").strip()

        if not nome:
            print("O nome da guilda nao pode ficar vazio.")
            return

        if nome in self.guildas:
            print("Ja existe uma guilda com esse nome.")
            return

        guilda = Guilda(nome)
        self.guildas[nome] = guilda

        print(f"Guilda {guilda.nome} criada com sucesso!")

    def adicionar_membro_guilda(self):
        nome_guilda = input("Digite o nome da guilda: ").strip()
        nome_personagem = input(
            "Digite o nome do personagem: "
        ).strip()

        if nome_guilda not in self.guildas:
            print("Guilda nao encontrada.")
            return

        if nome_personagem not in self.personagens:
            print("Personagem nao encontrado.")
            return

        guilda = self.guildas[nome_guilda]
        personagem = self.personagens[nome_personagem]

        if guilda.adicionar_membro(personagem):
            print(
                f"Personagem {personagem.nome} adicionado "
                f"a guilda {guilda.nome}."
            )
        else:
            print("Esse personagem ja faz parte da guilda.")

    def listar_membros_guilda(self):
        nome = input("Digite o nome da guilda: ").strip()

        if nome not in self.guildas:
            print("Guilda nao encontrada.")
            return

        self.guildas[nome].listar_membros()

    def realizar_batalha(self):
        nome1 = input(
            "Digite o nome do primeiro personagem: "
        ).strip()

        nome2 = input(
            "Digite o nome do segundo personagem: "
        ).strip()

        if nome1 not in self.personagens:
            print("Primeiro personagem nao encontrado.")
            return

        if nome2 not in self.personagens:
            print("Segundo personagem nao encontrado.")
            return

        personagem1 = self.personagens[nome1]
        personagem2 = self.personagens[nome2]

        batalha = Batalha()
        batalha.lutar(personagem1, personagem2)

    def listar_personagens(self):
        print("\n--- PERSONAGENS CADASTRADOS ---")

        if not self.personagens:
            print("Nenhum personagem cadastrado.")
            return

        for personagem in self.personagens.values():
            print(
                f"- {personagem} | "
                f"Bonus de ataque: {personagem.calcular_bonus()}"
            )

    def listar_todos_itens(self):
        print("\n--- TODOS OS ITENS CADASTRADOS ---")

        if not self.itens:
            print("Nenhum item cadastrado.")
            return

        for item in self.itens.values():
            print(f"- {item}")

    def listar_guildas(self):
        print("\n--- GUILDAS CADASTRADAS ---")

        if not self.guildas:
            print("Nenhuma guilda cadastrada.")
            return

        for guilda in self.guildas.values():
            guilda.listar_membros()

    def executar(self):
        # Mostra os objetos que foram carregados antes de jogar.
        self.mostrar_dados_iniciais()

        while True:
            print("\n========== MENU RPG ==========")
            print("1. Criar Personagem")
            print("2. Criar Item")
            print("3. Adicionar Item ao Personagem")
            print("4. Listar Itens do Personagem")
            print("5. Criar Guilda")
            print("6. Adicionar Membro a Guilda")
            print("7. Listar Membros da Guilda")
            print("8. Realizar Batalha")
            print("9. Sair")
            print("10. Listar Personagens")
            print("11. Listar Todos os Itens")
            print("12. Listar Guildas")

            opcao = input("Escolha uma opcao: ").strip()

            if opcao == "1":
                self.criar_personagem()

            elif opcao == "2":
                self.criar_item()

            elif opcao == "3":
                self.adicionar_item_personagem()

            elif opcao == "4":
                self.listar_itens_personagem()

            elif opcao == "5":
                self.criar_guilda()

            elif opcao == "6":
                self.adicionar_membro_guilda()

            elif opcao == "7":
                self.listar_membros_guilda()

            elif opcao == "8":
                self.realizar_batalha()

            elif opcao == "9":
                print("Saindo do Sistema RPG. Ate logo!")
                break

            elif opcao == "10":
                self.listar_personagens()

            elif opcao == "11":
                self.listar_todos_itens()

            elif opcao == "12":
                self.listar_guildas()

            else:
                print("Opcao invalida. Escolha uma opcao do menu.")


# Ponto de entrada: inicia diretamente a parte jogavel.
if __name__ == "__main__":
    sistema = SistemaRPG()
    sistema.executar()
