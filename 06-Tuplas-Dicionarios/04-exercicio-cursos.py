# Enunciado:
# Crie uma tupla com 5 cursos. Use for e if para verificar se o curso "Python" está presente.

# Tupla com cursos
cursos = ("Python", "Java", "HTML", "JavaScript", "C++")

i = 0

while i < len(cursos):

    if cursos[i] == "Python":
        print(f"- {cursos[i]} está presente")

    else:
        print(cursos[i])

    i += 1