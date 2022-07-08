def desafio():

    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    ano_nasc = 2022 - idade
    peso = float(input('Digite o seu peso: '))
    altura = float(input('Digite sua altura: '))
    imc = peso / (altura ** 2)
    print(f'{nome}, {idade} anos, nasceu em {ano_nasc}, tem {altura} de altura e pesa {peso} e seu IMC é de {imc:.2f}')

desafio()