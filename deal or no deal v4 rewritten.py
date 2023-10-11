import random #random import for functions
players = [1,2,3,4,5,6,7,8,9,10] #player list
box = [1,2,3,4,5,6,7,8,9,10] #box list
money = [0.10, 0.50, 1, 10, 50, 100, 250, 1000, 25000, 100000] #money amounts available
assigned = [["","",""],["","",""],["","",""],["","",""],["","",""],["","",""],["","",""],["","",""],["","",""],["","",""]] #all 10 players, boxes and money amounts sorted into a list
round_counter = 0 #used for banker offers
#multiplier list, weighted to give multipliers closer to one, and have a lower chance to have an multiplier much lower or much higher than one 
multiplier_list_low= [0.5, 0.6]
multiplier_list_mid= [0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3]
multiplier_list_high= [1.4, 1.5]
#the values, players and boxes are selcected 
p= random.sample(set(players), 10) #lists created and then added into the assigned list  
b= random.sample(set(box), 10)   
m= random.sample(set(money), 10)
#loop used to assign a player, box and value to the assigned list
for i in range (len(assigned)):
    assigned[i][0] = p[i]
    assigned[i][1] = b[i]
    assigned[i][2] = m[i]

#the user of the code is linked to a player in game and then given their box number
player = random.choice(players)
for i in range (len(assigned)):
    if assigned[i][0] == int(player):
        user_box = assigned[i][1]
for i in range (len(assigned)): #index position of the player/user's box to be print if they win their own box
    if user_box == assigned [i][1]:
        u = i
player_money = assigned [u][2]
#generic integer validation
def swap(user_box):
    print("The banker is offering you to swap your box with another box in the room, type 'yes' to accept the offer.")
    box_swap = input().lower().strip()
    if box_swap == "yes":
        box_number_swap, box_number_swap_position = integer_validation_2()
##        box_number_swap = int(input("what box do you wish to swap with?"))
##        valid = False
##        while valid == False:
##            try:
##                for i in range (len(assigned)):
##                    if box_number_swap == assigned[i][1]:
##                        if x != user_box:
##                            box_number_swap2 = assigned[i][1]
##                            box_number_swap_position = i
##                            print("that box is available")
##                            print("swap commencing...")
##                            valid = True
##                        else:
##                            print("Must be an available box or not your own box!")
##            except:
##                    print("Must be a number of a box!")
        temp_box = assigned[box_number_swap_position][1]
        temp_money = assigned[box_number_swap_position][2]
        assigned[box_number_swap_position][1] = user_box
        assigned[box_number_swap_position][2] = assigned[u][2]
        assigned[u][1] = temp_box
        assigned[u][2] = temp_money
        print("you now have box number", box_number_swap)
    #print(assigned)
                
def integer_validation():
    valid = False
    while valid == False:
        try:
            print("Enter a box number to find the value and remove it.")
            x = int(input())
            for i in range (len(box)):
                if x == box[i]:
                    if x != user_box: #doesnt allow user to input their own box
                        valid = True
                    else:
                        print("Must be an available box or not your own box!")
        except:
            print("Must be a number of a box!")
    return x
def integer_validation_2():
    valid = False
    while valid == False:
        try:
            print("Enter a box number you wish to swap your box with.")
            x = int(input())
            for i in range (len(assigned)):
                if x == assigned[i][1]:
                    if x != user_box: #doesnt allow user to input their own box
                        box_number_swap2 = assigned[i][1]
                        box_number_swap_position = i
                        print("that box is available")
                        print("swap commencing...")
                        valid = True
                        
                    else:
                        print("Must be an available box or not your own box!")
        except:
            print("Must be a number of a box!")
    return x, box_number_swap_position
print ("You are player", player, "and you have box number", user_box)
#function for player to select and remove a box
def select():
    print ("These are the available boxes to open", box)
    x = integer_validation()
    for i in range(len(assigned)): #finds index position of the box the user inputs and removed the box from the boxes list
        if x == box [i]:
            box2 = box [i]
            q = i
    del box[q]
    for i in range(len(assigned)): #finds index position of the box, player and value in the assigned list and then uses the value to remove it 
        if x == assigned [i][1]:
            value = assigned [i][2]
            y = i
    for i in range(len(assigned)): #finds index position of the value associated with the box that the user wishes to remove
        if value == money [i]:
            value2 = money [i]
            z = i
    del money [z]
    del assigned [y]
    #print (assigned)
    #print (value)
    #print (money)
    print("The box being removed is", x, ". This box had £", value)
#this is how the user wins 
def accepted(offer):
    print("are you going to accept the bankers offer of £", round(offer),"pounds")
    choice = input().lower().strip()
    if choice == "yes":
        print("Congratulations on winning £", offer)
        quit()
def banker(round_counter, user_box):
    print ("\n")
    print ("The banker has an offer for you...")
    chance = random.choice(range(0, 100)) #random function to select a number from 0 to 100 and the multiplier is decided off of this random factor
    if chance >= 0 and chance < 15:
        multiplier = random.choice(multiplier_list_low)        
    elif chance >= 15 and chance < 85:
        multiplier = random.choice(multiplier_list_mid)        
    elif chance >= 85 and chance <= 100:
        multiplier = random.choice(multiplier_list_high)   
    max_val = max(money) #finds highest and lower money amount left in order to find another value 
    min_val = min(money)
    total = max_val + min_val 
    if round_counter == 0: #division value decreases each time in order to give a much higher value at the end of the game where the probability of getting a the highest value box is higher
        mean = total/32
    elif round_counter == 1:
        mean = total/16
    elif round_counter == 2:
        mean = total/8
    elif round_counter == 3:
        mean = total/2
    offer = mean * multiplier
    print (round(offer))
    round_counter = round_counter + 1 #increases each banker offer in order to reduce the number the offer is divided by 
    accepted(offer)
    chance2 = random.choice(range(0, 100))
    if chance2 < 100: #gives a 25% chance for the banker to offer a bank swap
        swap(user_box)
for i in range (4): #gameplay, runs lines 98-100 4 times
    for j in range (2): #runes lines 99-100 twice 
        select()
    banker(round_counter, user_box)
print("You have won the contents of your box")#this is if the player accepts no offers and chooses their own box 
print("You have won", player_money ,"pounds!")        
