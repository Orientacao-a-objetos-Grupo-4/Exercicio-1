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

print("O professor da Turma", Turma1.get_id(), "é o", Turma1.get_professor().get_nome())
