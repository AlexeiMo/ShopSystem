from good import Good


class Parser(object):

    def parse_to_good(self, obj):
        pass


class JSONParser(Parser):

    def parse_to_good(self, json_obj) -> Good:
        good = Good()
        good.name = json_obj["name"]
        good.price = json_obj["price"]
        good.category = json_obj["category"]
        return good

    def parse_to_json(self, obj: Good):
        json_obj = {"name": obj.name, "price": obj.price, "category": obj.category}
        return json_obj
