# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject. 
courses = {}  
course_ids = []  
continue_input = "yes"  
matched_courses = []  
  
while continue_input.lower() != "no":  
    course_id = input("Enter the course ID: ")  
    course_title = input("Enter the course title: ")  
    course_ids.append(course_id)  
    courses[course_id] = course_title  
    continue_input = input("Would you like to add another course? (yes/no): ")  

def find_courses(keyword, course_ids):  
    results = []  
    for course_id in course_ids:  
        if keyword.lower() in course_id.lower():  
            results.append(courses[course_id])  
    return results  

search_keyword = input("Enter the ID number to search for titles: ")  
matched_courses = find_courses(search_keyword, course_ids)  
print(f"Matching courses: {matched_courses}")

# Jadon Anderstrom, 10/25/2024, "Course Info".
