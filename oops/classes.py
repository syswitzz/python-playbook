# Attributes  - are variables that store data associated with an object. 
# Methods - are functions defined within a class.

class Vehicle:
    total_vehicles = 0  # Class variable - shared across all instances
    
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
        
        # Protected attribute
        self._mileage = 0
        
        # Private attribute
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



