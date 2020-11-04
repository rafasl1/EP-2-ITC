arquivo_gramatica = open("inp-glc.txt", 'r')
arquivo_cadeias = open("inp-cadeias.txt", 'r')

index = 0
primeira_linha = True
numero_de_gramaticas = 0
gramaticas = []
index_da_gramatica_lida = 0
preenchimento_inicial = False

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



print(gramaticas)


'''

[
    {
        'numero_de_variaveis': 6, 
        'numero_de_terminais': 2, 
        'numero_de_regras': 15, 
        'regras': [
            ['S0', '=>', '&'], 
            ['S0', '=>', 'A', 'T'], 
            ['S0', '=>', 'B', 'U'], 
            ['S0', '=>', 'S', 'S'], 
            ['S0', '=>', 'A', 'B'], 
            ['S0', '=>', 'B', 'A'], 
            ['S', '=>', 'A', 'T'], 
            ['S', '=>', 'B', 'U'], 
            ['S', '=>', 'S', 'S'], 
            ['S', '=>', 'A', 'B'], 
            ['S', '=>', 'B', 'A'], 
            ['T', '=>', 'S', 'B'], 
            ['U', '=>', 'S', 'A'], 
            ['A', '=>', 'a'], 
            ['B', '=>', 'b']], 
        'variaveis': ['S0', 'S', 'T', 'U', 'A', 'B'], 
        'terminais': ['a', 'b']}, 
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