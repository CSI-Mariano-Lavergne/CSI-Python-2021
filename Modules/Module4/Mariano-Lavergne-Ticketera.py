print("Welcome to the Jhay Cortéz Concert")
print("The cost of each seat is: Arena/Nivel Principal= 85$, Nivel Principal= 75$, Nivel Superior= 55$ ")
Arena = int(input("Cuantas taquillas quieres en arena/nivel principal?"))
Nivel_Principal = int(input("Cuantas taquillas quieres en el nivel principal? "))
Nivel_Superior = int(input("Cuantas taquillas quieres en el nivel superior?"))

def VentasporSección(Arena, Nivel_Principal, Nivel_Superior):
    print(f"El costo para las taquillas en areana es: {int(Arena) * 85}")
    print(f"El costo para las taquillas en el Nivel_Principal es: {int(Nivel_Principal) * 75}")
    print(f"El costo para las taquillas en el Nivel_Superior es: {int(Nivel_Superior) * 55} ")
print()
VentasporSección(Arena, Nivel_Principal, Nivel_Superior)
Venta_A = Arena * 85
Venta_NP = Nivel_Principal * 75
Venta_NS = Nivel_Superior * 55
def TaquillasTotal(Venta_A, Venta_NP, Venta_NS):
    print(f"El total de la venta de taquillas es: ${int(Venta_A) + int(Venta_NP) + int(Venta_NS)}")
print()
TaquillasTotal(Venta_A, Venta_NP, Venta_NS)
