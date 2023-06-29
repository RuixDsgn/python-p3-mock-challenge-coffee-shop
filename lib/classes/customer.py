class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if (type(name) == str) and (1 <= len(name) <= 15):
            self._name = name
        else:
            raise Exception()

    def orders(self, new_order=None):
        from classes.order import Order
        return [order for order in Order.all if self == order.customer]
    
    def coffees(self, new_coffee=None):
        coffee_list = [order.coffee for order in self.orders()]
        return [*set(coffee_list)]
    
    