# Program #1: Initials  
# Write a program that gets a string containing a person's first, middle, and last names,   
# and displays their first, middle, and last initials.  
# For example, if the user enters John William Smith, the program should display J. W. S.  

def initials_generator(personsName):  
    
    personsInitials = ""  
    
    #    Add your logic here
    name_parts = personsName.split()  
    
    for part in name_parts:  
        if part:  # Check that the part is not empty  
            personsInitials += part[0].upper() + ". "
            
    return personsInitials.strip()  

personsName = input('Enter the user\'s first, middle, and last name: ')  

initials = initials_generator(personsName)  

print(initials)

#Jadon Anderstrom, 10/25/2024, "Initials".
