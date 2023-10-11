from modelos import Aluno, Atleta, Turma

virginia = Aluno('Virginia', '19/06/1990', 5)
victor = Atleta('Victor', '29/08/1997', 5, 97)
lista_de_alunos = [victor, virginia]
turma = Turma(lista_de_alunos)

for aluno in turma:
    print(aluno)

print(f'Tamanho da turma: {len(turma)}')