import pandas as pd

pd.set_option("display.max_rows", None, "display.max_columns", None)  # maximize number of rows and columns displayed
pd.options.display.float_format = '{:,.2f}'.format  # format floating decimal point to 2 places
food_list = pd.read_excel(r'Food List.xlsx')  # import excel file using pandas
full_menu = pd.DataFrame(food_list)  # construct data frame for menu

inp = input("You: ")

request = str.lower(inp)

items = full_menu['item_name'].values.tolist()
lower_items = list()

for item in items:
    lower_items.append(item.lower())

for lower_item in lower_items:
    if lower_item in inp:
        detail = full_menu.loc[full_menu['item_name'].str.lower() == lower_item]
        detail = detail[['stall_name', 'item_name', 'price', 'delivery_service']]
        print(detail.to_string(index=False))


