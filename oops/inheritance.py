from classes import Vehicle     # we will inherit this class

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
        self._charge_level = min(100, self._charge_level + amount)
        return f"Charged! Battery level: {self._charge_level}%"
    
    @property
    def charge_level(self):
        return self._charge_level