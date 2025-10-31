class Disciplina():
    def __init__(self):
        self.__id = None
        self.__nome = None

    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome