class Turma():
    def __init__ (self):
        self.__id = None
        self.__disciplina = None
        self.__alunos = []
    
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