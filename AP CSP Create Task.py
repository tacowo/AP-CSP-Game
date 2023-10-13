# Importing python modules

import random
import time

#creating the lists the game picks thru 

game_items = [
    "Gold jewelry",
    "Drum Kit",
    "Video game consoles",
    "Power tools",
    "Signed Guitar",
    "Laptop",
    "Bicycle",
    "Cameras",
    "Collectible coin",
    "Diamond Ring",
    "Watch",
    "Vintage Phone",
    "DVDs and Blu-rays",
    "Designer handbag",
    "Japanese Samurai Sword",
    "Vintage Movie Prop",
    "Painting",
    "Television set",
    "Fishing equipment",
    "Smartphone",
    "Football Jersey",
    "Books",
    "Keyboard",
    "Plastic cup",
    "Shoe",
    "Record"
]

item_values = [
    200,
    250,
    150,
    95,
    300,
    199,
    100,
    150,
    300,
    250,
    499,
    100,
    50,
    300,
    500,
    200,
    200,
    300,
    199,
    250,
    185,
    50,
    50,
    50,
    50,
    50,
]

starting_items = [
    "Work boot",
    "Bowling Pin",
    "Book",
    "Computer Part",
    "Car Tire"
    ]

names = [
    "Bob",
    "Jeff",
    "Bennifer",
    "Mario",
    "Bowser",
    "Walter",
    "Hank",
    "Flynn",
    "Jesse"
]


#starting the game, explaining how to play to user

print("Welcome to Swap Specialist!")
time.sleep(2)
print("Swap Specialist is a game where you swap items until you reach a certain amount of money.")
time.sleep(3)
print("You will start with a random item and be presented with trades by the game")
time.sleep(3)
readytoplay = input("Are you ready to play? [yes] [no] ")
if readytoplay == ("yes"):
    print("Great! Let's begin!")
    #setting up values and lists so the game can work
    time.sleep(1.5)
    starter_item = random.choice(starting_items)
    print("The starting item you've recieved is a " + (starter_item) + " Worth $100!")
    balance = 100
    owned_items = [(starter_item),]
    owned_item_values = [100,]
    inventory_index = 1
    time.sleep(2)
    print("Now, time to get to trading. The goal is $1500, Good luck.")
    time.sleep(4)
    # the part where the game actually begins
    trades = 0
    while balance <= 1500:
        #selecting which items will be included in the trade
        tradername = random.choice(names)
        selected_num = random.randint(0,len(game_items) - 1)
        offered_item = game_items[selected_num]
        offered_value = item_values[selected_num]
        if len(owned_items) > 1:
            wanted_num = random.randint(0,len(owned_items))
        else:
            wanted_num = 0
        want_item = owned_items[wanted_num]
        want_value = owned_item_values[wanted_num]
        #random chance that the trade is 1 or 2 items
        amount_of_item = random.randint(1,5)
        if amount_of_item == 1:
            print("")
            print("Trade Offer! " + tradername + " Offers " + offered_item + " Worth " + str(offered_value) + "!")
        else:
            selected_num2 = random.randint(0,len(game_items))
            offered_item2 = game_items[selected_num2]
            offered_value2 = item_values[selected_num2]
            offered_value = offered_value + item_values[selected_num2]
            print("")
            print("Trade Offer! " + tradername + " Offers " + offered_item + " and " + offered_item2 + " Worth " + str(offered_value) + "!")
        time.sleep(1.5)
        print("In exchange for your " + want_item + " Worth " + str(want_value) + ".")
        choice = input("Would you like to accept this trade? [swap] [decline] ")
        if choice == "swap":
            print("Trade offer Accepted!")
            owned_items[wanted_num] = offered_item
            if amount_of_item == 1:
                num_after = wanted_num + 1
                owned_item_values[num_after] = offered_value2
            else:
                owned_item_values[wanted_num] = offered_value
            balance = balance + offered_value
            balance = balance - want_value
            print("Your inventory value after trade is " + str(balance) + "!")
            time.sleep(3)
            trades = trades + 1
        else:
            print("No Deal, on to the next trade!")
            time.sleep(3)
    print("Congratulations, You win!")
    time.sleep(1.5)
    print("You finished in " + str(trades) + " trades!")        
            
else: 
    print("Ok then, Have a good day.")