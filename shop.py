from good import Good
from categories import Category, Food, Tools, Electronics, Books
from json_parser import Parser, JSONParser


class Shop(object):

    def __init__(self, categories=None, parser=None):
        if categories is None:
            self._categories = {"Food": Food(),
                                "Tools": Tools(),
                                "Electronics": Electronics(),
                                "Books": Books()
                                }
        else:
            self._categories = categories
        self._parser = JSONParser() if parser is None else parser

    def add_category(self, cat_name: str) -> None:
        if cat_name not in self.categories.keys():
            self.categories[cat_name] = Category(cat_name)

    def add_good(self, json_file) -> None:
        new_good = self.parser.parse_to_good(json_file)

        if new_good.category not in self.categories.keys():
            self.add_category(new_good.category)

        self.categories[new_good.category].add_good(new_good)

    def clear_goods(self, cat_name: str) -> None:
        if cat_name in self.categories.keys():
            self.categories[cat_name].clear_goods()

    def get_goods(self, cat_name: str) -> list:
        json_obj = []
        if cat_name in self.categories.keys():
            for good in self.categories[cat_name].goods:
                json_obj.append(self.parse_to_json(good))
        return json_obj

    def parse_to_good(self, json_file) -> Good:
        return self.parser.parse_to_good(json_file)

    def parse_to_json(self, obj: Good):
        return self.parser.parse_to_json(obj)

    def _get_categories(self) -> dict:
        return self._categories

    def _get_parser(self) -> JSONParser:
        return self._parser

    def _set_categories(self, categories: dict) -> None:
        self._categories = list(categories)

    def _set_parser(self, parser: Parser) -> None:
        self._parser = parser

    categories = property(fget=_get_categories, fset=_set_categories)
    parser = property(fget=_get_parser, fset=_set_parser)
