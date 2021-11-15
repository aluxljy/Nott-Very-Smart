import read_excel as r

full_menu = r.display_menu()


def info(inp):
    # inp = input("You: ")

    request = str.lower(inp)

    flag = 0

    items = full_menu['item_name'].values.tolist()
    lower_items = list()

    for item in items:
        lower_items.append(item.lower())

    for lower_item in lower_items:
        if lower_item in request:
            detail = full_menu.loc[full_menu['item_name'].str.lower() == lower_item]
            detail = detail[['stall_name', 'item_name', 'price', 'delivery_service']]
            print(detail.to_string(index=False))
        else:
            flag += 1

        if flag == len(lower_items):
            print("Bot: The food/ beverage is not available.")
