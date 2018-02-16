class Analise(object):

    def analisaFrase(self, letra, palavra ):

        #Ler lista de tokens
        arquivo = open('keywords.txt', 'r')

        for linha in arquivo:
            token = linha.split(' ')

            print('#####################################################################\n')
            print(letra +' == '+ token[1]) 
            print(palavra +' == '+ token[1])
            print(token)
            vazio= ' '

            if(letra == token[1]):
                return [letra, token[0]]
            elif(palavra == token[1]):
                return [palavra, token[0]]
            elif(str(letra) == " "):
                return [letra, palavra]

        
        return [None, None]



        """if (palavra == 'print' ):
            return [palavra, 'Palavra Reservada']
        elif (palavra == '(' or palavra == ')'):
            return [palavra, 'Operador']
        else:
            return [palav
            ra, 'String']"""

    def verificaFrase(self, frase, nlinha):
        lista = list(frase)
        data = ''
        linha = ''
        numLinha = str(nlinha)

        for i in range(len(lista)):
            linha = linha + str(lista[i])
            condicao = self.analisaFrase(lista[i],linha)
            posicao = i - len(linha)
            print(posicao)

            if(condicao[1] == '1'):
                data += condicao[0] + ' ---> Palavra Reservada ---> '+ numLinha  +' \n'
                linha = ''
            elif(condicao[1] == '2'):
                if(len(linha) == 1):
                    data += condicao[0] + ' ---> Operador ---> '  + numLinha  +' \n'
                    linha = ''
                else:
                    op = str(condicao[0])
                    s = linha.replace(op,'')
                    data += s + ' ---> Identificador ---> '  + numLinha  +' \n'
                    data += condicao[0] + ' ---> Operador ---> '  + numLinha +' \n'
                    linha = ''
            elif(condicao[1] == '3'):
                if(len(linha) == 1):
                    data += condicao[0] + ' ---> Delimitador ---> '  + numLinha  +' \n'
                    linha = ''  
                else:
                    dl = str(condicao[0])
                    s = linha.replace(dl,'')
                    data += s + ' ---> Identificador ---> '  + numLinha +' \n'
                    data += condicao[0] + ' ---> Delimitador ---> '  + numLinha +' \n'
                    linha = ''
            elif(str(condicao[0]) == ' '):
                if(len(linha) == 1):
                    linha = ''  
                else:
                    s = linha.replace(" ",'')
                    print(s)
                    data += s + ' ---> Identificador ---> '  + numLinha +' \n'
                    linha = ''
            else:
                print('haha')
                

        return data