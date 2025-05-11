import json
import csv

def carregar_gastos():
    try:
        with open("gastos.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_gastos(gastos):
    with open("gastos.json", "w") as arquivo:
        json.dump(gastos, arquivo, indent=4)

def salvar_em_csv(gastos):
    with open("gastos.csv", "w", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Descrição", "Valor", "Categoria"])
        for gasto in gastos:
            escritor.writerow([gasto["descricao"], gasto["valor"], gasto["categoria"]])

def adicionar_gasto():
    while True:
        descricao = input("Descrição do gasto: ")
        if descricao.lower() == 'x':
            return
        
        try:
            valor = input("Valor do gasto: R$ ")
            if valor.lower() == 'x':
                return
            valor = float(valor)
        except ValueError:
            print("Valor inválido! Tente novamente ou digite 'x' para voltar.\n")
            continue
        
        categoria = input("Categoria: ")
        if categoria.lower() == 'x':
            return
        
        gasto = {"descricao": descricao, "valor": valor, "categoria": categoria}
        
        gastos = carregar_gastos()
        gastos.append(gasto)
        salvar_gastos(gastos)
        print("Gasto registrado com sucesso!\n")
        break

def listar_gastos():
    gastos = carregar_gastos()
    if not gastos:
        print("Nenhum gasto registrado.\n")
        return
    
    print("Lista de Gastos:")
    for i, gasto in enumerate(gastos, start=1):
        print(f"{i}. {gasto['descricao']} - R$ {gasto['valor']:.2f} ({gasto['categoria']})")
    print()

def menu():
    while True:
        print("1. Adicionar Gasto")
        print("2. Listar Gastos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_gasto()
        elif opcao == "2":
            listar_gastos()
        elif opcao == "3":
            print("Salvando gastos em CSV...")
            gastos = carregar_gastos()
            salvar_em_csv(gastos)
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    menu()
