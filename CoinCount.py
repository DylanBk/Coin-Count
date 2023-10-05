#=============== imports =====

import time
from colorama import Fore

#=============== variables =====

total_value = 0
bags_checked = 0
valid_bags = 0
accuracy = 0
display_info = False

#=============== dictionaries =====

coin_weights = {
    "£2" : 12,
    "£1" : 8.75,
    "50p" : 8,
    "20p" : 5,
    "10p" : 6.5,
    "5p" : 2.35,
    "2p" : 7.12,
    "1p" : 3.56
}

bag_weights = {
    "£2" : 120,
    "£1" : 175,
    "50p" : 160,
    "20p" : 250,
    "10p" : 325,
    "5p" : 235,
    "2p" : 356,
    "1p" : 356
}

bag_value = {
    "£2" : 20,
    "£1" : 20,
    "50p" : 10,
    "20p" : 10,
    "10p" : 5,
    "5p" : 5,
    "2p" : 1,
    "1p" : 1
}

volunteers_accuracy = {}

#=============== subroutines =====

def reset(): #resets stats when a new user uses the program
    global bags_checked, valid_bags, display_info
    bags_checked = 0
    valid_bags = 0
    display_info = False

def collect_inputs():
    global bag_weight, coin_type, bags_checked, valid_bags
    try:
        exit_to_menu = int(input("\n[1] Continue\n[2] Exit to menu\n> "))
        if exit_to_menu == 1:
            pass
        elif exit_to_menu == 2:
            reset()
            menu()
        else:
            print(Fore.RED + "Invalid input, please try again" + Fore.WHITE)
            collect_inputs()
        coin_type = input("\nCoin type: ")
        bag_weight = float(input("Weight of bag: "))
        validation()
    except ValueError:
        print(Fore.RED + "\nInvalid input, please try again" + Fore.WHITE)

def bag_recording():
    global display_info
    try:
        check_bags = int(input("\nWould you like to display how many bags are checked?\n[1] Yes\n[2] No\n> "))
        if check_bags == 1:
            display_info = True
            collect_inputs()
        elif check_bags == 2:
            collect_inputs()
        else:
            print(Fore.RED + "\nInvalid input, please try again" + Fore.WHITE)
            bag_recording()
    except ValueError:
        print(Fore.RED + "\nInvalid input, please try again" + Fore.WHITE)
        bag_recording()

def validation():
    global bag_weight, coin_type, bags_checked, total_value, valid_bags, record_bags
    bags_checked += 1
    if coin_type not in coin_weights:
        print(Fore.RED + "\nInvalid coin type, please try again" + Fore.WHITE)
        collect_inputs()
    else:
        if bag_weight not in bag_weights:
            print("\nA bag of " + str(coin_type) + " coins should weigh " + str(bag_weights[coin_type]) + " grams")
            if bag_weight > bag_weights[coin_type]:
                coins_to_remove = (bag_weight - bag_weights[coin_type]) / coin_weights[coin_type]
                print(str(coins_to_remove) + " coins need to be removed")
                time.sleep(3)
                display()
                collect_inputs()
            elif bag_weight < bag_weights[coin_type]:
                coins_to_add = (bag_weights[coin_type] - bag_weight) / coin_weights[coin_type]
                print(str(coins_to_add) + " coins need to be added")
                time.sleep(3)
                display()
                collect_inputs()
            else:
                print(Fore.GREEN + "\nBag validated" + Fore.WHITE)
                value = bag_value[coin_type]
                total_value += value
                valid_bags += 1
                display()

def display(): #if user chooses for stats to show, then this displays stats
    global bags_checked, valid_bags, total_value, display_info, accuracy,  volunteer_name
    volunteer_accuracy()
    if display_info == True:
        print("\nName: " + volunteer_name)
        print("Bags checked: " + str(bags_checked))
        print("Correct bags: " + str(valid_bags))
        print("Total value collected: £" + str(total_value))
        print("Accuracy: " + str(accuracy) + "%")
        time.sleep(3)
        collect_inputs()

def volunteer_accuracy(): #calculaion to get accuracy per volunteer
    global accuracy, bags_checked, valid_bags, volunteer_name, sorted_list
    accuracy = valid_bags / bags_checked * 100
    volunteers_accuracy[volunteer_name] = (accuracy) #accuracy added to list with their name
    sorted_list = sorted(volunteers_accuracy.items(), key = lambda x:x[1], reverse=True) #list is sorted by accuracy descending
    storing_info()

def storing_info():
    f = open("volunteerAccuracy.txt", "w")
    f.write(str(sorted_list))
    f.close()

def menu():
    global volunteer_name
    print(Fore.YELLOW + """\n ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌░▌     ▐░▌ ▀▀▀▀█░█▀▀▀▀ 
▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌     ▐░▌     
▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌ ▐░▌   ▐░▌     ▐░▌     
▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌     ▐░▌     
▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌   ▐░▌ ▐░▌     ▐░▌     
▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌     ▐░▌     
▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌     ▐░▌     
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌     ▐░▌     
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀       ▀      
                                                                                                                          
""" + Fore.WHITE)
    while True:
        try:
            menu_choice = int(input("\n[1] Continue\n[2] View volunteers\n> "))       
            if menu_choice == 1:
                volunteer_name = input("\nName: ")
                bag_recording()
                collect_inputs()
            elif menu_choice == 2:
                f = open("volunteerAccuracy.txt", "r")
                print("")
                print(f.read())
                f.close()
                input("\nPress [ENTER] to continue")
                menu()
            else:
                print(Fore.RED + "\nInvalid input, please try again\n" + Fore.WHITE)
                continue
        except ValueError:
            print(Fore.RED + "\nInvalid input, please try again" + Fore.WHITE)

#=============== main program =====

menu()
