planets = ["Mercury" , "Venus" , "Earth", "Mars" , "Jupiter" , "Saturn" , "Uranus" , "Neptune"]
rel_gravity = [2.65, 1.11, 1, 2.64, 0.40, 0.94, 1.13, 0.88]

print("Jumping on other planets")

myJump = float(input("What is the length of your jump on Earth (meters)?"))
myPlanet = input(f"Choose a planet from this list: {planets}")

def calculateLength(planet, length):
    print(f"\nYour jump in Earth is: {length}")

    planet_index = planets.index(planet)
    print(f"Your jump length in {planets[planet_index]} is {myJump * rel_gravity[planet_index]} m")

calculateLength(myPlanet, myJump)
    