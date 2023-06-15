from Cosas import Alumno, Perro

def main():
    al1 = Alumno("Jose", 19, "ICO")
    print(vars(al1))
    al1.__nombre = "Diego"
    print(vars(al1))
    al1.set_nombre("Maria")
    print(vars(al1))
    print("-------To string--------")
    print(al1)
    al1.set_edad(999)
    print(al1)
    al1.estudiar(4)

    print("---Perro---")
    perro1 = Perro("Poddle", 2, 0.35)
    print(vars(perro1))
    perro1.raza = "Callejero"
    print(vars(perro1))
    perro1.__raza = "otra"
    print(vars(perro1))
    perro1.edad = 12
    perro1.estatura = 0.43
    print(perro1)
    cachorrito = Perro.es_cachorro(perro1.edad)
    print(cachorrito)
    Perro.dormir()
    danes = Perro.perro_grande(0.8)
    print(danes)
main()