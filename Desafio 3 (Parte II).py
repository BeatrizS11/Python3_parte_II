peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {} :.if'.format(imc))
if imc < 2.1:
    print('Peso invalido, não existe pessoa tão leve assim')
elif imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('você está em SOBRPESO!')
elif 30 <= imc < 40:
    print('você está em OBESIDADE classificada COMO GRAU 1, CUIDADO')
elif 40 <= imc < 50:
    print('você está em OBESIDADE classificada COMO GRAU 2, CUIDADO!')
elif 50 <= imc < 100:
    print('Você está em OBESIDADE classificada como GRAU 3,CUIDADO SUA SAÚDE ESTÁ EM RISCO!!!')
elif imc <= 500:
    print('Peso invalido, não existe pessoa tão pessada assim')