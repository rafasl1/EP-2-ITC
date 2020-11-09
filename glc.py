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
def verificar_cadeia(cadeia_resposta, gramatica, cadeia_atual, numero_de_chamadas):
 
    vetor_cadeia_resposta = list(cadeia_resposta)
    vetor_cadeia_atual = list(cadeia_atual)
    cadeia_finalizada = True
    if len(cadeia_atual) > len(cadeia_resposta):
        return

    for i in vetor_cadeia_atual:
        if i in gramatica['variaveis']:
            cadeia_finalizada = False
            break
    if cadeia_finalizada:
        if len(cadeia_atual) == 0 and cadeia_resposta == '&':
            print('Deu bom')
            return 1
        if cadeia_atual == cadeia_resposta:
            print("Deu bom")
            return 1
    

    if len(vetor_cadeia_atual) > 0:
        for index, i in enumerate(cadeia_atual):
            if i in gramatica['terminais']:
                pass
            else:
                for j in gramatica['regras']:

                    if i == j[0]:
                        vetor_de_substituicoes = j[2:]
                        for k in vetor_de_substituicoes:
                            if k != '&':
                                vetor_cadeia_atual_novo =  vetor_cadeia_atual.copy()
                                vetor_cadeia_atual_novo[index] = k
                                cadeia_nova = ''.join(vetor_cadeia_atual_novo)

                                try:
                                    resposta = verificar_cadeia(cadeia_resposta, gramatica, cadeia_nova, numero_de_chamadas + 1)
                                    if resposta == 1:
                                        return 1
                                except:
                                    print('bugou')
                                    return
                            else:
                                vetor_cadeia_atual_novo =  vetor_cadeia_atual.copy()
                                vetor_cadeia_atual_novo.pop(index)
                                if len(vetor_cadeia_atual) == 0:
                                    if cadeia_resposta == '&':
                                        print('Deu bom')
                                        return 1
                                else :
                                    cadeia_nova = ''.join(vetor_cadeia_atual_novo)
                                    try:
                                        resposta = verificar_cadeia(cadeia_resposta, gramatica, cadeia_nova, numero_de_chamadas + 1)
                                        if resposta == 1:
                                            return 1
                                    except:
                                        print('bugou ')
                                        return


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
    }, 'Z', 1 )


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