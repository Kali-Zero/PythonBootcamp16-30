piano_keys = ["a","b","c","d","e","f","g"]

print(piano_keys[2:5]) #Grabs 'c','d','e'

print(piano_keys[2:]) #Grabs everything after 'b'

print(piano_keys[:5]) #Grabs everything before 'f'

print(piano_keys[2:5:2]) #The third number is the 'step' So it would grab 'c', then skip two to 'e' and grab that

print(piano_keys[::2]) #Grab every other letter, starting at 'a'.

print(piano_keys[::-1]) #Grabs every letter in reverse order.

#All these work on tuples too.