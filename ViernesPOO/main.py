from cosas import Persona, Alumno, Profesor, AyudanteProfesor

def main():
    per1 = Persona("Jose", 19)
    print(per1)
    print(Persona.descripcion)

    print("----herencia alumno------")
    al1 = Alumno ("Jose", 19, "39494939", "ICO")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Juan"
    print(al2)
    al2.dormir()

    print("-----herencia profe-------")
    profe1 = Profesor("Jesus", 30 + 16, 3584848, "Ingenieria de software")
    print(profe1)
    profe1.dormir

    print("-----herencia ayudante profe-----")
    ayudante = AyudanteProfesor("Adrian", 20, "2392830", "ICO", 928329, "Ing de Software", 8)
    print(ayudante)
    ayudante.dormir()
    ayudante.nombre = "Abrahamas"
    ayudante.dar_clase("P.O.O")

main()
