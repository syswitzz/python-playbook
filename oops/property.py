# @property - It is used to define a method as a property, 
# Properties are a special kind of attribute
# that provides a controlled way to access, set, and delete attribute values. 
# Properties allow you to add logic (like validation or computation) when an attribute is accessed or modified, 
# while still allowing it to be accessed like a regular attribute.
# it is useful to create read only, write only, custom behaviour to gate the access to the private attribute


class Circle:
    def __init__(self, radius):
        self._radius = radius

    # getter - gets the value of the property
    @property
    def radius(self):
        '''get the radius of the circle'''
        return self._radius
    
    #setter - sets the value of the property
    @radius.setter
    def radius(self, value):
        '''sets the value of radius. must be +ve'''
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be postiive.")
    
    @radius.deleter
    def radius(self):
        del self._radius


circle = Circle(5)
circle.radius()  # is wrong now since its a property
circle.radius  # gives the radius
circle.radius = 4 #  sets the radius
del circle.radius  # deletes the property