import pandas
import random
#List Comprehension----------------------------------------------------------------------------------------
#new_list = [new_item for item in list]

#Usual method for creating a new list based off another list:
new_numbers = []
numbers = [1,2,3]
for number in numbers:
    add_1 = number + 1
    new_numbers.append(add_1)

#Re-written in List Comprehension... looks like this:
new_list = [n + 1 for n in new_numbers]
#Note: Make sure you match your variables. Note both are 'n' above.

#Python Sequences: list, range, string, tuple... (Have a specific order)

#Using range: Takes range(1,5), doubles it, and puts it in a list.
range_list = [num *2 for num in range(1,5)]

#Conditional List Comprehension
#new_list = [new_item for item in list if test]
name_list = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in name_list if len(name) < 5]
#print(short_names)

#Alter the list items...
uppercase_long = [name.upper() for name in name_list if len(name) > 5]
#print(uppercase_long)

#Dictionary Comprehension-------------------------------------------------------------------------------------
#new_dict = {new_key:new_value for item in (list or range or string or any iterable)}

#new_dict = {new_key:new_value for (key,value) in dict.items() if test}
name_list2 = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
scores = {student:random.randint(1,100) for student in name_list2}
#print (scores)
#------------------This..............Matches this
passed_students = {student:score for student,score in scores.items() if score >= 60}
#print(passed_students)

#Test-----------------------
#Use Dictionary Comprehension to create a dictionary called result that
# takes each word in the given sentence and calculates the number of letters in each word.
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
split_sentence = sentence.split()
result = {word:len(word) for word in split_sentence}

#Test2----------------------
#Use Dictionary Comprehension to create a dictionary called weather_f that takes
# each temperature in degrees Celsius and converts it into degrees Fahrenheit.
# Celsius to Fahrenheit formula: (temp_c * 9/5) + 32 = temp_f
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:(temp * 9/5 + 32) for day,temp in weather_c.items()}
#print(weather_f)

#-----------------------------
student_dict = {
    "student":["Angela", "James", "Lily"],
    "score": [66,76,86]
}
#Looping through dictionaries
# for (key, value) in student_dict.items():
#     print(f"{key}: {value}")

#Panda DataFrame--------------
student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)

#Loop through the data frame
# for (key, value) in student_data_frame.items():
#     print(value)

#Loop through the data rows instead of the columns
for (index, row) in student_data_frame.iterrows():
    #print(row)
    print(row.student)
    #print(row.score)
