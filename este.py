#Escreva um programa que receba uma sequência digitada pelo usuário e a salve num arquivo no formato fasta.   

#criando caixa de escrita para o usuário
arquivo = input("digite sua sequencia: ")

#criando variável para poder escrever no arquivo designado
arq = open("arquivo.fasta", "w")

#variável podendo escrever e mandar pro arquivo
arq.write(arquivo)

#imprimindo a mensagem enviada pela escrita da variável
print(arquivo)

#fchando arquivo
arq.close()

