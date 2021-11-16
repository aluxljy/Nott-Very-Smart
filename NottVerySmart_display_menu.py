import NottVerySmart_check_quit as check_quit
import NottVerySmart_functions as f
import NottVerySmart_spelling_error_detector as error_detector

full_menu = f.display_menu()


def show_menu():
    print("Bot: Which stall's menu do you wish to look at?")
    inp = input("You: ")
    check_quit.quit_system(inp)

    request_list = f.clean_input(inp)

    corrected = list()

    for request in request_list:
        if error_detector.correction(request) != request:
            for wl in error_detector.word_list:
                if error_detector.correction(request) == wl:
                    yes = 'y'
                    print("Bot: Instead of " + request + " did you mean " + wl + "? (Y/N)")
                    ans = input("You: ")
                    ans = ans.lower()  # convert to lowercase
                    check_quit.quit_system(ans)  # check for the word "quit"
                    if yes in ans:
                        corrected.append(error_detector.correction(request))
                    else:
                        corrected.append(" ")

    request_list.extend(corrected)

    stalls = ['Malay', 'Mamak', 'Beverage', 'Korean', 'Japanese']
    flag = 0  # flag to keep track of the overall passes in the loop

    for word in request_list:
        for stall in stalls:
            if word == stall:
                menu = full_menu.loc[full_menu['stall_name'] == word]  # select certain rows by label stall_name
                menu = menu[['item_name', 'price', 'delivery_service']]  # display certain columns only
                print("Bot: Here's the", word, "Stall's Menu.")
                print(menu.to_string(index=False))  # hide index of data frame
            else:
                flag += 1  # increment number of passes

    if flag == (len(request_list) * len(stalls)):
        print(
            "Bot: Not sure which menu you wish to view but here's everything that's available on our cafeteria's Menu.")
        print(full_menu.to_string(index=False))  # hide index of data frame


