import pandas as pd
import string


def display_menu():
    pd.set_option("display.max_rows", None, "display.max_columns",
                  None)  # maximize number of rows and columns displayed
    pd.options.display.float_format = '{:,.2f}'.format  # format floating decimal point to 2 places
    food_list = pd.read_excel(r'Food List.xlsx')  # import excel file using pandas
    return pd.DataFrame(food_list)  # construct data frame for menu


def clean_input(inp):
    request = string.capwords(str.lower(inp))  # convert input to lowercase then capitalize first letter of each word
    request = request.split()  # split input to a list of words

    request_list = list()  # create new list to store non duplicated words
    for word in request:
        word = ''.join(character for character in word if character.isalnum())  # remove special characters in word
        if word not in request_list:
            request_list.append(word)  # add word to new list if not duplicated
    return request_list
