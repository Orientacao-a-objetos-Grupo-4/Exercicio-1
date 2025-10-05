class Turma():
    def __init__(self, codigo, nome, professor, alunos=None):
        self.codigo = codigo
        self.nome = nome
        self.professor = professor
        self.alunos = alunos if alunos is not None else []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def remover_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)

    def listar_alunos(self):
        return [aluno.nome for aluno in self.alunos]

    def __str__(self):
        return f'Turma {self.codigo} - {self.nome}, Professor: {self.professor.nome}, Alunos: {len(self.alunos)}'