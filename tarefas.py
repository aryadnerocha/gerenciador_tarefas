import os

ARQUIVO = "tarefas.txt"

def carregar_tarefas():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r") as f:
        return [linha.strip() for linha in f.readlines()]

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        for tarefa in tarefas:
            f.write(tarefa + "\n")

def listar_tarefas(tarefas):
    if not tarefas:
        print("✅ Nenhuma tarefa cadastrada.")
    else:
        print("\n📝 Lista de Tarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

def adicionar_tarefa(tarefas):
    nova = input("Digite a nova tarefa: ")
    tarefas.append(nova)
    salvar_tarefas(tarefas)
    print("✅ Tarefa adicionada!")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa a remover: ")) - 1
        if 0 <= indice < len(tarefas):
            removida = tarefas.pop(indice)
            salvar_tarefas(tarefas)
            print(f"🗑️ Tarefa '{removida}' removida!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def main():
    tarefas = carregar_tarefas()
    while True:
        print("\n📋 Menu:")
        print("1. Listar tarefas")
        print("2. Adicionar tarefa")
        print("3. Remover tarefa")
        print("4. Sair")

        opcao = input("Escolha: ")
        if opcao == "1":
            listar_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            remover_tarefa(tarefas)
        elif opcao == "4":
            print("👋 Até logo!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
