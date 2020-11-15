arquivo_gramatica = open("inp-glc.txt", 'r')
arquivo_cadeias = open("inp-cadeias.txt", 'r')
string_de_saida = ''

index = 0
primeira_linha = True
numero_de_gramaticas = 0
gramaticas = []
index_da_gramatica_lida = 0
preenchimento_inicial = False

for linha in arquivo_gramatica:
	# condição para verificar se todas as informações da gramatica já foram gravadas em variaveis
    if  preenchimento_inicial and index > 2 + gramaticas[index_da_gramatica_lida]['numero_de_regras']:
        # atribuição de valores para indicar que uma gramatica foi lida completamente e resetar o index do loop
        index = 0
        index_da_gramatica_lida += 1
        preenchimento_inicial = False
    
	# verificar se a linha que está sendo lida é a primeira do arquivo
    if index == 0 and primeira_linha: 

        numero_de_gramaticas = int(linha)

        #incializa um dicionario vazio para cada gramatica
        for i in range(int(numero_de_gramaticas)):
            gramaticas.append({})

	# verificar se está sendo lida a primeira linha de configuração da gramtatica
    elif index == 0 and primeira_linha == False:
        
		# preenchimento das configurações de cada gramatica
        parametros = linha.split()
        gramaticas[index_da_gramatica_lida]['numero_de_variaveis'] = int(parametros[0])
        gramaticas[index_da_gramatica_lida]['numero_de_terminais'] = int(parametros[1])
        gramaticas[index_da_gramatica_lida]['numero_de_regras'] = int(parametros[2])
        gramaticas[index_da_gramatica_lida]['regras'] = []

        index += 1

	# verifica se a linha é a primeira lida depois do preenchimento de configurações iniciais
    elif index == 1 and primeira_linha == False:
    
        gramaticas[index_da_gramatica_lida]['variaveis'] = linha.split()
        index += 1

	# verifica se a linha lida é a proxima apos ter preenchido a configuração de variaveis
    elif index == 2 and primeira_linha == False:
    
        gramaticas[index_da_gramatica_lida]['terminais'] = linha.split()
        index += 1

	# verifica se a linha lida é a proxima apos ter preenchido a configuração de terminais
    elif index >= 3 and index <= 2 + gramaticas[index_da_gramatica_lida]['numero_de_regras'] :
        # une todos os elementos finais de uma transicao em uma unica string e preenche a configuracao de regras
        final_regra = linha.split()[2:]
        final_regra = ''.join(final_regra)
        inicio_regra = linha.split()[:2]
        inicio_regra.append(final_regra)
        gramaticas[index_da_gramatica_lida]['regras'].append(inicio_regra)

        preenchimento_inicial = True
        index += 1
        
	# indica para o loop que não é a primeira linha que está sendo lida da gramatica
    primeira_linha = False


#reinicia as variaveis para leitura das cadeias pelo arquivo
index = 0
primeira_linha = True
index_da_gramatica_lida = 0
preenchimento_inicial = False
cadeias = {}
numero_de_cadeias = 0
primeira_leitura = True

for linha in arquivo_cadeias:
	# condição para verificar se todas as informações das cadeias de cada gramatica já foram gravadas
    if preenchimento_inicial and index >= numero_de_cadeias:
        index = 0
        primeira_linha = True
        preenchimento_inicial = False
        index_da_gramatica_lida += 1

    # incializa um dicionario vazio como um vetor para cada uma das gramaticas tendo o nome do campo como o index da gramatica
    if index == 0 and primeira_linha:
        numero_de_cadeias = int(linha)
        if primeira_leitura:
            for i in range(int(numero_de_gramaticas)):
                cadeias['{}'.format(i)] = []
            primeira_leitura = False
        primeira_linha = False

    # retira os espacos da cadeia e coloca dentro das regras da respectiva gramatica
    elif index >= 0 and index < numero_de_cadeias and primeira_linha == False:
        preenchimento_inicial = True
        string_cadeia = "".join(linha.split())
        cadeias['{}'.format(index_da_gramatica_lida)].append(string_cadeia)
        index += 1


# funcao para criar matriz (funcao nao autoral)
def crie_matriz(n_linhas, n_colunas, valor):
        matriz = []

        for i in range(n_linhas):
            linha = []

            for j in range(n_colunas):
                linha.append(valor)

            matriz.append(linha)

        return matriz

# funcao para implementar o algoritmo de CYK
def verificar_cadeia(cadeia_resposta_, gramatica):
    # adiciona um elemento na string para que possa ser usado os mesmos index do que o código passado em aula
    cadeia_resposta = '*' + cadeia_resposta_
    variavel_inicial = gramatica['variaveis'][0]
    regras_especiais = [] # Regras no formato A => BC

    # regras no formato A => BC
    for regra in gramatica['regras']:
        if len(regra[2]) == 2:
            regras_especiais.append(regra)

    # implementacao do algoritmo CYK em si

    if cadeia_resposta_ == '&':
        for regra in gramatica['regras']:
            if regra[0] == variavel_inicial and regra[2] == '&':
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


    return gramatica['variaveis'][0] in matriz[1][len(cadeia_resposta_)].split()

# itera pelas gramaticas e chama a funcao para as suas respectivas cadeias
for i in range(0, numero_de_gramaticas):
    for cadeia in cadeias['{}'.format(i)]:
        cadeia_aceita = verificar_cadeia(cadeia,gramaticas[i])
        if cadeia_aceita:
            # se a cadeia for aceita preenche com 1
            string_de_saida += '1 '
        else:
            # se a cadeia for aceita preenche com 0
            string_de_saida += '0 '
    string_de_saida += '\n'


# fecha os arquivos
arquivo_cadeias.close()
arquivo_gramatica.close()

# escreve a string de saida no arquivo de resposta
arquivo_saida = open("out-status.txt", 'w')
arquivo_saida.write(string_de_saida)
arquivo_saida.close()