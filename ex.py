class Expense:
    def __init__(self, name: str, category: str, amount: float):
        self.name = name
        self.category = category
        self.amount = amount
    
    def __str__(self):
        return f"{self.name}, {self.category}, {self.amount}"

    def __repr__(self) -> str:
        return f"Expense:{self.name},{self.amount:.2f},{self.category}"
    