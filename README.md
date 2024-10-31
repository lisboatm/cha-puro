# Degustação de Chá às Escuras

## Descrição

Este problema faz parte da Competição Ideal de Consumidores de Chá Puro (ICPC), onde os participantes devem identificar diferentes tipos de chá apenas usando seus sentidos do olfato e paladar. Durante o programa, um bule de chá é preparado e servido a cinco competidores, que devem tentar adivinhar o tipo de chá. Os tipos de chá possíveis são:

1. Chá Branco
2. Chá Verde
3. Chá Preto
4. Chá de Ervas

O objetivo é verificar quantos competidores acertaram suas respostas ao identificar o tipo de chá.

## Entrada

- A primeira linha contém um inteiro **T** (1 ≤ T ≤ 4), representando o tipo de chá real.
- A segunda linha contém cinco inteiros **A, B, C, D e E** (1 ≤ A, B, C, D, E ≤ 4), representando as respostas dadas pelos cinco competidores.

## Saída

- A saída deve conter um único inteiro, representando o número de competidores que forneceram a resposta correta.

## Exemplo de Entrada

```
2
1 2 2 3 4
```

## Exemplo de Saída

```
2
```

## Explicação do Exemplo

Neste exemplo, o tipo de chá real é **2** (chá verde). Os competidores deram as seguintes respostas:

- Competidor 1: 1 (Incorreto)
- Competidor 2: 2 (Correto)
- Competidor 3: 2 (Correto)
- Competidor 4: 3 (Incorreto)
- Competidor 5: 4 (Incorreto)

Portanto, dois competidores acertaram a resposta.

## Resolução do Problema

Para resolver este problema, siga os passos abaixo:

1. **Leia a entrada:** Capture o tipo de chá real e as respostas dos competidores.
2. **Compare as respostas:** Verifique quantas respostas dos competidores são iguais ao tipo de chá real.
3. **Conte os acertos:** Mantenha uma contagem das respostas corretas.
4. **Exiba o resultado:** Imprima o número total de respostas corretas.

## Implementação

Aqui está um exemplo de implementação em Python:

```python
# Leitura do tipo de chá real
tipo_cha_real = int(input())

# Leitura das respostas dos competidores
respostas = list(map(int, input().split()))

# Contagem de acertos
acertos = sum(1 for resposta in respostas if resposta == tipo_cha_real)

# Impressão do resultado
print(acertos)
