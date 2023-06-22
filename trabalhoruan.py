import datetime
import os 
# Lista para armazenar os produtos cadastrados
produtos = []
#função para cadastrar produtos
def cadastrar_produto():
    while True:
        print("== Cadastro de Produto ==")
        nome = input("Nome do produto: ")
        estoque = int(input("Quantidade em estoque: "))
        valor = float(input("Valor do produto: "))
        promocao = input("O produto está em promoção? (S/N): ").upper() == "S"
#caso seja deixado um espaço vazio
        if nome == "":
            print("O nome do produto é obrigatório.")
            continue
#caso o estoque seja menor ou = a 0
        if estoque <= 0:
            print("A quantidade em estoque não pode ser negativa.")
            continue
#dicionario 
        produto = {
            "nome": nome,
            "estoque": estoque,
            "valor": valor,
            "promocao": promocao
        }
        #colocando os dados da lista no dicionario
        produtos.append(produto)
        print("Produto cadastrado com sucesso.")

        opcao = input("Deseja cadastrar outro produto? (S/N): ").upper()
        if opcao != "S":
            break
#função para pesquisar produto
def pesquisar_produto():
    while True:
        print("== Pesquisar Produto ==")
        nome = input("Nome do produto: ")
        #caso o produto não seja encontrado
        encontrado = False
#fazendo a leitura do produto caso achado
        for produto in produtos:
            if produto["nome"].lower() == nome.lower():
                print("Nome:", produto["nome"])
                print("Estoque:", produto["estoque"])
                print("Valor:", produto["valor"])
                if produto["promocao"]:
                    print("Promoção: Sim")
                else:
                    print("Promoção: Não")
                encontrado = True
                break
#se não for encontrado
        if not encontrado:
            print("Produto não encontrado.")

        opcao = input("Deseja pesquisar outro produto? (S/N): ").upper()
        if opcao != "S":
            break
#funçao para alterar produto
def alterar_produto():
    while True:
        print("== Alterar Produto ==")
        nome = input("Nome do produto: ")
        encontrado = False
#fazendo a leitura do programa caso achado
        for produto in produtos:
            if produto["nome"].lower() == nome.lower():
                print("Digite os novos dados do produto (deixe em branco para manter o valor atual):")
                novo_nome = input("Nome do produto: ")
                novo_estoque = input("Quantidade em estoque: ")
                novo_valor = input("Valor do produto: ")
                nova_promocao = input("O produto está em promoção? (S/N): ").upper()

                if novo_nome != "":
                    produto["nome"] = novo_nome

                if novo_estoque != "":
                    estoque = int(novo_estoque)
                    if estoque < 0:
                        print("A quantidade em estoque não pode ser negativa.")
                        return
                    produto["estoque"] = estoque

                if novo_valor != "":
                    produto["valor"] = float(novo_valor)

                if nova_promocao != "":
                    produto["promocao"] = nova_promocao == "S"

                print("Produto alterado com sucesso.")
                encontrado = True
                break
#se não for encontrado
        if not encontrado:
            print("Produto não encontrado.")

        opcao = input("Deseja alterar outro produto? (S/N): ").upper()
        if opcao != "S":
            break
#função para remover produto
def remover_produto():
    while True:
        print("== Remover Produto ==")
        nome = input("Nome do produto: ")
        encontrado = False
#fazendo a leitura do produto caso achado
        for produto in produtos:
            if produto["nome"].lower() == nome.lower():
                produtos.remove(produto)
                print("Produto removido com sucesso.")
                encontrado = True
                break

        if not encontrado:
            print("Produto não encontrado.")

        opcao = input("Deseja remover outro produto? (S/N): ").upper()
        if opcao != "S":
            break
#função para realizar venda
def realizar_venda():
    while True:
        print("== Realizar Venda ==")
        nome = input("Nome do produto: ")
        encontrado = False

        for produto in produtos:
            if produto["nome"].lower() == nome.lower():
                quantidade = int(input("Quantidade vendida: "))

                if quantidade > produto["estoque"]:
                    print("Quantidade em estoque insuficiente.")
                    return

                valor_total = quantidade * produto["valor"]
                if produto["promocao"]:
                    valor_total *= 15/100 # Aplicando desconto de 15% se estiver em promoção
                produto["estoque"] -= quantidade
                data_venda = datetime.date.today().strftime("%d/%m/%Y")

                print("Venda realizada com sucesso.")
                print("Valor total da venda:", valor_total)
                print("Data da venda:", data_venda)
                encontrado = True
                break

        if not encontrado:
            print("Produto não encontrado.")

        opcao = input("Deseja realizar outra venda? (S/N): ").upper()
        if opcao != "S":
            break

def listar_vendas():
    print("== Listar Vendas ==")

    if len(produtos) == 0:
        print("Não há vendas realizadas.")
        return
#fazendo a leitura do produto caso achado
    for produto in produtos:
        print("Nome:", produto["nome"])
        print("Quantidade em estoque:", produto["estoque"])
        print("Valor:", produto["valor"])
        if produto["promocao"]:
            print("Promoção: Sim")
        else:
            print("Promoção: Não")
        print("=============================")
#função para exibir menu
def exibir_menu():
    print("\n== Mercadao da Dedeza e do L.Ruan ==")
    print("1 - Cadastrar Produto")
    print("2 - Pesquisar Produto")
    print("3 - Alterar Produto")
    print("4 - Remover Produto")
    print("5 - Realizar Venda")
    print("6 - Listar Vendas")
    print("7 - Sair")

exibir_menu()
opcao = input("Escolha uma opção: ")
#lupin 
while opcao != "7":
    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        pesquisar_produto()
    elif opcao == "3":
        alterar_produto()
    elif opcao == "4":
        remover_produto()
    elif opcao == "5":
        realizar_venda()
    elif opcao == "6":
        listar_vendas()
    else:
        print("Opção inválida.")
    input("Pressione Enter para continuar...")
    os.system('clear')  
        

    exibir_menu()
    opcao = input("Escolha uma opção: ")