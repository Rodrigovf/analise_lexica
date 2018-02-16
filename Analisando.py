class Analise(object):

    def analisaFrase(self, letra, palavra ): # rece a paavra formada ate o momento e o caracter

        #Ler lista de tokens
        arquivo = open('keywords.txt', 'r')
        print("inicio")
        print(letra)
        print(palavra)

        for linha in arquivo:
            token = linha.split(' ')
            
            if(letra == token[1]):
                return [letra, token[0]]
            elif(palavra == token[1]):
                return [palavra, token[0]]
            elif(str(letra) == " "):
                return [letra, palavra]
        
        return [None, None]

    def verificaFrase(self, frase, numlinha):
        numLinha = str(numlinha)
        lista = list(frase)
        while True:
            try:
                lista.remove('\t')

            except ValueError:
                try:
                    lista.remove('\n')
                except ValueError:
                    break

        data = ''
        linha = ''
        coluna = 0
        contId = 0

        for i in range(len(lista)):

            linha = linha + str(lista[i])
            condicao = self.analisaFrase(lista[i],linha)
            print(str(lista))

            if(condicao[1] == '1'):
                data += condicao[0] + ' | Palavra Reservada | '+ numLinha  +'  | '+ str(coluna) +' \n'
                linha = ''
                coluna = i -1
            elif(condicao[1] == '2'):
                if(len(linha) == 1):
                    data += condicao[0] + ' | Operador | '  + numLinha  +'  | '+ str(coluna) +' \n'
                    linha = ''
                    coluna = i +1
                else:
                    op = str(condicao[0])
                    s = linha.replace(op,'')
                    data += s + ' | Identificador['+str(contId)+'] | '  + numLinha  +'  | '+ str(coluna) +' \n'
                    data += condicao[0] + ' | Operador | '  + numLinha +'  | '+ str(coluna + len(s)) +' \n'
                    linha = ''
                    coluna = i +1
                    contId += 1
            elif(condicao[1] == '3'):
                if(len(linha) == 1):
                    data += condicao[0] + ' | Delimitador | '  + numLinha  +'  | '+ str(coluna) +' \n'
                    linha = ''  
                    coluna = i +1
                else:
                    dl = str(condicao[0])
                    s = linha.replace(dl,'')
                    data += s + ' | Identificador['+str(contId)+'] | '  + numLinha +'  | '+ str(coluna) +' \n'
                    data += condicao[0] + ' | Delimitador | '  + numLinha +'  | '+ str(coluna + len(s)) +' \n'
                    linha = ''
                    coluna = i +1
                    contId += 1
            elif(str(condicao[0]) == ' '):
                if(len(linha) == 1):
                    linha = ''  
                    coluna = i +1
                else:
                    s = linha.replace(" ",'')
                    data += s + ' | Identificador['+str(contId)+'] | '  + numLinha +'  | '+ str(coluna) +' \n'
                    linha = ''
                    coluna = i +1
                    contId += 1
                

        if(len(linha) > 0):
            data += linha + ' | Identificador['+str(contId)+'] | '  + numLinha +' \n'
            linha = ''  
        
        return data