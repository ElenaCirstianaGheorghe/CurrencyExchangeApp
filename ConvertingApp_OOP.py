from ConvertingApp_scraping import exchange_dict

class Ccy:

    _currencies = exchange_dict

    __slots__ = ['currency', 'value']

    def __init__(self,  currency, value):
        self.currency = currency
        self.value = value

    def Converting_Currency(self, new_unit):
        """ It converts the value submitted by the user from the initial
        currency to the new one."""
        
        self.value = (self.value * Ccy._currencies[self.currency]) / Ccy._currencies[new_unit]
        self.currency = new_unit

