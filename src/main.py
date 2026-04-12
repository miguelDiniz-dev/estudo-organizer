import sys

tarefas = []


def adicionar_tarefa(materia, horas):
    if not materia or horas <= 0:
        return False
    tarefa = {"materia": materia, "horas": horas}
    tarefas.append(tarefa)
    return True


def listar_tarefas():
    return tarefas


def menu():
    print("\n--- Organizador de Estudos v1.0.0 ---")
    print("1. Adicionar Matéria")
    print("2. Listar Plano")
    print("3. Sair")
    
    while True:
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            m = input("Nome da matéria: ")
            h = int(input("Horas de estudo: "))
            if adicionar_tarefa(m, h):
                print("Adicionado com sucesso!")
            else:
                print("Erro: Dados inválidos.")
        elif opcao == "2":
            lista = listar_tarefas()
            for i, t in enumerate(lista):
                print(f"{i+1}. {t['materia']} - {t['horas']}h")
        elif opcao == "3":
            print("Bons estudos!")
            sys.exit()

if __name__ == "__main__":
    menu()
