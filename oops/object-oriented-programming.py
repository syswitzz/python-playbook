# ============================================
# PYTHON CLASSES - INTERMEDIATE & ADVANCED CONCEPTS
# ============================================

class Vehicle:
    """
    A comprehensive class demonstrating Python OOP concepts
    """
    
    # Class variable - shared across all instances
    total_vehicles = 0
    
    def __init__(self, brand, model, year):
        """
        Constructor - initializes instance variables
        
        Args:
            brand (str): Vehicle brand name
            model (str): Vehicle model
            year (int): Manufacturing year
        """
        # Instance variables - unique to each object
        self.brand = brand
        self.model = model
        self.year = year
        
        # Protected attribute (convention: single underscore)
        self._mileage = 0
        
        # Private attribute (name mangling: double underscore)
        self.__engine_code = "DEFAULT123"
        
        Vehicle.total_vehicles += 1
    
    # Regular instance method - requires self
    def drive(self, distance):
        """Add distance to mileage"""
        self._mileage += distance
        return f"Drove {distance} km. Total mileage: {self._mileage}"
    
    # Property decorator - getter for encapsulation
    @property
    def mileage(self):
        """Get mileage (read-only access to protected attribute)"""
        return self._mileage
    
    # Property setter - controlled modification
    @mileage.setter
    def mileage(self, value):
        """Set mileage with validation"""
        if value < 0:
            raise ValueError("Mileage cannot be negative")
        self._mileage = value
    
    # Class method - works with class, not instance
    @classmethod
    def from_string(cls, vehicle_string):
        """
        Alternative constructor - creates instance from string
        
        Args:
            vehicle_string (str): Format "Brand-Model-Year"
        
        Returns:
            Vehicle: New vehicle instance
        """
        brand, model, year = vehicle_string.split('-')
        return cls(brand, model, int(year))
    
    @classmethod
    def get_total_vehicles(cls):
        """Return total number of vehicles created"""
        return cls.total_vehicles
    
    # Static method - doesn't need class or instance
    @staticmethod
    def is_vintage(year):
        """Check if vehicle is vintage (25+ years old)"""
        from datetime import datetime
        current_year = datetime.now().year
        return current_year - year >= 25
    
    # Special method for string representation
    def __str__(self):
        """User-friendly string representation"""
        return f"{self.year} {self.brand} {self.model}"
    
    # Special method for developer representation
    def __repr__(self):
        """Detailed representation for debugging"""
        return f"Vehicle('{self.brand}', '{self.model}', {self.year})"
    
    # Operator overloading - comparing vehicles by year
    def __lt__(self, other):
        """Less than comparison based on year"""
        return self.year < other.year
    
    def __eq__(self, other):
        """Equality comparison"""
        return (self.brand == other.brand and 
                self.model == other.model and 
                self.year == other.year)


# ============================================
# INHERITANCE & POLYMORPHISM
# ============================================

class ElectricVehicle(Vehicle):
    """
    Child class demonstrating inheritance and polymorphism
    """
    
    def __init__(self, brand, model, year, battery_capacity):
        """
        Initialize electric vehicle with additional attributes
        
        Args:
            battery_capacity (int): Battery capacity in kWh
        """
        # Call parent constructor
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity
        self._charge_level = 100
    
    # Method overriding - polymorphism
    def drive(self, distance):
        """
        Override parent drive method with battery consumption
        """
        battery_used = distance * 0.2  # 0.2 kWh per km
        if self._charge_level - battery_used < 0:
            return "Insufficient battery!"
        
        self._charge_level -= battery_used
        self._mileage += distance
        return f"Drove {distance} km. Battery: {self._charge_level:.1f}%"
    
    def charge(self, amount):
        """Charge the battery"""
        self._charge_level = min(100, self._charge_level + amount)
        return f"Charged! Battery level: {self._charge_level}%"
    
    @property
    def charge_level(self):
        """Get current charge level"""
        return self._charge_level


# ============================================
# USAGE EXAMPLES
# ============================================

# Creating instances
car1 = Vehicle("Toyota", "Camry", 2020)
car2 = Vehicle.from_string("Honda-Civic-2018")  # Using classmethod

# Using properties
print(car1.mileage)  # 0 (using getter)
car1.drive(100)      # Updates internal _mileage
print(car1.mileage)  # 100

# Using static method
print(Vehicle.is_vintage(1990))  # True
print(Vehicle.is_vintage(2020))  # False

# Class variables
print(Vehicle.get_total_vehicles())  # 2

# Inheritance and polymorphism
ev = ElectricVehicle("Tesla", "Model 3", 2023, 75)
print(ev.drive(50))   # Uses overridden method
print(ev.charge(20))  # Uses new method

# Operator overloading
print(car2 < car1)    # True (2018 < 2020)
print(car1 == car2)   # False

# String representations
print(str(car1))      # "2020 Toyota Camry"
print(repr(car1))     # "Vehicle('Toyota', 'Camry', 2020)"
