from cosas import Libro, Autor, Alumno

def main():
    l1 = Libro.Libro_planeta("El perfume", Autor ("Patrick", "PS"), 1980)
    print(l1)

    l1.autor.pseudonimo = l1.autor.pseudonimo.lower()
    print(l1)
    print("-----------Herencia------------")
    al2 = Alumno("Jose", 19, "4949493", "ICO", 9)
    al2.nombre = "Pepe"
    print(vars(al2))

main()