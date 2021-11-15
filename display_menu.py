import string
import check_quit
import read_excel as r

full_menu = r.display_menu()


def menu():
    print("Bot: Which menu?")
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

    for word in request_list:
        for stall in stalls:
            if word == stall:
                menu = full_menu.loc[full_menu['stall_name'] == word]  # select certain rows by label stall_name
                menu = menu[['item_name', 'price', 'delivery_service']]  # display certain columns only
                # print("Bot: " + random.choice(responses))
                print("Bot: Here's the", word, "Stall's Menu.")
                print(menu.to_string(index=False))  # hide index of data frame
            else:
                flag += 1  # increment number of passes

    if flag == (len(request_list) * len(stalls)):
        print(
            "Bot: Not sure which menu you wish to view but here's everything that's available on our cafeteria's Menu.")
        print(full_menu.to_string(index=False))  # hide index of data frame

# menu()
