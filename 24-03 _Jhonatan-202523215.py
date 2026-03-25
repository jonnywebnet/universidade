reset = "\033[0m"
verde = "\033[32m"

print(verde + "=== EXERCÍCIO 1 ===" + reset)
try:
    x = float(input("Digite um número: "))
    y = float(input("Digite outro número: "))
    resultado = x / y
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Erro: não pode dividir por zero!")
except ValueError:
    print("Erro: digite um número válido!")

print(verde + "\n=== EXERCÍCIO 2 ===" + reset)
cores = {'vermelho': (255, 0, 0), 'verde': (0, 255, 0), 'azul': (0, 0, 255)}

try:
    cor = input("Digite uma cor (vermelho, verde, azul): ").lower()
    rgb = cores[cor]
    print("RGB da cor:", rgb)
except KeyError:
    print("Erro: essa cor não existe no dicionário!")

print(verde + "\n=== EXERCÍCIO 3 ===" + reset)
try:
    numero = int(input("Digite um número: "))
    if numero > 10:
        print("Número válido!")
except ValueError:
    print("Erro: deve ser um número!")
else:
    print("Programa executado com sucesso!")
finally:
    print("Programa encerrado")

def validar_senha(senha):
    if len(senha) < 8:
        raise ValueError("Senha deve ter pelo menos 8 caracteres!")
    
    tem_numero = False
    for c in senha:
        if c.isdigit():
            tem_numero = True
            break
    
    if not tem_numero:
        raise ValueError("Senha deve ter pelo menos 1 número!")

print(verde + "\n=== EXERCÍCIO 4 ===" + reset)
try:
    senha = input("Digite uma senha: ")
    validar_senha(senha)
    print("Senha válida!")
except ValueError as e:
    print("Erro:", e)

print(verde + "\n=== EXERCÍCIO 5 ===" + reset)
try:
    saldo = float(input("Saldo da conta: R$ "))
    transferencia = float(input("Valor da transferência: R$ "))
    
    if transferencia > saldo:
        raise ValueError("Saldo insuficiente")
    
    novo_saldo = saldo - transferencia
    print("Transferência realizada!")
    print("Novo saldo: R$", novo_saldo)
except ValueError:
    print("Erro: Saldo insuficiente")