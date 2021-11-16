import NottVerySmart_functions as f

full_menu = f.display_menu()


def info(inp):

    request = str.lower(inp)  # convert to lowercase

    flag = 0  # flag to keep track of the overall passes in the loop

    items = full_menu['item_name'].values.tolist()  # convert elements in data frame into a list
    lower_items = list()  # create new list

    for item in items:
        lower_items.append(item.lower())  # append to list

    for lower_item in lower_items:
        if lower_item in request:
            detail = full_menu.loc[full_menu['item_name'].str.lower() == lower_item]  # select certain rows by label item_name
            detail = detail[['stall_name', 'item_name', 'price', 'delivery_service']]  # # display certain columns only
            print(detail.to_string(index=False))  # hide index of data frame
        else:
            flag += 1  # increment number of passes

        if flag == len(lower_items):
            print("Bot: Sorry, the food/beverage is not available.")
