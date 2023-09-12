class Offer:
    def __init__(self, offer_price, valid_until):
        # private
        self.__offer_price = offer_price
        self.__valid_until = valid_until

    # setters & getters
    @property
    def offer_price(self):
        return self.__offer_price

    @offer_price.setter
    def offer_price(self, offer_price):
        self.__offer_price = offer_price

    @property
    def valid_until(self):
        return self.__valid_until

    @valid_until.setter
    def valid_until(self, valid_until):
        self.__valid_until = valid_until

    @classmethod
    def create_new_offer(cls, offer_price, valid_until):
        return cls(offer_price, valid_until)

    def __str__(self):
        return f"Offer Price: {self.offer_price}\nValid Until: {self.valid_until}\n"
