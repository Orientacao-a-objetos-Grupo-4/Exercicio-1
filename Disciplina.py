class Disciplina():
    def __init__(self):
        self.__id = None
        self.__nome = None
        self.__turmas = []

    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome

    def add_turma(self, turma):
        self.__turmas.append(turma)

    def get_turmas(self):
        return self.__turmas