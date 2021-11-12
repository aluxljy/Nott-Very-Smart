import pandas as pd
import string

pd.set_option("display.max_rows", None, "display.max_columns", None)
food_list = pd.read_excel(r'C:\Users\M.I.C.H.E.L.L.E\Downloads\Food List.xlsx')
full_menu = pd.DataFrame(food_list)
print(full_menu.to_string(index=False))

request_menu = input("Please enter the stall's menu you would like to view: ")
request_menu = string.capwords(str.lower(request_menu))
stalls = ['Malay', 'Mamak', 'Beverage', 'Korean', 'Japanese']


def print_menu():
    flag = 0
    for stall in stalls:
        if request_menu == stall:
            menu = full_menu.loc[full_menu['stall_name'] == request_menu]
            print(menu.to_string(index=False))
        else:
            flag += 1
    if flag == len(stalls):
        print("Sorry,", request_menu, "is not a valid stall. Please try again.")


print_menu()
