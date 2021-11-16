import NottVerySmart_check_quit as check_quit
import NottVerySmart_functions as f

full_menu = f.display_menu()
complete_order = list()


def place_order(complete_order):
    print("Bot: Please enter the name of the food or beverage you would like to order.")
    inp = input("You: ")
    check_quit.quit_system(inp)

    request = str.lower(inp)

    items = full_menu['item_name'].values.tolist()
    items_list = list()

    for item in items:
        items_list.append(item.lower())
    flag = 0  # flag to keep track of the overall passes in the loop

    for item in items_list:
        ##############################################
        # Skip for loop for the following conditions #
        ##############################################
        if item.lower() == 'kimchi' and request.lower() == "kimchi fried rice":
            continue
        if item.lower() == 'bulgogi' and request.lower() == "bulgogi with rice":
            continue
        if item.lower() == 'miso soup' and request.lower() in ["chicken teriyaki lunch set (miso soup)",
                                                               "tempura lunch set (miso soup)",
                                                               "vegetarian lunch Set (miso soup)"]:
            continue
        if item.lower() == 'chawanmushi' and request.lower() in ["chicken teriyaki dinner set (chawanmushi)",
                                                                 "tempura dinner set (chawanmushi)",
                                                                 "vegetarian dinner set (chawanmushi)"]:
            continue
        if item.lower() == 'tempura' and request.lower() in ["tempura soba",
                                                             "zaru soba + tempura",
                                                             "tempura udon", "zaru udon + tempura",
                                                             "tempura lunch set (miso soup)",
                                                             "tempura dinner set (chawanmushi)"]:
            continue
        if item.lower() == 'zaru soba' and request.lower() == "zaru soba + tempura":
            continue
        if item.lower() == 'zaru udon' and request.lower() == "zaru udon + tempura":
            continue

        if item in request:
            order_name = full_menu.loc[full_menu['item_name'].str.lower() == item.lower()]
            complete_order.append(order_name['item_name'].to_string(index=False, header=False)) # insert the ordered items into a list
            order_list = full_menu.loc[full_menu['item_name'].str.lower() == item.lower()]
            order_list = order_list[['item_name', 'price', 'delivery_service']]  # display certain columns only
            print("Bot: Here is your order: ")
            print(order_list.to_string(index=False))
            if not confirm_order():  # ask user to confirm order
                if not cancel_order():  # check whether want to cancel order or not
                    print("Bot: Here is your order:")
                    print(order_list.to_string(index=False))
                else:
                    complete_order.pop()
            yes = 'y'
            print("Bot: Do you want to make another order? (Y/N) ")
            ans = input("You: ")
            ans = ans.lower()
            check_quit.quit_system(ans)
            if yes in ans:
                place_order(complete_order)
            else:
                i = 0
                if len(complete_order) != 0:  # check whether the user has order any food or beverages
                    delivery_service(complete_order)
                    print("Bot: Here is your receipt: ")
                    for item_name in complete_order:
                        order_list = full_menu.loc[full_menu['item_name'].str.lower() == item_name.lower()]
                        order_list = order_list[['item_name', 'price', 'delivery_service']]
                        if i == 0:
                            print(order_list.to_string(index=False))
                            i += 1
                        else:
                            print(order_list.to_string(index=False, header=False))
                    calculate_price(complete_order)
                else:
                    print("Bot: Seem like you did not order anything :(")
                    quit()
        else:
            flag += 1  # increment number of passes

        if flag == len(items_list):
            print("Bot: Sorry, the food/beverage is not available.")
            place_order(complete_order)


# ask user to confirm order
def confirm_order():
    print("Bot: Confirm? (Y/N) ")
    confirm = input("You: ")
    confirm = confirm.lower()
    check_quit.quit_system(confirm)
    if 'y' in confirm:
        return True
    else:
        return False


# if user chooses not to confirm order, then it will ask the user again to ensure the user wants to cancel order
def cancel_order():
    print("Bot: Are you sure you want to cancel this order? (Y/N) ")
    cancel = input("You: ")
    cancel = cancel.lower()
    check_quit.quit_system(cancel)
    if 'y' in cancel:
        return True
    else:
        return False


# calculate the total price of the order
def calculate_price(complete_order):
    total_price = 0
    for item_name in complete_order:
        order = full_menu.loc[full_menu['item_name'].str.lower() == item_name.lower()]
        price = order['price'].to_string(index=False, header=False)
        price = float(price)
        total_price += price
    total_price = "{:.2f}".format(total_price)
    print("Bot: Total price: RM " + total_price)
    print("Bot: Please pay RM " + total_price + " upon collection or delivery of your order.")
    print("Bot: Thanks for ordering! ")


# if all the items ordered provide delivery service, then will auto deliver, else pick up
def delivery_service(complete_order):
    number = 0
    for item_name in complete_order:
        order = full_menu.loc[full_menu['item_name'].str.lower() == item_name.lower()]
        delivery = order['delivery_service'].to_string(index=False, header=False)
        if delivery == 'yes':
            number += 1
    if number == len(complete_order):
        print("\nBot: Delivery Service can be done!")
        while True:
            print("Bot: Please enter your address.")  # ask for customer's address
            address = input("You: ")
            print("Bot: Your address is " + address)
            print("Bot: Confirm? (Y/N) ")
            ans = f.take_input()
            if 'y' in ans:
                print("Bot: Address recorded!")
                break
    else:
        print("\nBot: Please come and collect your food at Uni Cafeteria in 20 minutes!")
