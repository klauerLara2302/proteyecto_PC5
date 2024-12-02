

def interfaz():
    print("    ---  Escoger una opcion  ---")
    print(" 1. Prom. general del Estudiante")
    print(" 2. Prom. general del Estudiante/Materia")
    print(" 3. Prom. general del Salon/Materia")
    print(" 4. Prom. general del salon")
    print(" 5. Generar Reporte")
    print(" 6. Salir ")

class Calificaciones:
  
    def __init__(self): #constructor de la clase / inicializa todo en cero
        self._notas = [[0 for _ in range(3)] for _ in range(3)]  # Notas por curso [ [0 , 0 , 0] , [0 , 0 , 0] ,[0 , 0 , 0] ]
        self._prom_materia = [0] * 3  # Promedios por curso / [ 0 , 0 , 0]
        self._promedio_general = 0

    def Notas_cursos(self):
        for i in range(3):
            print(f" -Curso {i + 1}: ")
            for j in range(3):
                self._notas[i][j] = float(input(f" |Nota {j + 1}: "))

    def Notas_de_un_curso(self, k, f):
        for i in range(3):
            f.write(f"{self._notas[k][i]:<8}")

    def prom_general(self):
        suma = 0
        for i in range(3):
            for j in range(3):
                suma += self._notas[i][j]
        self._promedio_general = suma / 9  # Promedio general del alumno

    def Dev_promedio_general(self):
        return self._promedio_general

    def prom_general_materia(self):
        for i in range(3):
            suma = 0
            for j in range(3):
                suma += self._notas[i][j]
            self._prom_materia[i] = suma / 3

    def Acceder_prom_materia(self, k):
        return self._prom_materia[k]



class Estudiante:
    def __init__(self, nombre="", ID=0): #constructor/ inicializa el nombre y el ID 
        self._nombre = nombre
        self._ID = ID
        self.calificaciones = Calificaciones()

    def Escribir_nombre(self):
        self._nombre = input()

    def Devolver_nombre(self):
        return self._nombre

    def Pedir_ID(self):
        self._ID = int(input("ID del Alumno: "))

    def Devolver_ID(self):
        return self._ID




# ----------------------- Funciones utilizadas -------------------------------------- #


def Mostrar_promedio_Alumno(ptr, n):
    for i in range(n):
        print(f"Prom.Alumno {i + 1}: {ptr[i].calificaciones.Dev_promedio_general()}")

def Mostrar_promedio_Alumno_materia(ptr, n):
    for i in range(n):
        print(f"Alumno {i + 1} ->  |M1: {ptr[i].calificaciones.Acceder_prom_materia(0)}| |M2: {ptr[i].calificaciones.Acceder_prom_materia(1)}| |M3: {ptr[i].calificaciones.Acceder_prom_materia(2)}|")

def Crear_promedio_salon_materia(ptr, arr, n):
    for i in range(3):
        suma = 0
        for j in range(n):
            suma += ptr[j].calificaciones.Acceder_prom_materia(i)
        arr[i] = suma / n

def Mostrar_promedio_salon_materia( arr):
    for i in range(3):
        print(f"Prom.Alumnos.Curso {i + 1}: {arr[i]}")

def Mostrar_promedio_salon_total(arr):
    suma = 0
    for i in range(3):
        suma += arr[i]
    return suma / 3

def Generar_reporte(ptr, n):
    with open("Reporte.txt", "w") as f:
        f.write(" ------Reporte Actualizado de la clase----\n")
        f.write(" ID      Nombre                       Curso1                  Curso2                     Curso3           Promedio\n")

        for i in range(n):
            f.write(f"{ptr[i].Devolver_ID():<10}{ptr[i].Devolver_nombre():<20}")
            ptr[i].calificaciones.Notas_de_un_curso(0, f)
            f.write("  ")
            ptr[i].calificaciones.Notas_de_un_curso(1, f)
            f.write("  ")
            ptr[i].calificaciones.Notas_de_un_curso(2, f)
            f.write(f"{ptr[i].calificaciones.Dev_promedio_general():>10}\n")


# -----------------------------  Funcion principal  ----------------------------------- #

def main():
    print( "-----  Inicio del programa  -----" )
    alumnos = int(input("  Numero de alumnos matriculados: "))
    print()

    ptr = [Estudiante() for _ in range(alumnos)]  # Lista de clases Estudiante

    # Pedimos el nombre del alumno y su ID
    print("---- Registro de Datos y Notas de los estudiantes ----")
    print()

    for i in range(alumnos): # desde cero hasta alumnos -1 // bucle for
        print(f"Nombre del Alumno {i + 1}: ", end="")
        ptr[i].Escribir_nombre()
        ptr[i].Pedir_ID()
        print(f"Notas del Alumno {i + 1} : ")
        ptr[i].calificaciones.Notas_cursos()
        print()

    # En función a las notas, creo toda la demás información

    # Promedios generales
    for i in range(alumnos):  # desde cero hasta (alumnos-1) // bucle for
        ptr[i].calificaciones.prom_general()

    # Promedios generales por materia
    for k in range(alumnos):  # desde cero hasta (alumnos -1) // bucle for
        ptr[k].calificaciones.prom_general_materia()

    opcion = 0  # Controla la opción que vamos a elegir
    arr = [0] * 3  # Arreglo para almacenar promedio del salón/materia

    interfaz()
    opcion = int(input("opcion--> ")) #introduce el usuario la opcion que prefiera

    while opcion != 6:
        if opcion == 1:
            print("//Prom. general del Estudiante//")
            Mostrar_promedio_Alumno(ptr, alumnos)
            print()
            interfaz()
        elif opcion == 2:
            print("//Prom. general del Estudiante/Materia//")
            Mostrar_promedio_Alumno_materia(ptr, alumnos)
            interfaz()
        elif opcion == 3:
            print("//Prom. general del Salon/Materia//")
            Crear_promedio_salon_materia(ptr, arr, alumnos)
            Mostrar_promedio_salon_materia(arr)
            print()
            interfaz()
        elif opcion == 4:
            print("//Prom. general del salon//")
            print(f"Prom.total.salon: {Mostrar_promedio_salon_total(arr)}")
            print()
            interfaz()
        elif opcion == 5:
            print("//Generar Reporte//")
            Generar_reporte(ptr, alumnos)
            print()
            interfaz()
        else:
            print("Opcion no permitida. Vuelva a intentar.")
        
        opcion = int(input("opcion--> "))

        if opcion == 6:
            print("//Salir//")
            print("Saliendo del programa...")

if __name__ == "__main__":
    main()



