receipts = {
    "Jessica": {
        "Drinks": {
            "Iced Coffee": 4.50
        },
        "Appetizers": {
            "Garlic Bread": 6.00,
            "Bruschetta": 7.00
        },
        "Entrees": {
            "Grilled Salmon": 18.00
        }
    },
    "Jennifer": {
        "Drinks": {
            "Soda": 3.00,
            "Iced Tea": 2.75
        },
        "Entrees": {
            "Spaghetti Carbonara": 15.00,
            "Vegetable Stir-fry": 12.50
        }
    },
    "Jung": {
        "Drinks": {
            "Soda": 3.00,
        },
        "Appetizers": {
            "Edamame": 4.00
        },
        "Entrees": {
            "Beef Bulgogi": 17.00
        },
        "Desserts": {
            "Mochi Ice Cream": 6.50,
            "Custard Tart": 5.50
        }
    },
    "Hannah": {
        "Drinks": {
            "Lemonade": 3.75,
            "Mango Smoothie": 5.00
        },
        "Appetizers": {
            "Fried Calamari": 8.50
        },
        "Desserts": {
            "Tiramisu": 7.75
        }
    }
}


order_receipt = []

guest_order = {}

def get_guest():
    i = 1
    for key in receipts.keys():
        print(f' {i}) {key}')
        guest_order[i] = key
        i += 1

def get_guest_receipt():
    if guest_confirmation.isdigit():
        if int(guest_confirmation) in guest_order.keys():
            guest_selection = guest_order[int(guest_confirmation)]
            print(f'You selected {guest_selection}\'s check.')
            print(f'Processing the check for you now....')

            


        else:
            print(f'{guest_confirmation} is not a valid option')
    else:
        print("You didn't select a number. ")



while True:
    
    checkout_question = input("Thank you for dining with us! Are you ready to checkout? (Y/N) ")
    
    match(checkout_question.lower().strip()):
        case "y":
            get_guest()
            guest_confirmation = input("Sounds good! Which guest are you? Select a number. ")
            get_guest_receipt()
            break;
        case "n":
            print("Got it! Let us know whenever you're ready to checkout!")
            break
        case _:
            print(f"I didn't understand your response. Please try again.")



    








 


