# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: https://www.w3schools.com/python/ref_string_strip.asp

#Open the starting letter
with open("Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_contents = letter_file.read()

#Open invited_names
with open("Input/Names/invited_names.txt", mode="r") as name_file:
    invited_names = name_file.read()

#Parse the invited names into a list.
invite_list = invited_names.splitlines()

#For each name in the list, create a letter from the starting letter, and save it in 'Ready to Send'
for name in range (len(invite_list)):
    new_letter = letter_contents.replace("[name]", invite_list[name])
    with open(f"Output/ReadyToSend/letter_for_{invite_list[name]}.txt", mode="w") as file:
        file.write(new_letter)
