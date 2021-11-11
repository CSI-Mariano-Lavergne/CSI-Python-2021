import math
from ExperimentalData import ExperimentalData
from pathlib import Path
import json
import os
# gun = "FN GL40"
# cartridge = "40X46 mm"
# ammunition_type = "M381 grenade"
# projectile_velocity = 76
# building = "Caribbean Sea View"
# building_height = 334
# gravity = 9.81

def ProjectileFunction(experimentalData:ExperimentalData):

    # Parallel Lists
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

# Planet Index
    planet_index = planets.index(input("Planet Name: "))

# Planet Gravity
    g_ms2[planet]


    time_s = math.sqrt((2 * experimentalData.building_height) / experimentalData.planets
    # distance = (experimentalData[projectile_velocity] * time_s)
    distance = (experimentalData.projectile_velocity * time_s)

    print(f"The gun i chose was a grenade launcher. The offcial gun name is {experimentalData.gun}. Its cartridge size is {experimentalData.cartridge}. The type of bullet that it takes is a {experimentalData.ammunition_type}. Lastly it shoots a grenade at a speed at {experimentalData.projectile_velocity} mi/s. The time the bullet took to travel to the bottom of the {experimentalData.building} which is a distance{distance} meters was {time_s} seconds ")


# ProjectileFunction("FN GL40", "40X46mm", "M381 grenade", 76, "Caribbean Sea View", 334, 9.81)

# experimentalData = {
# "gun" : "FN GL40", 
# "cartridge" : "40X46 mm", 
# "ammunition_type" : "M381 grenade",
# "projectile_velocity" : 76,
# "building" : "Caribbean Sea View",
# "building_height" : 334,
# "gravity" : 9.81
# }

# experimentalData = ExperimentalData("FN GL40", "40X46mm", "M381 grenade", 76, "Caribbean Sea View", 334, 9.8)

myDataSet = [
ExperimentalData("FN GL40", "40X46mm", "M381 grenade", 76, "Caribbean Sea View", 334, 9.8),
ExperimentalData("FN GL40", "40X46mm", "M381 grenade", 76, "Burj Khalifa", 828, 9.8),
ExperimentalData("FN GL40", "40X46mm", "M381 grenade", 76, "Shanghai Tower", 632, 9.8),   
ExperimentalData("FN GL40", "40X46mm", "M381 grenade", 76, "Lotte World Tower", 555, 9.8),
ExperimentalData("FN GL40", "40X46mm", "M381 grenade", 76, "One World Trade Center", 541.3, 9.8) 
]

for data in myDataSet:
    print("\n-------------------------------\n")
    ProjectileFunction(data)

    myOutputPath = Path(__file__).parents[0]
    myOutputFilePath = os.path.join(myOutputPath, 'Projectile-Motion.json')

    with open(myOutputFilePath, 'w') as outfile:
        json.dump([data.__dict__ for data in myDataSet], outfile)

    
deserialize = open(myOutputPath)
experimentJson = json.load(deserialize)


for e in experimentJson:
    ExperimentalData(**e).run()
