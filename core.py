import functions

tarefas = []

while True:
  functions.mostrar_menu()

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
    
    concluiu_tarefa = input("Você já concluiu essa tarefa?").strip().lower()            # Strip ignora espaços em branco

    while True:
      if concluiu_tarefa in ["sim", "nao"]:
        if concluiu_tarefa == "sim":
          dicionario_tarefa["concluida"] = True
          tarefas.append(dicionario_tarefa)
          print("Tarefa adicionada com sucesso !")
          break
        elif concluiu_tarefa == "nao":
          dicionario_tarefa["concluida"] = False
          tarefas.append(dicionario_tarefa)
          print("Tarefa adicionada com sucesso !")
          break
      else:
        print("Tente novamente, só serão aceitas respostas sim ou não")
        concluiu_tarefa = input("Você já concluiu essa tarefa?").strip().lower()


  elif opcao == 2:
    contador = 0
    for i in tarefas:
      contador += 1
      if i["concluida"] == True :
        print(contador, i["nome"], "Concluida")
      else:
        print(contador, i["nome"], "Pendente")
        

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

    contador_tres = 0
    for i in tarefas:
      contador_tres += 1
      print(contador_tres, i["nome"])
      
    excluir_tarefa = int(input("Qual tarefa você deseja excluir ?"))
    buscador_dois = excluir_tarefa - 1
    tarefas.pop(buscador_dois)
    print("Tarefa excluida com sucesso !")


  elif opcao == 5:
    print("Fechando programa...")
    break

  else:
    print("Tente uma opção válida, por favor")




