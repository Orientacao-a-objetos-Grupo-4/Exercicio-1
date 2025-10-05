class Aluno(Pessoa):
    def __init__(self):
        super().__init__()
        self.__id = None
        self.__matricula = None

    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id
    def get_matricula(self):
        return self.__matricula
    def set_matricula(self, matricula):
        self.__matricula = matricula