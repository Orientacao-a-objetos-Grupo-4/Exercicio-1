# Exercício Relâmpago Surpresa 🎃

---

## 📚 Tema: Orientação a Objetos  
### Edição Comemorativa de Halloween 👻

---

## 📊 Diagrama de Classes

Observe o diagrama abaixo que apresenta **herança**, **associação do tipo 1** e **associação do tipo n**:

<br/>
<img width="342" height="273" alt="image" src="https://github.com/user-attachments/assets/9b5c5fa2-bb99-4aca-b5f5-0ade8bc7c13e" />


---

## 🧩 O que devo fazer?

Com base no diagrama de classes apresentado, implemente o sistema com as classes e comportamentos indicados.

Responda (via código) às seguintes questões:

1️⃣ **Qual o nome do professor de uma turma?**  
2️⃣ **Quais os nomes de todos os alunos de uma turma?**  
3️⃣ **Quais os nomes dos professores que lecionam em alguma turma de um curso?**  
4️⃣ **Quais os nomes dos alunos que estão em alguma turma de um curso?**  
5️⃣ **Quais os nomes dos alunos que estão registrados em um curso?**  
6️⃣ **Quais as disciplinas que estão em alguma turma de um curso?**  
7️⃣ **Verificar se um aluno está em uma turma.**  
8️⃣ **Verificar se um aluno está em um curso.**  
9️⃣ **Verificar se uma turma está em um curso.**  
🔟 **Excluir um aluno de uma turma.**  
1️⃣1️⃣ **Excluir uma turma de um curso.**  
1️⃣2️⃣ **Excluir um aluno de um curso.**  

---

## ⚙️ Estrutura sugerida

### 🧍‍♀️ Classe `Pessoa`
- Atributos: `nome`

---

### 👨‍🏫 Classe `Professor` (herda de Pessoa)
- Métodos: retornar nome do professor

---

### 🎓 Classe `Aluno` (herda de Pessoa)
- Métodos: retornar nome do aluno

---

### 🏫 Classe `Turma`
- Atributos: `professor`, `disciplina`, `alunos`
- Métodos: listar alunos, obter professor, adicionar e remover alunos

---

### 📘 Classe `Curso`
- Atributos: `nome`, `turmas`, `alunos`
- Métodos: verificar se aluno/turma está no curso, adicionar e remover alunos/turmas

---




