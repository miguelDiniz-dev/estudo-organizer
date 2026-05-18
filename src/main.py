import sys
import requests


tarefas = []


def obter_dica():
    """Consome uma API Pública para exibir uma dica/conselho na tela."""
    try:
        resposta = requests.get("https://api.adviceslip.com/advice", timeout=5)
        if resposta.status_code == 200:
            dados = resposta.json()
            return f"Dica da API: {dados['slip']['advice']}"
        return "Dica local: Estude um pouco todos os dias!"
    except:
        return "Dica local: Mantenha o foco e não desista!"


def adicionar_tarefa(materia, horas):
    if not materia or horas <= 0:
        return False
    tarefa = {"materia": materia, "horas": horas}
    tarefas.append(tarefa)
    return True


def listar_tarefas():
    return tarefas


def menu():
    print("\n--- Organizador de Estudos v2.0.0 ---")
    print(obter_dica())
    print("-------------------------------------")
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
            if not lista:
                print("Nenhuma matéria cadastrada.")
            for i, t in enumerate(lista):
                print(f"{i+1}. {t['materia']} - {t['horas']}h")
        elif opcao == "3":
            print("Bons estudos!")
            sys.exit()

if __name__ == "__main__":
    menu()
