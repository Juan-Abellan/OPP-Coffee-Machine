from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO: STARTING CONDITIONS
still_working = True

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

# TODO: FLOW
while still_working:
    choice = input(f"What would you like? {my_menu.get_items()}: ").lower()
    if choice == "off":
        still_working = False
        print("Switching off ...")
    elif choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        # print(f"{choice = }")
        if my_menu.find_drink(order_name=choice):
            if my_coffee_maker.is_resource_sufficient(drink=my_menu.find_drink(order_name=choice)):
                if my_money_machine.make_payment(cost=my_menu.find_drink(order_name=choice).cost):
                    my_coffee_maker.make_coffee(order=my_menu.find_drink(order_name=choice))

    # print(f"""
    # TESTING MENU ........................................................................
    # ATTRIBUTES
    # {my_menu.menu = }
    # {type(my_menu.menu) = }
    # ---
    # {my_menu.menu[0] = }
    # {type(my_menu.menu[0]) = }
    # ---
    # {my_menu.menu[0].name = }
    # {type(my_menu.menu[0].name) = }
    #
    # METHODS
    # {my_menu.get_items() = }
    # {type(my_menu.get_items()) = }
    # {my_menu.find_drink(order_name=choice) = }
    # .....................................................................................
    # """)
    #
    # print(f"""
    # TESTING COFFEE_MAKER .................................................................
    # ATTRIBUTES
    # {my_coffee_maker.resources = }
    # {type(my_coffee_maker.resources) = }
    #
    # METHODS
    # {my_coffee_maker.report() = }
    # {type(my_coffee_maker.report()) = }
    # {my_coffee_maker.is_resource_sufficient(drink=my_menu.find_drink(order_name=choice)) = }
    # .....................................................................................
    # """)

    # print(f"""
    # TESTING MONEY_MACHINE .................................................................
    #
    # ATTRIBUTES
    # {my_money_machine.process_coins() = }
    #
    # """)
