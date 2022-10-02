# ----- Function and Logic Section ----- #
def user_order():
    '''This function takes the order of a customer and prints out his order, to exit the function type "quit"'''
    counter = 0
    while True:
        user_input = input("> ").title()
        if user_input == "Quit":
            if counter != 0:
                print("\nYour order is: \n")
                for i in orders:
                    if orders[i] != 0:
                        print(f' - {orders[i]} {i}')
                print("\n")
            else:
                print("\n")
                print("Bye...Bye...")
                print("\n")
            break
        if user_input in orders:
            orders[f"{user_input}"] += 1
             
            if  orders[f"{user_input}"] == 1:
                print(f"** {orders[f'{user_input}']} order of {user_input} have been added to your meal **")
            else:
                print(f"** {orders[f'{user_input}']} orders of {user_input} have been added to your meal **")
        else:
            print(f"Sorry we don't have {user_input} in our menu")
        counter += 1
                

# ----- Execution Section ----- #

if __name__ == "__main__":

    MENU = '''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Beverages
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************'''

    orders = {
        "Wings": 0,
        "Cookies": 0,
        "Spring Rolls": 0,
        "Salmon": 0,
        "Steak": 0,
        "Meat Tornado": 0,
        "A literal Garden": 0,
        "Ice Cream": 0,
        "Cake": 0,
        "Pie": 0,
        "Coffee": 0,
        "Tea": 0,
        "Unicorn Tears": 0
    }

    print(MENU)
    user_order()
