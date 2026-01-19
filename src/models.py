from typing import List, Optional, Dict

class Product:
    ALLOWED_CONDITIONS: List[str] = ["Loose", "CIB", "New/Sealed"]
    def __init__(self, sku, title: str, platform: str, condition: str, price: float, quantity: int, ) -> None:
        
        formated_condition = condition.strip().title()

        if formated_condition not in self.ALLOWED_CONDITIONS:
            raise ValueError(f"Invalid condition. Must be one of: {self.ALLOWED_CONDITIONS}")
        
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.sku = sku.upper()
        self.title = title
        self.platform = platform
        self.condition = formated_condition
        self.price = price
        self.quantity = quantity


    def add_stock(self, count: int):
        if count < 0:
            raise ValueError("Please enter a value greater than zero")
        self.quantity += count
    
    def romove_stock(self,count: int):
        if count < 0:
            raise ValueError("Please enter a value greater than zero")
        self.quantity -= count

    def update_price(self, new_price: float) -> None:
        if new_price < 0:
            raise ValueError("Price cannot be less than zero")
        self.price = new_price

    def get_total_value(self):
        pass
    

    