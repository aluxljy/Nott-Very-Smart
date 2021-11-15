import pandas as pd


def display_menu():
    pd.set_option("display.max_rows", None, "display.max_columns",
                  None)  # maximize number of rows and columns displayed
    pd.options.display.float_format = '{:,.2f}'.format  # format floating decimal point to 2 places
    food_list = pd.read_excel(r'Food List.xlsx')  # import excel file using pandas
    return pd.DataFrame(food_list)  # construct data frame for menu
