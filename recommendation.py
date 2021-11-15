import string
import random
import check_quit

import read_excel as r

full_menu = r.display_menu()


def recommend(is_beverage):
    inp = input("You: ")
    check_quit.quit_system(inp)

    request = string.capwords(str.lower(inp))  # convert input to lowercase then capitalize first letter of each word
    request = request.split()  # split input to a list of words

    request_list = list()  # create new list to store non duplicated words
    for word in request:
        word = ''.join(character for character in word if character.isalnum())  # remove special characters in word
        if word not in request_list:
            request_list.append(word)  # add word to new list if not duplicated

    stalls = ['Malay', 'Mamak', 'Beverage', 'Korean', 'Japanese']
    flag = 0  # flag to keep track of the overall passes in the loop

    # is_beverage = "no"

    for word in request_list:
        for stall in stalls:
            if word == stall:
                menu = full_menu.groupby('stall_name')  # group data frame by stall_name column
                menu = menu.get_group(word)  # get stall_name group based on user input of word
                if is_beverage == "yes":
                    try:
                        menu = menu.groupby('is_beverage')  # group data frame by is_beverage column
                        menu = menu.get_group(is_beverage)  # get is_beverage group based on is_beverage flag
                        recommendation = menu.sample(n=1, weights='price',
                                                     random_state=random.randint(0, 21))  # sample a random row
                        item = recommendation['item_name'].to_string(index=False,
                                                                     header=False)  # hide index and header of data frame
                        item_price = recommendation['price'].to_string(index=False,
                                                                       header=False)  # hide index and header of data frame
                        item_delivery = recommendation['delivery_service'].to_string(index=False,
                                                                                     header=False)  # hide index and header of data frame
                        print("Bot: For the " + word + " Stall, I recommend " + item + " which costs RM" + item_price + ".")
                        print("Bot: Delivery service status -> " + item_delivery + ".")

                    except KeyError:
                        print("Bot: Sorry, the", word, "Stall doesn't sell beverages :(")

                else:
                    try:
                        menu = menu.groupby('is_beverage')  # group data frame by is_beverage column
                        menu = menu.get_group(is_beverage)  # get is_beverage group based on is_beverage flag
                        recommendation = menu.sample(n=1, weights='price',
                                                     random_state=random.randint(0, 21))  # sample a random row
                        item = recommendation['item_name'].to_string(index=False,
                                                                     header=False)  # hide index and header of data frame
                        item_price = recommendation['price'].to_string(index=False,
                                                                       header=False)  # hide index and header of data frame
                        item_delivery = recommendation['delivery_service'].to_string(index=False,
                                                                                     header=False)  # hide index and header of data frame
                        print("Bot: For the " + word + " Stall, I recommend " + item + " which costs RM" + item_price + ".")
                        print("Bot: Delivery service status -> " + item_delivery + ".")

                    except KeyError:
                        print("Bot: Sorry, the", word, "Stall doesn't sell food :(")

            else:
                flag += 1  # increment number of passes

    if flag == (len(request_list) * len(stalls)):
        available_stalls = full_menu.drop_duplicates(subset='stall_name')
        available_stalls = available_stalls[['stall_name']]  # display certain column only
        print("Bot: Sorry, I think you've entered an invalid stall name. Please check your spelling again.")
        print("Bot: Or rather, have a look at the stalls available in our cafeteria.")
        print(available_stalls.to_string(index=False))  # hide index of data frame

