# Group Name: Nott-Very-Smart
# Authors: Looi Jie Ying, Liew Qian Hui
# Project Name: Food Ordering Chatbot
# Date: 10/11/2021

################################
# import libraries and modules #
################################
import string
import tensorflow as tf
import tflearn
import nltk
from nltk.stem.lancaster import LancasterStemmer
import json
import numpy as np
import random
import NottVerySmart_display_menu as display_menu
import NottVerySmart_order as order
import NottVerySmart_check_quit as check_quit
import NottVerySmart_recommendation as recommendation
import NottVerySmart_information as information
import NottVerySmart_functions as f

stemmer = LancasterStemmer()
nltk.download('punkt')
nltk.download('wordnet')

#########################
# Get data from intents #
#########################
with open('NottVerySmart_intents.json') as file1:
    data = json.load(file1)

######################
# Create empty lists #
######################
words = []  # holds tokenized words in pattern
tags_name = []  # holds all the tag names without repetition
patterns = []  # holds all the user input pattern
tags_of_patterns = []  # holds the tag name of the pattern
root_words = []  # holds all the root words
training = []  # holds training data
output = []  # holds output data

for intent in data['intents']:
    tags_name.append(intent['tag'])  # insert all the tags name into tags_name[]
    for pattern in intent['patterns']:
        single_word = nltk.word_tokenize(pattern)  # tokenize the words in pattern
        words.extend(single_word)  # insert tokenized words into words[]
        patterns.append(single_word)  # insert tokenized words in pattern list into patterns[]
        tags_of_patterns.append(intent["tag"])

tags_name = sorted(tags_name)

##################################
# Get the root words by stemming #
##################################
for w in words:
    if w not in string.punctuation:
        root_words.append(stemmer.stem(w.lower()))

root_words = sorted(set(root_words))

#############################
# Create bag of words model #
#############################
out_empty = [0 for _ in range(len(tags_name))]  # 0 for all tags in intents

for index, details in enumerate(patterns):
    bag = []
    text = [stemmer.stem(w.lower()) for w in details]
    for w in root_words:
        if w in text:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[tags_name.index(tags_of_patterns[index])] = 1

    training.append(bag)
    output.append(output_row)

####################################################
# Convert training data and output to numpy arrays #
####################################################
training = np.array(training)
output = np.array(output)

####################################################
# Convert training data and output to numpy arrays #
####################################################
tf.compat.v1.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    model.load("NottVerySmart_model.tflearn")
except:
    model = tflearn.DNN(net)
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("NottVerySmart_model.tflearn")


###############################
# Check the data in the lists #
###############################
def printdata():
    print(words)
    print(tags_name)
    print(patterns)
    print(tags_of_patterns)
    print(root_words)


########################
# Bag of word function #
########################


def bag_of_words(s, root_words):
    bag = [0 for _ in range(len(root_words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(root_words):
            if w == se:
                bag[i] = 1

    return np.array(bag)


#################
# Chat function #
#################


def chat():
    print("Welcome to Uni Cafeteria Food Ordering System!")
    print("You can always type quit to stop!")
    print("\nBot: How can I help you? ")
    while True:
        inp = input("You: ")

        check_quit.quit_system(inp)

        results = model.predict([bag_of_words(inp, root_words)])[0]
        results_index = np.argmax(results)
        tag = tags_name[results_index]

        if results[results_index] > 0.7:
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']

            # print responses based on the respective tag the user input falls in
            if tag in ["greeting_question1", "greeting_question2", "greeting_question3", "greeting_slang",
                       "greeting_casual1", "greeting_casual2", "greeting_formal"]:
                print("Bot: " + random.choice(responses))  # print random responses
                print("Bot: How can I help you?")
                print("Bot: You can ask for recommendations, request for the menu, place orders and ask queries.")
            elif tag == "goodbye":
                print("Bot: " + random.choice(responses))  # print random responses
                break
            elif tag == "menu":
                display_menu.show_menu()  # print full menu
                while True:
                    yes = 'y'
                    print("Bot: Do you want to have a look at a specific stall's menu? (Y/N) ")
                    ans = f.take_input()
                    if yes in ans:
                        display_menu.show_menu()  # print respective menu based on user input
                    else:
                        print("Bot: Do you want to order now? (Y/N) ")
                        ans = f.take_input()
                        if yes in ans:
                            complete_order = list()  # create new list
                            order.place_order(complete_order)  # place order and print receipt
                            quit()
                        else:
                            print("Bot: How can I help you next? ")
                            break
            elif tag == "place_order":
                complete_order = list()  # create new list
                order.place_order(complete_order)  # place order and print receipt
                quit()
            elif tag == "food_recommendation":
                print("Bot: " + random.choice(responses))  # print random responses
                print("Bot: Do you want me to make recommendation based on stalls? (Y/N) ")
                inp = f.take_input()
                if 'y' in inp:
                    print("Bot: Which stall would you wish the recommendation to be based on? ")
                    recommendation.recommend("no")  # recommendation based on food
                    print("Bot: How can I help you next? ")
                else:
                    print("Bot: How can I help you next? ")
            elif tag == "beverage_recommendation":
                print("Bot: " + random.choice(responses))  # print random responses
                print("Bot: Do you want me to make recommendation based on stalls? (Y/N) ")
                inp = f.take_input()
                if 'y' in inp:
                    print("Bot: Which stall would you wish the recommendation to be based on? ")
                    recommendation.recommend("yes")  # recommendation based on beverage
                    print("Bot: How can I help you next? ")
                else:
                    print("Bot: How can I help you next? ")
            elif tag == 'details':
                information.info(inp)  # print item details based on user input
                print("Bot: How can I help you next? ")
            else:
                print("Bot: " + random.choice(responses))  # print random responses
        else:
            print("Bot: I don't understand.. can you rephrase your word :(")
            print("Bot: Or rather, you can try typing words such as recommendation, menu, stalls, hours, overall price or delivery service.")


chat()
