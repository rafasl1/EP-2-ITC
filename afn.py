import sys

arquivo_teste = open(sys.argv[1], 'r')
arquivo_saida = open(sys.argv[2], 'w')

index = 0
numero_de_automatos = 0
numero_de_automatos_lidos = 0
automatos = []
primeira_linha = True
index_do_automato_lido = 0
preenchimento_inicial = False
string_de_saida = ''

for linha in arquivo_teste:
	# condição para verificar se todas as informações do automato já foram gravadas em variaveis
	if  preenchimento_inicial and index > automatos[index_do_automato_lido]['numero_de_transicoes'] + 2 + automatos[index_do_automato_lido]['numero_de_cadeias']:
		# atribuição de valores para indicar que foi um automato foi lido completamente e resetar o index do loop
		index = 0;
		index_do_automato_lido += 1
		preenchimento_inicial = False

	# verificar se a linha que está sendo lida é a primeira do arquivo
	if index == 0 and primeira_linha == True:
		numero_de_automatos = int(linha)

		# inicializa um dicionário vazio para cada automato
		for i in range(int(numero_de_automatos)):
			automatos.append({})
	# verificar se está sendo lida a primeira linha de configuração do automato
	elif index == 0 and primeira_linha == False:
		# preenchimento das configurações de cada automato
		parametros = linha.split()
		automatos[index_do_automato_lido]['numero_de_estados'] = int(parametros[0])
		automatos[index_do_automato_lido]['numero_de_simbolos'] = int(parametros[1])
		automatos[index_do_automato_lido]['numero_de_transicoes'] = int(parametros[2])
		automatos[index_do_automato_lido]['index_do_estado_inicial'] = int(parametros[3])
		automatos[index_do_automato_lido]['numero_de_estados_de_aceitacao'] = int(parametros[4])
		automatos[index_do_automato_lido]['transicoes'] = []
		automatos[index_do_automato_lido]['cadeias'] = []

		index += 1
	# verifica se a linha é a primeira lida depois do preenchimento de configurações iniciais
	elif index == 1 and primeira_linha == False:
		# preenche as informações do automato
		automatos[index_do_automato_lido]['estados_de_aceitacao'] = linha.split()
		index += 1
	# verifica se a linha lida é a proxima apos ter preenchido a configuração de estados de aceitação
	elif index >= 2 and index <= automatos[index_do_automato_lido]['numero_de_transicoes'] + 1 and primeira_linha == False:
		# preenche as informações do automato
		automatos[index_do_automato_lido]['transicoes'].append(linha.split())
		index += 1
	# verifica se a linha lida é a proxima apos ter preenchido a configuração de transições
	elif index > automatos[index_do_automato_lido]['numero_de_transicoes'] + 1 and index <= automatos[index_do_automato_lido]['numero_de_transicoes'] + 2 and primeira_linha == False:
		# preenche configurações do automato
		automatos[index_do_automato_lido]['numero_de_cadeias'] = int(linha)
		# indica que as configurações já foram preenchidas
		preenchimento_inicial = True

		index += 1
	# verifica se a linha lida é a proxima apos ter preenchido a configuração de numero de cadeias
	elif index > automatos[index_do_automato_lido]['numero_de_transicoes'] + 2 and index <= automatos[index_do_automato_lido]['numero_de_transicoes'] + 2 + automatos[index_do_automato_lido]['numero_de_cadeias'] and primeira_linha == False: 
		automatos[index_do_automato_lido]['cadeias'].append(linha.split())
		index += 1;
	# indica para o loop que não é a primeira linha que está sendo lida do automato
	primeira_linha = False


def verificar_cadeira(cadeia, automato, estado_atual):

	# verifica se a cadeia que está sendo lida já foi consumida completamente
    if len(cadeia) == 0:
		# verifica se os estados de aceitação incluem o ultimo estado
        if str(estado_atual) in automato['estados_de_aceitacao']:
			# indica no arquivo auxiliar que cadeia foi aceita
            aux = open('verificacao_automato.txt', 'a')
            aux.write('1 ')
            aux.close()

		# verifica se há uma transição no vazio do ultimo estado caso a cadeia já tenha sido consumida completamente
        else:
            for transicao in automato['transicoes']:
                if str(estado_atual) == str(transicao[0]) and str(transicao[1]) == '0':
                    cadeia_consumida = cadeia.copy()
                    try:
						# tenta chamar a função recursivamente indicando o estado apos a transição no vazio 
                    	verificar_cadeira(cadeia_consumida, automato, transicao[2])
                    except:
						# para o casos de loop infinito onde a pilha de execução é estourada, sai da função
                    	return

        return
	# caso a cadeia não tenha sido consumida completamente
    else:
        simbolo_atual = cadeia[0]

        for transicao in automato['transicoes']:

			# verificando se o estado referente a transição em questão coincide com o estado atual 
			# e se o simbolo da transição coincide com o simbolo atual
            if str(estado_atual) == str(transicao[0]) and str(simbolo_atual) == str(transicao[1]):
				# clona a cadeia e remove o simbolo consumido
                cadeia_consumida = cadeia.copy()
                cadeia_consumida.pop(0)
                try:
					# tenta chamar recursivamente a função após a cadeia ter sido consumida
                	verificar_cadeira(cadeia_consumida, automato, transicao[2])
                except:
                	return
			# verifica se há uma transição no vazio que parte do estado atual
            if str(estado_atual) == str(transicao[0]) and str(transicao[1]) == '0':
                cadeia_consumida = cadeia.copy()
                try:
					# tenta chamar recursivamente a função a partir do novo estado após a transição
                	verificar_cadeira(cadeia_consumida, automato, transicao[2])
                except:
                	return


for i in range(numero_de_automatos):
	automato = automatos[i]

	# verifica cada cadeia de cada automato
	for cadeia in automato['cadeias']:
		# chama a função para a cadeia em questão 
		verificar_cadeira(cadeia, automato, automato['index_do_estado_inicial'])
		# variavel para ler o conteudo do arquivo auxiliar
		aux = open('verificacao_automato.txt', 'r')

		conteudo = aux.readline()
		aux.close()
		aux = open('verificacao_automato.txt', 'r')

		# verifica se a linha do arquivo auxiliar é vazia, ou seja, que cadeia não foi aceita
		if not bool(conteudo):
			# preenche a string de saida com 0, indicando a não aceitação
			string_de_saida += '0 '
		# caso a linha não seja vazia, verifica se há um numero 1 dentro da linha, o que indica que a cadeia foi aceita
		for linha in aux:
			vetor = linha.split()
			if('1' in vetor):
				# preenche a string de saida com 1, indicando a aceitação
				string_de_saida += '1 '
			else :
				# preenche a string de saida com 0, indicando a não aceitação
				string_de_saida += '0 '

		aux.close()
		aux = open('verificacao_automato.txt', 'w')
		# reseta o arquivo auxiliar para verificação de cadeia
		aux.write('')
		aux.close()

	# pula um linha para verificação do próximo automato
	string_de_saida += '\n'

# grava string de saida no arquivo final
arquivo_saida.write(string_de_saida)
arquivo_teste.close()