cpf_inteiro = input('Por favor, digite seu CPF, apenas numeros: ')
cpf = cpf_inteiro[:9]
reorganizar_numeros = [0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
for numero in cpf:
    reorganizar_numeros[i] = int(numero)
    i += 1
i = 0
cpf = reorganizar_numeros
i = 0
multiplicador = 10
coleta = [0, 0, 0, 0, 0, 0, 0, 0, 0]
final = 0
while True:
    resultado = cpf[i] * multiplicador 
    coleta[i] = resultado
    i += 1
    multiplicador -= 1
    final += resultado
    if multiplicador == 1:
        break

print(final)
print(coleta)
primeiro_digito = 0
if ((final * 10) % 11) <=9:
    primeiro_digito = ((final * 10) % 11) % 11
else:
    primeiro_digito = 0

print(f'{primeiro_digito}')
