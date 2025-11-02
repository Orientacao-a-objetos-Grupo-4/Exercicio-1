# from Turma import Turma
from Aluno import Aluno


class Curso():
    def __init__ (self):
        self.__id = None
        self.__nome = None
        self.__turmas = []
        self.__alunos = []
    
    def get_Cursoid(self):
        return self.__id
    def set_Cursoid(self, id):
        self.__id = id
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
    def get_turmas(self):
        return self.__turmas
    def set_turmas(self, turmas):
        self.__turmas = turmas
    
    def add_turma(self, turma):
        self.__turmas.append(turma)
    def rem_turma(self, turma):
        self.__turmas.remove(turma)

    def get_Alunos(self):
        return self.__alunos
    
    def set_Alunos(self, alunos):
        self.__alunos = alunos

    def add_aluno(self, aluno):
        self.__alunos.append(aluno)
        if self not in aluno.get_cursos():
            aluno.add_curso(self)

    def remove_aluno(self, aluno):
        self.__alunos.remove(aluno)

    def set_alunos(self, turmas):
        self.__turmas = turmas
    
    def professor_turma(self):
        for turma in self.get_turmas():
            print(f"O professor da turma {turma.get_id()}  do curso  {self.get_nome()} é {turma.get_professor().get_nome()}.")

    def alunos_turma(self):
        for turma in self.get_turmas():
            print(f"Alunos da turma {turma.get_id()}:")
            for aluno in turma.get_alunos():
                print("-", aluno.get_nome())

    def listar_alunos(self):
        aluno_curso = []
        for turma in self.get_turmas():
            for aluno in turma.get_alunos():
                if aluno not in aluno_curso:
                    aluno_curso.append(aluno)
        return aluno_curso
    
    def alunos_curso(self):
        print("Os alunos registrados no curso", self.get_nome(), "são:")
        for aluno in self.get_Alunos():
            print("-", aluno.get_nome())
    
    def retorno_listar_alunos(self):
        print("Os alunos registrados no", self.get_nome(), "são:")
        for aluno in self.listar_alunos():
            print("-", aluno.get_nome())
    
    def obter_disciplinas(self):
        print("Dentro do curso de", self.get_nome(), "o aluno cursará as disciplinas:")
        for turma in self.get_turmas():
            print("-", turma.get_disciplina())

    def pesquisa_aluno(self, aluno):
        if aluno in self.get_Alunos():
            print(f"O(a) aluno {aluno.get_nome()} está matriculado(a) no curso de {self.get_nome()}.")
        else:
            print(f"O(a) aluno {aluno.get_nome()} não está matriculado(a) no curso de {self.get_nome()}.")

    def pesquisa_turma(self, turma):
        if turma in self.get_turmas():
            print(f"A turma {turma.get_id()} faz parte do curso de {self.get_nome()}.")
        else:
            print(f"A turma {turma.get_id()} não faz parte do curso de {self.get_nome()}.")
    
    def rem_aluno_curso(self, aluno):
        aluno_rem_curso = False
        for turma in self.__turmas:
            if turma.rem_aluno(aluno):
                aluno_rem_curso = True
        if aluno_rem_curso:
            if aluno in self.__alunos:
                self.remove_aluno(aluno)
            print(f"O aluno {aluno.get_nome()} foi excluído com sucesso do curso {self.__nome}!")
        else:
            print(f"O aluno {aluno.get_nome()} não pertence ao curso {self.__nome}.")

    def retorno_rem_turma(self, turma):
        if turma in self.__turmas:
            self.rem_turma(turma)
            print(f"A turma {turma.get_id()} foi excluída com sucesso do curso {self.__nome}!")
        else:
            print(f"A turma {turma.get_id()} não pertence ao curso {self.__nome}.")