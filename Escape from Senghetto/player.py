from items import *
from map import rooms

inventory = []
sense = True



def checkinv(useless):
	weight_limit = 3.0
	cur_weight = 0.0
	for item in inventory:
		useless = 0.0
		cur_weight = cur_weight + item['weight']
	if cur_weight > 3.0:
		print("YOU CANNOT CARRY ALL THESE ITEMS, YOU HAVE DROPPED SOME ON THE FLOOR.")
		for item in inventory:
			inventory.remove(item)
			current_room['items'].append(item)


# Start game at the reception
current_room = rooms["Bedroom"]
