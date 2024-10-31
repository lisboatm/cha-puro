# Leitura do tipo de chá correto
T = int(input())

# Leitura das respostas dos competidores
respostas = list(map(int, input().split()))

# Contagem de acertos
acertos = respostas.count(T)

# Exibindo o resultado
print(acertos)
