from menu import MENU,resources
account = 0
water = resources['water']
coffee = resources['coffee']
milk = resources['milk']

def is_resource_available(prompt) -> bool:
    if coffee < MENU[prompt]["ingredients"]["coffee"] :
        print("Sorry there is not enough coffee.")
        return False
    if water < MENU[prompt]["ingredients"]["water"] :
        print("Sorry there is not enough water.")
        return False
    if prompt != "espresso":
        if milk < MENU[prompt]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return False


    return True

def calculate_coins(q,d,n,p):
    return round((q*0.25)+(d*0.1)+(n*0.05)+(p*0.01),2)

def deduct_resources(prompt,w,m,c):
    w -= MENU[prompt]["ingredients"]["water"]
    c -= MENU[prompt]["ingredients"]["coffee"]
    if prompt != 'espresso':
        m -= MENU[prompt]["ingredients"]["milk"]
    return [w,c,m]



while True:
    prompt = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()


    if prompt == "off":
        break
    elif prompt == "report":
        print(f"Water: {water}ml\n"
              f"Milk: {milk}ml\n"
              f"Coffee: {coffee}g\n"
              f"Money: ${account}")
    else:
        available = is_resource_available(prompt)
        if not available:
            continue
        else:
            print("Please insert Coins.")
            quarters = int(input("How many Quarters? "))
            dimes = int(input("How many Dimes? "))
            nickles = int(input("How many Nickles? "))
            pennies = int(input("How many Pennies? "))

            money = calculate_coins(quarters,dimes,nickles,pennies)

            actual_cost = MENU[prompt]["cost"]

            if money == actual_cost:
                print(f"Here is your {prompt}. Enjoy!")
                account += actual_cost
                water,coffee,milk = deduct_resources(prompt,water,milk,coffee)
            elif money > actual_cost:
                print(f"Here is ${round(money - actual_cost,2)} in change.")
                print(f"Here is your{prompt}. Enjoy!")
                account += actual_cost
                water,coffee,milk = deduct_resources(prompt,water,milk,coffee)
            else:
                print("Sorry,That's not enough money.Money refunded.")
