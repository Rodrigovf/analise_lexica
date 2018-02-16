import Analisando

analise = Analisando.Analise()

arquivo = open('arquivo.txt', 'r')
arquivo2 = open('arquiTXT.txt', 'w')
data = ''
"""codigo = arquivo.readlines()"""
numLinha =0
for frase in arquivo:
    numLinha+=1
    strNumLinha = str(numLinha)
    data += analise.verificaFrase(frase,numLinha)
    print(data)
    

arquivo2.writelines(data)