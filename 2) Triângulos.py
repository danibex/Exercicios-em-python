lado1 = int(input("Ddigite o primeiro lado: "))
lado2 = int(input("Ddigite o segundo lado: "))
lado3 = int(input("Ddigite o terceiro lado: "))

if lado1 == lado2 == lado3:
    print("Esse triângulo é equilátero!")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Esse triângulo é Isóceles!")
elif lado1 != lado2 != lado3:
    print("Esse triângulo é escaleno!")