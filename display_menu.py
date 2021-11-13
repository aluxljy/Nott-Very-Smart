import pandas as pd
import string

pd.set_option("display.max_rows", None, "display.max_columns", None)
food_list = pd.read_excel(r'C:\Users\M.I.C.H.E.L.L.E\Downloads\Food List.xlsx')
full_menu = pd.DataFrame(food_list)

inp = input("You: ")

request = string.capwords(str.lower(inp))
request = request.split()

request_list = list()
for word in request:
    if word not in request_list:
        request_list.append(word)

stalls = ['Malay', 'Mamak', 'Beverage', 'Korean', 'Japanese']
flag = 0

for word in request_list:
    flag += 1
    for stall in stalls:
        if word == stall:
            menu = full_menu.loc[full_menu['stall_name'] == word]
            menu = menu[['item_name', 'price', 'delivery_service']]
            #print("Bot: " + random.choice(responses))
            print("Bot: Here's the", word, "Stall's Menu.")
            print(menu.to_string(index=False))
        else:
            flag += 1

if flag == ((len(request_list) * len(stalls)) + len(request_list)):
    print("Bot: Not sure which menu you wish to view but here's everything that's available on our cafeteria's Menu.")
    print(full_menu.to_string(index=False))

