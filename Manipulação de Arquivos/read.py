arquivo = open("arquivo.txt", "r", encoding="utf-8")
# Leitura de arquivo
conteudo = arquivo.read()
#Imprimir o conteúdo do arquivo
print(conteudo)
#Fechar arquivo
arquivo.close()