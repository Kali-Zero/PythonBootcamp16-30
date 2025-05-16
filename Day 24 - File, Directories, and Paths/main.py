# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

#This is better, because you don't have to remember to close the file
#when you are done with it. (Opens it in 'READ ONLY' mode)
# with open("my_file.txt", mode="r") as file:
#     contents = file.read()
#     print(contents)

#Opens the file in 'write mode' as indicated by 'mode="w"' - replaces EVERYTHING in the file.
#If file does not exist, it will create it.
# with open("my_NEW_file.txt", mode="w") as file:
#     file.write("Hello File!\nThis is definitely a file!")

#Opens the file in 'append mode'
# with open("my_file.txt", mode="a") as file:
#     file.write("\nThis is new text!")

#Absolute path (relative to root):
#Always use FORWARD slash, to avoid stupid errors
# with open("/Users/Kali/Desktop/desktop.txt", mode="r") as file:
#     contents = file.read()
#     print(contents)

#Relative path (relative to current working directory):
#Start in "Day 24 - File, Directories, and Paths" - BEGIN HERE-> "PythonBootcamp16-100"/PycharmProjects/Kali
#then follow back down with /Desktop/desktop.txt"
with open("../../../Desktop/desktop.txt", mode="r") as file:
    contents = file.read()
    print(contents)

#C:\Users\Kali\PycharmProjects\PythonBootcamp16-100\Day 24 - File, Directories, and Paths
