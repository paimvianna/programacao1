#Entrada
#sal = float(input("Informe o salário do colaborador: "))
#percent = float(input("Informe a porcentagem do reajuste do salário do colaborador: "))

#Processamento
#reajust = ((100 + percent) * sal) / 100

#Saída
#print ('O valor do salário reajustado e de: ',reajust)

#OBS: tenho que descobrir como fazer ficar definido somente com duas casas decimais, outra coisa se eu fizer o valor da percent ja divido por 100 ja na entrada teria problema.

#Entrada
sal = float(input("Informe o salário do colaborador: "))
percent = float(input("Informe a porcentagem do reajuste do salário do colaborador: "))/100 #percebi que o valor so pode ser dividido apos ele ser como ponto flutuante. e que o ficou muito mais exato

#Processamento
reajust = (1 + percent) * sal

#Saída
print (F"O valor do salário reajustado e de: {reajust:.2f}") #achei a resposta no livro pag 48 truncamento do valor de pi
