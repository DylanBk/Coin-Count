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

def collect_inputs():
    global bag_weight, coin_type
    volunteer_name = input("Name: ")
    coin_type = input("Coin type: ")
    bag_weight = float(input("Weight of bag: "))

def validation():
    if coin_type not in coin_weights:
        print("Invalid coin type, please try again")
        collect_inputs()
    else:
        if bag_weight not in bag_weights:
            print("A bag of " + str(coin_type) + " coins should weigh " + str(bag_weights[coin_type]) + " grams")
            if bag_weight > bag_weights[coin_type]:
                weight_to_remove = bag_weight - bag_weights[coin_type]
                print(str(weight_to_remove) + " grams need to be removed")
            elif bag_weight < bag_weights[coin_type]:                    
                weight_to_add = bag_weights[coin_type] - bag_weight
                print(str(weight_to_add) + " grams need to be added")
        


collect_inputs()
validation()