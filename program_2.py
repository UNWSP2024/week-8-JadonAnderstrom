# Program #2: Word Separator  
# Write a program that accepts as input a sentence in which all of the words are run together,   
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces,  
# and the first word starts with an uppercase.  
# For example, the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."  

def word_separator(sentence):  
    new_sentence = ""  
    
    for char in sentence:  

        if char.isupper() and new_sentence:  # Add a space if it's not the first character  
            new_sentence += " "  

        new_sentence += char.lower() if new_sentence else char  
    
    return new_sentence.strip()  
 
sentence = input('Enter a sentence with no spaces, but capitalize the beginning of each word. The rest is magic!: ')  

new_sentence = word_separator(sentence)  

if new_sentence:  
    new_sentence = new_sentence[0].upper() + new_sentence[1:] + '.'  

print(new_sentence)

# Jadon Anderstrom, 10/25/2024, "Word Separator".
