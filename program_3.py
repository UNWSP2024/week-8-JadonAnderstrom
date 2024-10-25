# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).

import random  

# Dictionary of states and their capitals  (Went to Google for List)
states_key = {  
    'Alabama': 'Montgomery',  
    'Alaska': 'Juneau',  
    'Arizona': 'Phoenix',  
    'Arkansas': 'Little Rock',  
    'California': 'Sacramento',  
    'Colorado': 'Denver',  
    'Connecticut': 'Hartford',  
    'Delaware': 'Dover',  
    'Florida': 'Tallahassee',  
    'Georgia': 'Atlanta',  
    'Hawaii': 'Honolulu',  
    'Idaho': 'Boise',  
    'Illinois': 'Springfield',  
    'Indiana': 'Indianapolis',  
    'Iowa': 'Des Moines',   
    'Kansas': 'Topeka',  
    'Kentucky': 'Frankfort',  
    'Louisiana': 'Baton Rouge',  
    'Maine': 'Augusta',  
    'Maryland': 'Annapolis',  
    'Massachusetts': 'Boston',  
    'Michigan': 'Lansing',  
    'Minnesota': 'St. Paul',  
    'Mississippi': 'Jackson',  
    'Missouri': 'Jefferson City',  
    'Montana': 'Helena',  
    'Nebraska': 'Lincoln',  
    'Nevada': 'Carson City',  
    'New Hampshire': 'Concord',  
    'New Jersey': 'Trenton',  
    'New Mexico': 'Santa Fe',  
    'New York': 'Albany',  
    'North Carolina': 'Raleigh',  
    'North Dakota': 'Bismarck',  
    'Ohio': 'Columbus',  
    'Oklahoma': 'Oklahoma City',  
    'Oregon': 'Salem',  
    'Pennsylvania': 'Harrisburg',  
    'Rhode Island': 'Providence',    
    'South Carolina': 'Columbia',  
    'South Dakota': 'Pierre',  
    'Tennessee': 'Nashville',  
    'Texas': 'Austin',  
    'Utah': 'Salt Lake City',  
    'Vermont': 'Montpelier',  
    'Virginia': 'Richmond',  
    'Washington': 'Olympia',  
    'West Virginia': 'Charleston',  
    'Wisconsin': 'Madison',  
    'Wyoming': 'Cheyenne'  
}  

states_list = list(states_key.keys())  
correct_answer = 0  
incorrect_answer = 0  

# quiz  
print("Welcome to the Capital Quiz!")  
print("(Case Sensitive)")
print("Type 'exit' to end the quiz at any time.\n")  

while True:  
    # Randomly select a state  
    state = random.choice(states_list)  
    capital = states_key[state]  
  
    # Prompt user for the capital of the state  
    user_input = input(f"What is the capital of {state}?: ")  
    
    # Exit condition  
    if user_input.lower() == 'exit':  
        print("Thank you for participating!")  
        break  
    
    # Check if answer is correct  
    if user_input.strip() == capital:  
        correct_answer += 1  
        print("Correct!\n")  
    else:  
        incorrect_answer += 1  
        print(f"Incorrect! The capital of {state} is {capital}.\n")  
    
    # Display score  
    print(f"Correct answers: {correct_answer}\nIncorrect answers: {incorrect_answer}\n")

# Jadon Anderstrom, 10/25/2024, "Capital Quiz".
