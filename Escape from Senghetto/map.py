from finalItems import *

room_bedroom = {
    "name": "Bedroom",

    "description":
    """Pizza boxes, alcohol containers and numerous variants of 
    mixer lay scattered around the floor; among the mess are 
    several pairs of used boxers, none of them yours. This is 
    not your room. There is a chest of drawers beside the bed,
    a large wardrobe standing against the northern wall and a tall
    mirror opposite. The room contains a door.
    """,

    "exits": {"south": "Hall"},

    "items": [item_pen , item_belt]
}

room_kitchen = {
    "name": "Kitchen",

    "description":
    """Kitchen is a rather grandeous term for what is effectively
    a 'pot noodle storage room'. There is barely enough room to move
    in here. There is a bin overflowing with sachets containing soy
    sauce. There's a microwave with a thick layer of rust around the
    frame. There is a fridge but it currently isn't plugged in. This
    room contains a door.
    """,

    "exits": {"east": "Hall"},

    "items": [item_plastic_knife, item_sponge, item_bacon, item_top]
    }
room_hall = {
    "name": "Hall",

    "description":
    """The flickering ceiling light dimly illuminates various locked
    doors along both walls of the narrow corridor. There is an unearthly
    sound coming from room E followed by a splattering of liquid. The
    origin of a large stain on the carpet is best not to think about.
    Considering most of the doors will lead into somebody's room, there
    is a total of four doors you can use without getting a restraining order.
    """,

    "exits": {"north": "Bedroom", "east": "Bathroom", "south": "Exit", "west": "Kitchen" },

    "items": [item_bulb, item_pumpkin]
}

room_bathroom = {
    "name": "Bathroom",

    "description":
    """The room is dark, you try the light switch but it doesn't seem
    to work! The floor is wet and the air humid as if someone has
    showered recently. The mirror above the sink is dirty and a strange
    odour is coming from the toilet. There is one door in the room.
    """,

    "exits": {"west": "Hall"},

    "items": [item_toilet_roll, item_boxers]
}

room_exit = {
    "name": "Exit",

    "description":
    """There is a single light hanging from the ceiling. There is a 
    collection of bin bags on the floor that no one has bothered to 
    carry 10 metres over to the bins. All the doors for the post boxes
    have been broken open. This room contains 2 doors.
    """,

    "exits": {"north": "Hall", "east": "Outside"},

    "items": [item_trousers]
    }
    
room_outside = {
    "name": "Outside",

    "description":
    """You are standing outside a flat in Senghenydd, lucking quite close
    to the outskirts. There is a faint smell of someone burning toast and 
    a police siren is going off nearby. You can see a bus stop to the south, 
    however it is through quite a dark alley. To the east is a rather small
    and dingy corner shop advertising yesterday's paper in the window. 
    """,

    "exits": {"west": "Exit", "east": "Shop", "south": "Alley"},

    "items": [item_stone]
}
room_shop = {
    "name": "Shop",

    "description":
    """Not exactly Waitrose, this shop seems to only stock pot noodle, alcohol
    and family planning apparatus. The man standing behind the counter looks
    vaguely familiar. He is wearing a tag saying "Kirill, here to help!" He
    smiles at you expectantly. The shop has one exit.
    """,

    "exits": {"west": "Outside"},

    "items": []
}
room_alley = {
    "name": "Alley",

    "description":
    """The smell of urine fills the alleyway. There is a makeshift bed on the
    side of the alley beside an empty bottle of cheap rum. Light enters the
    alley from the south where the bus stop is visible, and from the north
    which leads back to Senghenydd.
    """,

    "exits": {"north": "Outside", "south": "Bus Stop"},

    "items": []
}
room_alley_after = {
    "name": "Alley",

    "description":
    """
    
    """,

    "exits": {"north": "Outside", "south": "Bus Stop"},

    "items": [item_shoes]
}
room_bus = {
    "name": "Bus Stop",

    "description":
    """The whole world seems brighter on this side of the alleyway. There is
    a bus stop and it just so happens that the bus is here at this precise
    moment. The side of the bus declares that the price of a ticket is £1.80.
    This bus is heading back to glorious Talybont.
    """,

    "exits": {"north": "Alley"},

    "items": []
}
rooms = {
    "Bedroom": room_bedroom,
    "Kitchen": room_kitchen,
    "Hall": room_hall,
    "Bathroom": room_bathroom,
    "Exit": room_exit,
    "Outside": room_outside,
    "Shop": room_shop,
    "Alley": room_alley,
    "Bus Stop": room_bus
}
