gun = "FN GL40"
cartridge = "40X46 mm"
ammunition_type = "Single"
projectile_velocity = 30
building = "Caribbean Sea View"
building_height = 334
gravity = 9.81

import math

time_s = math.sqrt((2 * building_height) / gravity)

distance = (projectile_velocity * time_s)

print(f"The gun selected was {gun}")

print("The gun i chose was a grenade launcher. The offcial gun name is the FN GL40. Its cartridge size is 40x46 mm. It takes single ammunition meaning that it can only shoot one grenade at a time. Lastly it shoots a grenade at a speed at 30mi/s. ")