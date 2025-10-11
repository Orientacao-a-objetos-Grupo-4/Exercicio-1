class Turma():
    def __init__ (self):
        self.__id = None
        self.__disciplina = None
        self.__alunos = []
        self.__professor = None
        self.__curso = None
    
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
    def get_curso(self):
        return self.__curso
    def set_curso(self, curso):
        self.__curso = curso

    