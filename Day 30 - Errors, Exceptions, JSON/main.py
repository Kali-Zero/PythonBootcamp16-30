
#-----JSON JavaScript Object Notation-----------------------------------
#It's just a bunch of dictionaries and list?!

#Write
#---json.dump()

#Read
#---json.load()

#Update
#---json.update()


#-----Catching Exceptions-----------------------------------------------
# try: #Something that MIGHT cause and exception
#     pass
# except: #Do this if there WAS an exception (Try to specify exception type you expect)
#     pass
# else: #Do this if there were NO exceptions
#     pass
# finally: #Do this NO MATTER WHAT happens
#     raise TypeError("It's broke!") #Select your own exception case

#-----CCommon Errors----------------------------------------------------

#FileNotFound
# with open("a_file.txt") as file:
#     file.read()

#KeyError
# a_dictionary = {"Key":"Value"}
# value = a_dictionary["non_existent_key"]

#IndexError
# fruit_list = ["apple", "banana", "orange"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)

#-----Examples----------------------------------------------------

# try:
#     file = open('a_file.txt')
#     a_dictionary = {"Key":"Value"}
#     value = a_dictionary["non_existent_key"]
#
# #Try to add a specific type of error to look for, otherwise, if there
# #is more than one kind of error, the second error will get ignored.
# except FileNotFoundError:
#     #Create file if it does not exist
#     file = open('a_file.txt', 'w')
#     file.write("Something")
#
# #'as error_message' Replaces the standard error message with your error message in the terminal.
# except KeyError as error_message:
#     print(f"That Key {error_message} doesn't exist.")
#
# else:
#     content = file.read()
#     print(content)
#
# #Not often used
# finally:
#     # file.close()
#     # print("File was closed.")
#     raise TypeError("It's broke!")

#-----'raise' Examples----------------------------------------------------
# height = float(input("Height: ")) #(In meters)
# weight = int(input("Weight: ")) # (In kilograms)
#
# if height > 3:
#     raise ValueError("Human height should not be greater than 3 meters.")
#
# bmi = weight / (height ** 2)









