import check_quit
import functions as f

full_menu = f.display_menu()
complete_order = list()


def place_order(complete_order):
    print("Bot: Please enter the name of food or beverage you would like to order.")
    inp = input("You: ")
    check_quit.quit_system(inp)

    request = str.lower(inp)

    items = full_menu['item_name'].values.tolist()
    items_list = list()

    for item in items:
        items_list.append(item.lower())
    flag = 0  # flag to keep track of the overall passes in the loop

    # print(items_list)
    # print(request)

    for item in items_list:
        if item.lower() == 'kimchi' and request.lower() == "kimchi fried rice":
            continue
        if item in request:
            order_name = full_menu.loc[full_menu['item_name'].str.lower() == item.lower()]
            complete_order.append(order_name['item_name'].to_string(index=False, header=False))
            # print(item)
            # print(request)
            # print(complete_order)
            order_list = full_menu.loc[full_menu['item_name'].str.lower() == item.lower()]
            order_list = order_list[['item_name', 'price', 'delivery_service']]  # display certain columns only
            print("Bot: Here is your order: ")
            print(order_list.to_string(index=False))
            if not confirm_order():
                if not cancel_order():
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
                if len(complete_order) != 0:
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
                    print("Bot: Seem like you do not order anything :(")
                    quit()
        else:
            flag += 1  # increment number of passes

        if flag == len(items_list):
            print("Bot: The food/ beverage is not available.")
            place_order(complete_order)


def confirm_order():
    print("Bot: Confirm? (Y/N) ")
    confirm = input("You: ")
    confirm = confirm.lower()
    check_quit.quit_system(confirm)
    if 'y' in confirm:
        return True
    else:
        return False


def cancel_order():
    print("Bot: Are you sure you want to cancel this order? (Y/N) ")
    cancel = input("You: ")
    cancel = cancel.lower()
    check_quit.quit_system(cancel)
    if 'y' or 'Y' in cancel:
        return True
    else:
        return False


def calculate_price(complete_order):
    total_price = 0
    for item_name in complete_order:
        order = full_menu.loc[full_menu['item_name'].str.lower() == item_name.lower()]
        price = order['price'].to_string(index=False, header=False)
        # print(price)
        price = float(price)
        total_price += price
    total_price = "{:.2f}".format(total_price)
    print("Bot: Total price: RM " + total_price)
    print("Bot: Please pay RM " + total_price + " upon collection or delivery of food.")
    print("Bot: Thanks for ordering! ")


def delivery_service(complete_order):
    number = 0
    for item_name in complete_order:
        order = full_menu.loc[full_menu['item_name'].str.lower() == item_name.lower()]
        delivery = order['delivery_service'].to_string(index=False, header=False)
        if delivery == 'yes':
            number += 1
    if number == len(complete_order):
        print("\nBot: Delivery Service can be done!")
    else:
        print("\nBot: Please come and collect ur food at uni cafeteria in 20 minutes!")

# place_order(complete_order)
