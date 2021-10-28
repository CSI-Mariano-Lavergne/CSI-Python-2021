import math

# gun = "FN GL40"
# cartridge = "40X46 mm"
# ammunition_type = "M381 grenade"
# projectile_velocity = 76
# building = "Caribbean Sea View"
# building_height = 334
# gravity = 9.81

def ProjectileFunction(gun:str, cartridge:str, ammunition_type:str, projectile_velocity:int, building:str, building_height:int, gravity:int):
    time_s = math.sqrt((2 * building_height) / gravity)
    distance = (projectile_velocity * time_s)

    print(f"The gun i chose was a grenade launcher. The offcial gun name is {gun}. Its cartridge size is {cartridge}. The type of bullet that it takes is a {ammunition_type}. Lastly it shoots a grenade at a speed at {projectile_velocity} mi/s. ")


ProjectileFunction("FN GL40", "40X46mm", "M381 grenade", 76, "Caribbean Sea View", 334, 9.81)