# @classmethod - It is used to define a method that operates on class itself (i.e., it uses cls). 
# Class methods can access and modify class state that applies across all instances of class.
# we dont get the instance of the class but the class itself which allows to access class attributes or staticmethods

class Person:
    species = "Homo Sapiens"

    @classmethod
    def get_species(cls):
        return cls.species
    

Person.get_species()    # Homo Sapiens