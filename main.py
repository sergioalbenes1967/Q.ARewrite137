import pytest

# Cozinheiro - Definições
def somar_dois_numeros(num1, num2):
    return num1 + num2

def subtrair_dois_numeros(num1, num2):
    return num1 - num2

def multiplicar_dois_numeros(num1, num2):
    return num1 * num2

def dividir_dois_numeros(num1, num2):
    return num1 / num2

def elevar_um_numero_pelo_outro(num1,num2):
    return num1 ** num2

# Calcular e testar a area do quadrado
# area = Lado **

# Calcular e testa a area do retnglo
# Area = Lado1 * Lado2

# Calcular e testar a area de um triangulo
# Area = lado1 * lado2 / 2

# Calcular e testar a area do circulo
# Area = pi* raio **

def calcular_area_do_circulo(raio):
    return 3.14 * raio ** 2

if __name__ == '__main__':

    # Garçon - Requisições / Chamadas
    resultado = somar_dois_numeros(5,7)
    print(f'A soma é {resultado}') # <-- Prato

    resultado = subtrair_dois_numeros(7,5)
    print(f'A subtração é {resultado}')

    resultado = multiplicar_dois_numeros(3,5)
    print(f'A multiplicação é {resultado}')

    resultado = dividir_dois_numeros(8,4)
    print(f'A divisão é {resultado}')

    resultado = elevar_um_numero_pelo_outro(7,7)
    print(f'A potencialização é (resultado')

    # Degustador Teste

def testar_somar_dois_numeros():
    # -1° Etapa: Configura / Prepara
    # Dados / Valores
    # Entrada / Input
    num1 = 8
    num2 = 9
    # Saida / Output
    resultado_esperado = 17

    # - 2° Etapa:  Executa
    resultado_atual = somar_dois_numeros(num1,num2)

    # - 3° Etapa: Valida
    assert resultado_atual == resultado_esperado


