fila_entregas = []
motoboys_disponiveis = ["Fernando", "Leonardo", "Jeferson"]
while True:
 print("1 - Novo pedido chegou")
      #(Adicionar a fila)
 print("2 - Chamar o próximo motoboy")
      #(Despachar entrega)
 print("3 - Ver fila de entrega e motoboys online")
 print("4 - Fechar sistema")
 opcao = int(input("Escolha uma opção: "))
 if opcao == 4:
     print("Fechando o Sistema de Delivery!")
     break
 elif opcao == 1:
     pedido = input("Digite o nome/número do pedido: ")
     fila_entregas.append(pedido)
 elif opcao == 3:
     print(f"\nPedidos aguardando entrega: {fila_entregas}")
     print(f"Motoboys disponíveis/Online: {motoboys_disponiveis}\n")
 elif opcao == 2:
     if len(fila_entregas) == 0:
        print("\n Não há pedidos na fila para entregar!")
     else:
        pedido_despachado = fila_entregas.pop(0)
        motoboy_da_vez = motoboys_disponiveis.pop(0)  

        print(f"\n Sucesso! O motoboy {motoboy_da_vez} saiu para entregar o pedido: {pedido_despachado}!")