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
            print('-' * 50)
            print('Welcome to Hoshi\'s Diner!')

            if guest_selection in receipts:
                guest_receipt = receipts[guest_selection]
                total = 0  


                for _, items in guest_receipt.items():
                    for item_name, price in items.items():
                        num_item_spaces = 45 - len(item_name)
                        item_spaces = " " * num_item_spaces
                        print(f'{item_name}{item_spaces}{price:.2f}')
                        total += price 
                print('-' * 50)
                sales_tax_rate= .04
                sales_tax = total * sales_tax_rate
                grand_total = total + sales_tax
                print(f'{item_spaces} Subtotal: {total:.2f}')
                print(f'{item_spaces} Sales Tax (4%): {sales_tax:.2f}')
                print(f'{item_spaces} Grand Total: {grand_total:.2f}')
                print(f'{item_spaces} Thank you and please come visit us again!')
                print(f'                                            ')
            else: 
                print(f'Cannot find {guest_selection}\'s receipt')
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
            
                repeat_prompt = input('Would you like checkout another receipt? (Y/N) ')
                print('                                                       ')
                if repeat_prompt.lower().strip() != "y":
                    print('Goodbye! ')
                    break;
        case "n":
            print("Got it! Let us know whenever you're ready to checkout!")
            break
        case _:
            print(f"I didn't understand your response. Please try again.")



    








 


