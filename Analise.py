import Analisando

analise = Analisando.Analise()

arquivo = open('arquivo.txt', 'r')
arquivo2 = open('arquiTXT.txt', 'w')
data = ''
"""codigo = arquivo.readlines()"""
numLinha =0
for frase in arquivo:
    strNumLinha = str(numLinha)
    data += analise.verificaFrase(frase,numLinha)
    numLinha+=1
    print(data)
    

arquivo2.writelines(data)