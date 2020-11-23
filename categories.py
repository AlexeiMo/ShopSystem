from good import Good


class Category(object):

    def __init__(self, name, goods=None):
        self._name = name
        if goods is None:
            self._goods = []
        else:
            self._goods = goods

    def add_good(self, good: Good) -> None:
        if good not in self._goods:
            self._goods.append(good)

    def clear_goods(self) -> None:
        if len(self._goods) != 0:
            self._goods.clear()

    def _get_name(self) -> str:
        return self._name

    def _get_goods(self) -> list:
        return self._goods

    def _set_name(self, name: str) -> None:
        self._name = name

    def _set_goods(self, goods: list) -> None:
        self._goods = goods

    name = property(fget=_get_name, fset=_set_name)
    goods = property(fget=_get_goods, fset=_set_goods)

    def __str__(self):
        result = "Name: {0.name}, Goods List: ".format(self)
        result += " ".join(good.name for good in self.goods)
        return result


class Food(Category):

    def __init__(self, goods=None):
        super().__init__("Food", goods)


class Tools(Category):

    def __init__(self, goods=None):
        super().__init__("Tools", goods)


class Electronics(Category):

    def __init__(self, goods=None):
        super().__init__("Electronics", goods)


class Books(Category):

    def __init__(self, goods=None):
        super().__init__("Books", goods)
