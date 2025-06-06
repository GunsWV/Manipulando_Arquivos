arquivo = open('arquivo.txt', 'a', encoding='utf-8')

#Adciona uma nova linha
arquivo.write("Adicionamos uma nova linha ao arquivo. \n")
arquivo.write('Esta é uma linha adicional. \n')
#Feche o arquivo
arquivo.close()