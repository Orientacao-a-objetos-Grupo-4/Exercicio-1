from Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self):
        super().__init__()
        self.__id = None
        self.__matricula = None

    def get_Professorid(self):
        return self.__id
    def set_Professorid(self, id):
        self.__id = id
    def get_matriculaProf(self):
        return self.__matricula 
    def set_matriculaProf(self, matricula):
        self.__matricula = matricula