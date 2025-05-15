class Animal: #'Super' class

    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):   #The Fish class inherits from the superclass 'Animal'
    def __init__(self):
        super().__init__() #Calls and initializes the superclass

    def breathe(self):
        #Creating this class, even though its in the super 'Animal' class,
        # allows me to edit it, without changing it in the super class
        # ie the changes only apply to this class.
        super().breathe() #Copies the function from the one in the super class
        print("...doing this underwater.")


    def swim(self):
        print("Swimming.")

nemo = Fish()
nemo.swim()

#The 'breathe' function is in the animal class, but because I inherited it
# through the Fish class, I can use it as if it were in the Fish class
nemo.breathe()