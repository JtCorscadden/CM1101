from finalItems import *
import string

# List of "unimportant" words (feel free to add more)
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']
def filter_words(words, skip_words):
    new_list = []
    words = (words.lower()).split()
    for word in words:
        if not word in skip_words:
            new_list.append(word)
    return ' '.join(new_list)
def remove_punct(text):
    for c in string.punctuation:
        text = text.replace(c, '')
    return text
def remove_spaces(text):
    text = text.lstrip()
    text = text.rstrip()
    return text
def normalise_input(user_input):
    global skip_words
    user_input = remove_punct(user_input)
    user_input = remove_spaces(user_input)
    user_input = filter_words(user_input, skip_words)
    return user_input.lower()
    
player = {"health": 40, "inventory": [], "alive": True}
clothes = {"Top": False, "Boxers": False, "Trousers": False, "Shoes": False, "Belt": False}
money = 0.0
wand = False
beggar = {"health": 80, "alive": True}
        
def print_inventory():
    for item in player["inventory"]:
        print("You have " + player["inventory"][item]+".")
        
def check_item(item):
    return item in player["inventory"]

def execute_beat():
    while player["alive"] is True or beggar["alive"] is True:
        print_inventory
        if clothes["Belt"]:
            print("You are wearing a belt.")
        user_input = input(print("Which item do you want to use?"))
        item = normalise_input(user_input)
        if check_item(item):
            beggar["health"]-= player["inventory"][item]["damage_beggar"]
            player["health"] -= player["inventory"][item]["damage_player"]
            player["inventory"].remove(item)
            print("Your health: "+player["health"]+"\t\tBeggar's health: "+beggar["health"])
    if player["alive"]:
        print("")
        # print_exits() 
    else:
        print("")
        # If he lost it will be the end of the game
def print_shop_menu():
    print("Item\t\tPrice")
    print("Water\t\t£")
    print("Wand\t\t£")
