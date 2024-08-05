compras = float(input("Digite o valor total das compras para receber um desconto: "))
pagamento = input("Digite a forma de pagamento! (Cartão/cheque/dinheiro/parcelar 3x/2x sem juros): ").lower()

dinheiro_ou_cheque = compras * 0.10
vista_cartao = compras * 0.05
calculo_juros = compras * 0.20
juros = compras + calculo_juros

if "cheque" in pagamento or "dinheiro" in pagamento:
    total_com_desconto = compras - dinheiro_ou_cheque
    print("Você recebeu um desconto de R$ {:.2f}, equivalente a 10% nas suas compras. Total a pagar: R$ {:.2f}.".format(dinheiro_ou_cheque, total_com_desconto))
elif "cartão" in pagamento:
    total_com_desconto = compras - vista_cartao
    print("Você recebeu um desconto de R$ {:.2f}, equivalente a 5% nas suas compras. Total a pagar: R$ {:.2f}.".format(vista_cartao, total_com_desconto))
elif "parcelar 3x" in pagamento:
    print("Você vai pagar em 3x com juros de R$ {:.2f}, totalizando R$ {:.2f} nas suas compras.".format(calculo_juros, juros))
elif "2x sem juros" in pagamento:
    print("Você vai pagar em 2x sem juros, totalizando R$ {:.2f} nas suas compras.".format(compras))
else:
    print("Forma de pagamento não reconhecida.")