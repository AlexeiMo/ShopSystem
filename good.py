class Good(object):

    def __init__(self, name="undefined", price=0.0, category="food"):
        self._name = name
        self._price = price
        self._category = category

    def _get_name(self) -> str:
        return self._name

    def _get_price(self) -> float:
        return self._price

    def _get_category(self) -> str:
        return self._category

    def _set_name(self, name: str) -> None:
        self._name = name

    def _set_price(self, price: float) -> None:
        if price >= 0:
            self._price = price
        else:
            self._price = 0

    def _set_category(self, category: str) -> None:
        self._category = category

    name = property(fget=_get_name, fset=_set_name)
    price = property(fget=_get_price, fset=_set_price)
    category = property(fget=_get_category, fset=_set_category)

    def __str__(self):
        return "Name: {0.name}, Price: {0.price}, Category: {0.category}".format(self)
