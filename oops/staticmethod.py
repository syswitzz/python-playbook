# @staticmethod - It is used to define a method that doesn't operate on an instance of class'
# (i.e., it doesn't use self). 
# Static methods are called on class itself, not on an instance of class.


class Math:
    @staticmethod
    def add(x, y):
        return x+y
    @staticmethod 
    def multiply(x, y):
        return x*y
    
instance = Math()
Math.add(5, 7)  # 12, note that we didnt make the instance of the class
instance.add(5, 7)   # 12, although it works this way too
