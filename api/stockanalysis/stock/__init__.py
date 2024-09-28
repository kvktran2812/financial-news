# TODO: implement Stock class


BASE_URL = "https://stockanalysis.com/stocks/"

class Stock:
    def __init__(self, stock: str):
        self.stock = stock

    def __str__(self):
        return self.stock