print("="*47)
print("Bem-vindo a Loja do JOAO VICTOR SILVA DE SOUSA!")

#SOLICITANDO DADOS EM RELAÇÃO AO PEDIDO
valorDoPedido = float(input("Entre com o valor do pedido: "))
quantidadeParcelas = int(input("Entre com a quantidade de parcelas: "))


#FAZENDO O CÁLCULO EM RELAÇÃO A QUANTIDADE DE PARCELAS
if quantidadeParcelas < 4:
    juros = (0/100)

elif quantidadeParcelas >=4 and quantidadeParcelas < 6:
    juros = (4/100)

elif quantidadeParcelas>=6 and quantidadeParcelas <9:
    juros = (8/100)

elif quantidadeParcelas >=9 and quantidadeParcelas<13:
    juros = (16/100)

else:
    juros = (32/100)

#APLICANDO A FÓRMULA PARA DESCOBRIR O QUE SE PEDE
valorDaParcela = ((valorDoPedido)*(1+juros))/(quantidadeParcelas)
valorTotalParcelado = valorDaParcela * quantidadeParcelas

#IMPRIMINDO NA TELA O QUE FOI SOLICITADO
print("O valor das parcelas é de: R$ {:.2f}".format(valorDaParcela))
print("O valor Total Parcelado é de: R$ {:.2f}".format(valorTotalParcelado))

print("="*47)