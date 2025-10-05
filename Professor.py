class Professor(Pessoa):
    def __init__(self):
        super().__init__()
        self.__id = None
        self.__matricula = None

    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id
    def get_especialidade(self):
        return self.__especialidade
    def set_especialidade(self, matricula):
        self.__especialidade = matricula