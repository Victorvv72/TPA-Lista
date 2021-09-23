nome = str(input('Digite o nome do aluno: '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segundo nota: '))
n3 =  float(input('Digite a terceiro nota: '))
media = (n1 + n2 + n3) / 3
if media > 7:
    print ('Parabéns {} você passou'.format (media, nome))
if media <= 7 and media >= 5:
    print ('{} você ficou com a média'.format (media, nome))
if media < 5:
    print ('{} ESTÁ REPROVADO'.format (media))