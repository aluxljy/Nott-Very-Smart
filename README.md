# Team Name: Nott-Very-Smart
# Authors: Looi Jie Ying, Liew Qian Hui
# Project Name: Food Ordering Chatbot
# Date: 10/11/2021

To run the project:
1. Clone the repository to your local repository/dowload the entire folder to your local machine
2. Open the project in your desired IDE
3. Run only the NottVerySmart_main.py file and the chatbot will be ready to go

All the files used to build this project:
1. Food List.xlsx   (added a new column is_beverage to indicate whether the item is a beverage)
2. NottVerySmart_check_quit.py   (detects the word "quit" and exit the program if detected)
3. NottVerySmart_display_menu.py   (displays menu based on stall preference)
4. NottVerySmart_functions.py   (consists several common functions used among the files)
5. NottVerySmart_information.py   (provides details of the items)
6. NottVerySmart_intents.json   (json file consists of data that includes tags, patterns and responses used to train the model)
7. NottVerySmart_main.py   (handles the model training and linking the all functionalities of the chatbot together)
8. NottVerySmart_model.tflearn.data-00000-of-00001   (to store trained model data)
9. NottVerySmart_model.tflearn.index   (to store trained model data)
10. NottVerySmart_model.tflearn.meta   (to store trained model data)
11. NottVerySmart_order.py   (handles the food ordering process)
12. NottVerySmart_recommendation.py   (provides food and beverage recommendations based on stall preference)
13. NottVerySmart_spelling.txt   (text file that consists of 5 words that can be detected if spelling error is present)
14. NottVerySmart_spelling_error_detector.py   (detects spelling errors and performs spelling correction)

Moving forward/scalability:
1. Shortcomings and improvements that can be made on the chatbot
- Spelling error detector:
(a)Shortcomings: can only detect single words and not a string of words, can only detect spelling errors to a certain extent, words that are able to be detected are limited
(b)Improvements: add more words to the dictionary, generate another function to accommodate more variants of the words to increase sensitivity
- Data in the json file: 
(a)Shortcomings: might not be sufficient to train a highly accurate model, however if more data is fed into the json file, greater noise may also be introduced
(b)Improvements: include more but important keywords under each tag
- Cleanliness of the codes:
(a)Shortcomings: codes may not be clean enough due to time constraints
(b)Improvements: do more refactoring on the codes and reduce repetitive codes as much as possible
- Print receipt function:
(a)Shortcomings: unable to save receipts automatically
(b)Improvements: add functions to allow the users to save the receipts in the form of a txt file for reference

2. Strategies to upscale the chatbot
- Build a GUI interface for the chatbot to elevate user experience
- Embed the chatbot to web applications or mobile applications so that it can be exposed to a wider range of users
- Develop a dedicated application to the chatbot to enable more functionalities and interactions
- Add more advanced functionalities to the chatbot to accommodate greater humanized services

3. Market potential of the chatbot
- Can be expanded and used in wide variety of restaurants and cafeterias within Malaysia to provide a speedy and humanized food ordering service
- Able to bring convenience to customers when ordering food especially during these trying times where human and human interactions are encouraged to be reduced
- Able to increase customer experience and customer loyalty by providing personalized services accompanied by an one-on-one chat experience
- Provide high availabilty and fast responses to satisfy the customer's requests and at the same time reducing costs for customer service as the need for employees is reduced
- Help understand the customers' needs by collecting and storing data and analyzing queries to understand the market demand and enhance productivity

