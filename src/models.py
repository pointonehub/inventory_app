from typing import List, Optional, Dict

class Product:
    ALLOWED_CONDITIONS: List[str] = ["Loose", "CIB", "New/Sealed"]
    def __init__(self, sku, title: str, platform: str, condition: str, price: float, quantity: int) -> None:
        
        formated_condition = condition.strip().title()

        if formated_condition no in self.ALLOWED_CONDITIONS:
            raise ValueError(f"Invalid condition. Must be one of: {self.ALLOWED_CONDITIONS}")
        
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.sku = sku.upper()
        self.title = title
        self.platform = platform
        self.condition = formated_condition
        self.price = price
        self.quantity = quantity


    def add_stock(count):
        pass
    
    def romove_stock(count):
        pass

    def update_price(new_price):
        pass

    def get_total_value():
        pass
    