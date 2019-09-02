from car import Car
# importar el e elemento car es el nombre del archivo y Car es el nombre de la clase
if __name__ == "__main__":
    # El metodo se inicia con minuscula el titulo del documento pero para la clases usamos uppperCamelCase
    print("Hola Mundo")
    car = Car("FEFE22", Account("Alejandro Hachiko", "EDFG48"))
    print(vars(car))
    print(vars(car))

    car2 = Car()
    car2.license = "SKDH33"
    car2.driver = "Machine Learning"
    print(vars(car2))