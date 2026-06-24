tarefas = []
def mostrar_menu():
  print("\n --- MENU PRINCIPAL ---")
  print("1. Adicionar nova tarefa")
  print("2. Visualizar tarefas")
  print("3. Marcar tarefas como concluídas")
  print("4. Sair")

while True:
  mostrar_menu()

  try:
    opcao = int(input("Digite sua opção: "))
  except ValueError:
    print("São aceitos somente numerais, tente novamente")
    continue     # Zera o loop e começa novamente

  if opcao == 1:
    nova_tarefa = input("Digite o nome da tarefa: ")

    dicionario_tarefa = {
      "nome" : nova_tarefa,
      "concluida" : False,
    }
    
    concluiu_tarefa = input("Você já concluiu essa tarefa?")

    if concluiu_tarefa == "sim":
      dicionario_tarefa["concluida"] = True

    tarefas.append(dicionario_tarefa)

  elif opcao == 2:
    contador = 0
    for i in tarefas:
      contador += 1
      print(contador, i["nome"])

  elif opcao == 3:
    contador_dois = 0

    for i in tarefas:
      contador_dois += 1
      if not i["concluida"] == True :
        print(contador_dois, i["nome"])


    escolha_usuario = int(input("Escolha qual tarefa deseja marcar como concluida: "))
    buscador = escolha_usuario - 1
    tarefas[buscador]["concluida"] = True
    

  elif opcao == 4:
    print("Fechando programa...")
    break

  else:
    print("Tente uma opção válida, por favor")




