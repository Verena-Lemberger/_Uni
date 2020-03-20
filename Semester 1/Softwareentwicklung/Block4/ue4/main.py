class Currency():
    def __init__(self, value, symbol="EUR", rate=1):
        self.value = value
        self.symbol = symbol
        self.rate = rate
        self.currentValue = value * rate

    def __str__(self):
        return "{:.2f} {}".format(self.currentValue, self.symbol)

    def __add__(self, other):
        if not isinstance(other, Currency):
            other = Currency(other)
        return Currency(self.currentValue + other.currentValue)

    def __sub__(self, other):        
        if not isinstance(other, Currency):
            other = Currency(other)
        return Currency(self.currentValue - other.currentValue)


usd1 = Currency(15, "USD", 0.89)
eur1 = Currency(15)

print(eur1 + 5 + usd1)
