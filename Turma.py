from Curso import Curso
class Turma():
    def __init__ (self):
        self.__id = None
        self.__disciplina = None
        self.__alunos = []
        self.__professor = None
    
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id
    def get_disciplina(self):
        return self.__disciplina
    def set_disciplina(self, disciplina):
        self.__disciplina = disciplina
    def get_alunos(self):
        return self.__alunos
    def set_alunos(self, alunos):
        self.__alunos = alunos
    def get_professor(self):
        return self.__professor
    def set_professor(self, professor):
        self.__professor = professor
    
    def add_aluno(self, aluno, curso):
        self.__alunos.append(aluno)
        if curso in curso.get_turmas():
            if aluno not in curso.get_Alunos():
                curso.add_aluno(aluno)

    def rem_aluno(self, aluno):
        if aluno in self.__alunos:
            self.__alunos.remove(aluno)
            return True
        else:
            return False

    def retorno_rem_aluno(self, aluno):
        if self.rem_aluno(aluno):
            print(f"O aluno {aluno.get_nome()} foi excluído com sucesso da turma {self.__id}.")
        else:
            print(f"O aluno {aluno.get_nome()} não pertence à turma {self.__id}.")

    def prof_turma (self):
        print(f"O professor da Turma {self.get_id()} é o {self.get_professor().get_nome()}.")

    def alunos_turma(self):
        print("Os alunos da Turma", self.get_id(), "são:")
        for aluno in self.get_alunos():
            print("-", aluno.get_nome())

    def pesquisa_aluno(self, aluno):
        if aluno in self.get_alunos():
            print(f"O(a) aluno {aluno.get_nome()} está matriculado(a) na turma {self.get_id()}.")
        else:
            print(f"O(a) aluno {aluno.get_nome()} não está matriculado(a) na turma {self.get_id()}.")