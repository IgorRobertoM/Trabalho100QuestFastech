while True:
    print("\nLojas Tabajara")
    total = 0
    produto = 1
    
    while True:
        preco = float(input(f"Produto {produto}: R$ "))
        if preco == 0:
            break
        total += preco
        produto += 1
    
    print(f"Total: R$ {total:.2f}")
    
    dinheiro = float(input("Dinheiro: R$ "))
    
    if dinheiro < total:
        print("Dinheiro insuficiente!")
    else:
        troco = dinheiro - total
        print(f"Troco: R$ {troco:.2f}")