from Aluno import Aluno
from Curso import Curso
from Disciplina import Disciplina
from Pessoa import Pessoa
from Professor import Professor
from Turma import Turma


Prof1 = Professor()
Turma1 = Turma()

Prof1.set_Professorid(1)
Prof1.set_nome("João")
Prof1.set_matriculaProf("12345")

Turma1.set_id(101)
Turma1.set_disciplina("Matemática")
Turma1.set_professor(Prof1)

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

# Exercício 1: Imprimir o nome do professor da turma

print("O professor da Turma", Turma1.get_id(), "é o", Turma1.get_professor().get_nome())

# Exercício 2: Imprimir os nomes dos alunos da turma

Turma1.add_aluno(Aluno1)
Turma1.add_aluno(Aluno2)

print("Os alunos da Turma", Turma1.get_id(), "são:")

for aluno in Turma1.get_alunos():
    print("-", aluno.get_nome())