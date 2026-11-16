cursos = ["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
notas = []
for i in cursos:
    nota = input(f"Que nota has sacado en  {i}? :")
    notas.append(nota)
for x in range(len(cursos)):
    print ("En ", cursos[x], "has sacado un", notas[x])