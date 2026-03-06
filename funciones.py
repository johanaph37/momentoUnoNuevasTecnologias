from diccionario import estudiantes

def registrar_estudiante():
    id_estudiante = input("Ingrese el la identificación del estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")

    estudiantes[id_estudiante] = {
    "nombre": nombre,
    "nota1": 0.0,
    "nota2": 0.0

    }

    print(f"Estudiante {nombre} registrado con éxito")
    