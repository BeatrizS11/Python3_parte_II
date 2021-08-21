peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {} :.if'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('você está em SOBRPESO!')
elif 30 <= imc < 40:
    print('você está em OBESIDADE, CUIDADO')
elif imc >= 40:
    print('você está em OBESIDADE MÓRBIDA, cuidado!')