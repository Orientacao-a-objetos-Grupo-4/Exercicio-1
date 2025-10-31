from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self):
        super().__init__()
        self.__id = None
        self.__matricula = None
        self.__cursos = []

    def get_Alunoid(self):
        return self.__id
    def set_Alunoid(self, id):
        self.__id = id

    def get_matriculaAluno(self):
        return self.__matricula
    def set_matriculaAluno(self, matricula):
        self.__matricula = matricula

    def get_cursos(self):
        return self.__cursos
    def set_cursos(self, cursos):
        self.__cursos = cursos
    def add_curso(self, curso):
        self.__cursos.append(curso)
    def rem_curso(self, curso):
        self.__cursos.remove(curso)