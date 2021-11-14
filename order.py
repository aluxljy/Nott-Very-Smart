import pandas as pd
import string

pd.set_option("display.max_rows", None, "display.max_columns", None)  # maximize number of rows and columns displayed
pd.options.display.float_format = '{:,.2f}'.format  # format floating decimal point to 2 places
food_list = pd.read_excel(
    r'C:\Users\User\Desktop\Qian Hui\Nott-A-Code\Food List 2.xlsx')  # import excel file using pandas
full_menu = pd.DataFrame(food_list)  # construct data frame for menu
complete_order = list()


def place_order(complete_order):
    print("Bot: Please enter the name of food or beverage you would like to order.")
    inp = input("You: ")

    request = str.lower(inp)

    items = full_menu['item_name'].values.tolist()
    items_list = list()

    for item in items:
        items_list.append(item.lower())
    flag = 0  # flag to keep track of the overall passes in the loop

    # print(items_list)
    # print(request)

    for item in items_list:
        if item in request:
            order_name = full_menu.loc[full_menu['item_name'].str.lower() == item.lower()]
            complete_order.append(order_name['item_name'].to_string(index=False, header=False))
            # print(complete_order)
            order_list = full_menu.loc[full_menu['item_name'].str.lower() == item.lower()]
            order_list = order_list[['item_name', 'price', 'delivery_service']]  # display certain columns only
            print("Here is your order: ")
            print(order_list.to_string(index=False))
            if not confirm_order():
                if not cancel_order():
                    print("Here is your order:")
                    print(order_list.to_string(index=False))
                else:
                    complete_order.pop()
            yes = 'y'
            ans = input("Do you want to make another order? (Y/N) ")
            ans = ans.lower()
            if yes in ans:
                place_order(complete_order)
            else:
                i = 0
                if len(complete_order) != 0:
                    delivery_service(complete_order)
                    print("Here is your receipt: ")
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
    confirm = input("Confirm? (Y/N) ")
    confirm = confirm.lower()
    if 'y' in confirm:
        return True
    else:
        return False


def cancel_order():
    cancel = input("Are you sure you want to cancel this order? (Y/N) ")
    cancel = cancel.lower()
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
        print("Bot: Delivery Service can be done!")
    else:
        print("Bot: Please come and collect ur food at uni cafeteria in 20 minutes!")

# place_order(complete_order)
