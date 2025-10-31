from Aluno import Aluno
from Curso import Curso
from Disciplina import Disciplina
from Pessoa import Pessoa
from Professor import Professor
from Turma import Turma

Prof1 = Professor()
Prof2 = Professor()
Turma1 = Turma()
Turma2 = Turma()
Turma3 = Turma()
Turma4 = Turma()
Curso1 = Curso()
Curso2 = Curso()

Aluno1 = Aluno()
Aluno1.set_Alunoid(1)
Aluno1.set_nome("Maria")
Aluno1.set_idade(20)
Aluno1.set_matriculaAluno("91234")

Aluno2 = Aluno()
Aluno2.set_Alunoid(2)
Aluno2.set_nome("Pedro")
Aluno2.set_idade(22)
Aluno2.set_matriculaAluno("92345")

Aluno3 = Aluno()
Aluno3.set_Alunoid(3)
Aluno3.set_nome("Rafael")
Aluno3.set_idade(18)
Aluno3.set_matriculaAluno("84321")

Aluno4 = Aluno()
Aluno4.set_Alunoid(4)
Aluno4.set_nome("Márcia")
Aluno4.set_idade(21)
Aluno4.set_matriculaAluno("71234")

Prof1.set_Professorid(1)
Prof1.set_nome("João")
Prof1.set_matriculaProf("12345")

Prof2.set_Professorid(2)
Prof2.set_nome("Joana")
Prof2.set_matriculaProf("54321")

Curso1.set_Cursoid(1)
Curso1.set_nome("Eng. de Software")
Curso2.set_Cursoid(2)
Curso2.set_nome("Arquitetura")

Turma1.set_id(101)
Turma1.set_disciplina("Matemática")
Turma1.set_professor(Prof1)

Turma2.set_id(102)
Turma2.set_disciplina("Português")
Turma2.set_professor(Prof2)

Turma3.set_id(103)
Turma3.set_disciplina("Inglês")
Turma3.set_professor(Prof2)

Curso1.add_turma(Turma1)
Curso1.add_turma(Turma2)
Curso1.add_turma(Turma3)

Curso1.add_aluno(Aluno1)
Curso1.add_aluno(Aluno2)
Curso1.add_aluno(Aluno3)
Curso1.add_aluno(Aluno4)

Turma1.add_aluno(Aluno1)
Turma1.add_aluno(Aluno2)
Turma2.add_aluno(Aluno1)
Turma2.add_aluno(Aluno3)
Turma3.add_aluno(Aluno2)
Turma3.add_aluno(Aluno4)

print("_____________________________________________________________________________________")
print("Exercício 1: Imprimir o nome do professor da turma")
Turma1.prof_turma()
print("_____________________________________________________________________________________")
print("Exercício 2: Imprimir os nomes dos alunos da turma")
Turma3.alunos_turma()
print("_____________________________________________________________________________________")
print("Exercício 3: Imprimir o nome do professor de alguma turma de um curso")
Curso1.professor_turma()
Curso2.professor_turma()
print("_____________________________________________________________________________________")
print("Exercício 4: Imprimir os nomes dos alunos que estão em alguma turma de um curso")
Curso1.alunos_turma()
print("_____________________________________________________________________________________")
print("Exercício 5: Imprimir os nomes dos alunos que estão registrados em um curso")
Curso1.retorno_listar_alunos()
print("_____________________________________________________________________________________")
print("Exercício 6: Imprimir quais disciplinas estão em alguma turma de um curso")
Curso1.obter_disciplinas()
Curso2.obter_disciplinas()
print("_____________________________________________________________________________________")
print("Exercício 7: Verificar se um aluno está em uma turma")
Turma1.pesquisa_aluno(Aluno4)
print("_____________________________________________________________________________________")
print("Exercício 8: Verificar se um aluno está em um curso")
Curso1.pesquisa_aluno(Aluno1)
print("_____________________________________________________________________________________")
print("Exercício 9: Verificar se uma turma está em um curso")
Curso1.pesquisa_turma(Turma3)
print("_____________________________________________________________________________________")
print("Exercício 10: Excluir um aluno de uma turma")
Turma1.rem_aluno(Aluno1)
print("_____________________________________________________________________________________")
print("Exercício 11: Excluir uma turma de um curso")
Curso1.rem_turma(Turma1)
print("_____________________________________________________________________________________")

for aluno in Curso1.get_Alunos():
    print("-", aluno.get_nome())

print("Exercício 12: Excluir um aluno de um curso")
Curso1.rem_aluno_curso(Aluno4)
print("_____________________________________________________________________________________")

for aluno in Curso1.get_Alunos():
    print("-", aluno.get_nome())