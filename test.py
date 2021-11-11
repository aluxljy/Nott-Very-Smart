import pandas as pd

pd.set_option("display.max_rows", None, "display.max_columns", None)
food_list = pd.read_excel(r'C:\Users\M.I.C.H.E.L.L.E\Downloads\Food List.xlsx')
df = pd.DataFrame(food_list)
print(df)
#print(food_list)

menu = pd.DataFrame(food_list, columns=['stall_name', 'item_name', 'price'])
delivery = food_list[["stall_name", "item_name", "delivery_service"]]
#print(menu)
#print(delivery)