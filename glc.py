#arquivo_gramatica = open("inp-glc.txt", 'r')
#arquivo_cadeias = open("inp-cadeias.txt", 'r')

index = 0
primeira_linha = True
numero_de_gramaticas = 0
gramaticas = []
index_da_gramatica_lida = 0
preenchimento_inicial = False
'''
for linha in arquivo_gramatica:

    if  preenchimento_inicial and index > 2 + gramaticas[index_da_gramatica_lida]['numero_de_regras']:
        index = 0
        index_da_gramatica_lida += 1
        preenchimento_inicial = False

    if index == 0 and primeira_linha: 

        numero_de_gramaticas = int(linha)

        for i in range(int(numero_de_gramaticas)):
            gramaticas.append({})

    elif index == 0 and primeira_linha == False:
        
        parametros = linha.split()
        gramaticas[index_da_gramatica_lida]['numero_de_variaveis'] = int(parametros[0])
        gramaticas[index_da_gramatica_lida]['numero_de_terminais'] = int(parametros[1])
        gramaticas[index_da_gramatica_lida]['numero_de_regras'] = int(parametros[2])
        gramaticas[index_da_gramatica_lida]['regras'] = []

        index += 1

    elif index == 1 and primeira_linha == False:
    
        gramaticas[index_da_gramatica_lida]['variaveis'] = linha.split()
        index += 1

    elif index == 2 and primeira_linha == False:
    
        gramaticas[index_da_gramatica_lida]['terminais'] = linha.split()
        index += 1

    elif index >= 3 and index <= 2 + gramaticas[index_da_gramatica_lida]['numero_de_regras'] :
        gramaticas[index_da_gramatica_lida]['regras'].append(linha.split())

        preenchimento_inicial = True
        index += 1
        
    
    primeira_linha = False
'''

def crie_matriz(n_linhas, n_colunas, valor):
        matriz = []

        for i in range(n_linhas):
            linha = []

            for j in range(n_colunas):
                linha.append(valor)

            matriz.append(linha)

        return matriz

def verificar_cadeia(cadeia_resposta_, gramatica):
    cadeia_resposta = '*' + cadeia_resposta_
    variavel_inicial = gramatica['variaveis'][0]
    regras_especiais = [] # Regras no formato A => BC

    for regra in gramatica['regras']:
        if len(regra[2]) == 2:
            regras_especiais.append(regra)

    if cadeia_resposta_ == '&':
        for regra in gramatica['regras']:
            if regra[0] == variavel_inicial and regra[2] == '&':
                print('foi')
                return True

    matriz = crie_matriz(len(cadeia_resposta_) + 1, len(cadeia_resposta_) + 1, '')

    for i in range(1, len(cadeia_resposta)):
        for A in gramatica['variaveis']:
            if [A, '=>', cadeia_resposta[i]] in gramatica['regras']:
                matriz[i][i] += A + ' '

    
    for l in range(2, len(cadeia_resposta)):
        for i in range(1, len(cadeia_resposta) - l + 1):
            j = i + l - 1
            for k in range(i, j - 1 + 1):
                for regra in regras_especiais:
                    matriz_copia = matriz.copy()
                    if regra[2][0] in matriz_copia[i][k].split(' ') and regra[2][1] in matriz_copia[k + 1][j].split(' '):
                        matriz[i][j] += regra[0] + ' '


    print(matriz[6][6])
verificar_cadeia('abaabb', {
        'numero_de_variaveis': 6, 
        'numero_de_terminais': 2, 
        'numero_de_regras': 15, 
        'regras': [
            ['Z', '=>', '&'], 
            ['Z', '=>', 'AT'], 
            ['Z', '=>', 'BU'], 
            ['Z', '=>', 'SS'], 
            ['Z', '=>', 'AB'], 
            ['Z', '=>', 'BA'], 
            ['S', '=>', 'AT'], 
            ['S', '=>', 'BU'], 
            ['S', '=>', 'SS'], 
            ['S', '=>', 'AB'], 
            ['S', '=>', 'BA'], 
            ['T', '=>', 'SB'], 
            ['U', '=>', 'SA'], 
            ['A', '=>', 'a'], 
            ['B', '=>', 'b']], 
        'variaveis': ['Z', 'S', 'T', 'U', 'A', 'B'], 
        'terminais': ['a', 'b']
    })

'''
print(gramaticas)
[
    {
        'numero_de_variaveis': 6, 
        'numero_de_terminais': 2, 
        'numero_de_regras': 15, 
        'regras': [
            ['S0', '=>', '&'], 
            ['S0', '=>', 'AT'], 
            ['S0', '=>', 'BU'], 
            ['S0', '=>', 'SS'], 
            ['S0', '=>', 'AB'], 
            ['S0', '=>', 'BA'], 
            ['S', '=>', 'AT'], 
            ['S', '=>', 'BU'], 
            ['S', '=>', 'SS'], 
            ['S', '=>', 'AB'], 
            ['S', '=>', 'BA'], 
            ['T', '=>', 'SB'], 
            ['U', '=>', 'SA'], 
            ['A', '=>', 'a'], 
            ['B', '=>', 'b']], 
        'variaveis': ['S0', 'S', 'T', 'U', 'A', 'B'], 
        'terminais': ['a', 'b']
    }, 
    {
        'numero_de_variaveis': 3, 
        'numero_de_terminais': 2, 
        'numero_de_regras': 3, 
        'regras': [
            ['S1', '=>', 'AB'], 
            ['A', '=>', '0'], 
            ['B', '=>', '1']], 
            'variaveis': ['S1', 'A', 'B'], 
            'terminais': ['0', '1']
    }
]


'''