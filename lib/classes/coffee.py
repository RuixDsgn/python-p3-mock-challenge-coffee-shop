class Coffee:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, "name"):
            raise Exception()
        else:
            self._name = name
        
    def orders(self, new_order=None):
        from classes.order import Order
        return [order for order in Order.all if self == order.coffee]
    
    def customers(self, new_customer=None):
        customer_list = [order.customer for order in self.orders()]
        return [*set(customer_list)]
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        prices = [order.price for order in self.orders()]
        return sum(prices) /len(prices)