import pandas as pd
import string

pd.set_option("display.max_rows", None, "display.max_columns", None)
food_list = pd.read_excel(r'C:\Users\M.I.C.H.E.L.L.E\Downloads\Food List.xlsx')
full_menu = pd.DataFrame(food_list)

inp = input("You: ")

request = string.capwords(str.lower(inp))
request = request.split()
stalls = ['Malay', 'Mamak', 'Beverage', 'Korean', 'Japanese']
flag = 0

for word in request:
    flag += 1
    for stall in stalls:
        if word == stall:
            menu = full_menu.loc[full_menu['stall_name'] == word]
            menu = menu[['item_name', 'price', 'delivery_service']]
            print(menu.to_string(index=False))
        else:
            flag += 1

if flag == ((len(request) * len(stalls)) + len(request)):
    print(full_menu.to_string(index=False))

