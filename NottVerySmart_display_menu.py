import NottVerySmart_check_quit as check_quit
import NottVerySmart_functions as f

full_menu = f.display_menu()


def show_menu():
    print("Bot: Which menu?")
    inp = input("You: ")
    check_quit.quit_system(inp)

    request_list = f.clean_input(inp)

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

