vetor_regra = ['S', '=>', 'B']

primeira_parte = vetor_regra[:2]
segunda_parte = vetor_regra[2:]

segunda_parte_nova = ''.join(segunda_parte)

primeira_parte.append(segunda_parte_nova)

print(primeira_parte)