from shop import Shop
from json_utils import JsonUtils


if __name__ == "__main__":

    utils = JsonUtils()

    # read json objects from "test_goods.json"
    goods_to_store = utils.read_json("test_goods.json")

    keys = list(goods_to_store.keys())

    shop = Shop()

    # add goods that we've read to shop
    for key in keys:
        shop.add_good(goods_to_store[key])

    # get json objects of shop goods from each existing category
    food_json_obj = shop.get_goods("Food")
    tools_json_obj = shop.get_goods("Tools")
    electronics_json_obj = shop.get_goods("Electronics")
    books_json_obj = shop.get_goods("Books")

    # print jsons of goods
    print("Food goods: ")
    for json in food_json_obj:
        print(json)
    print("*" * 80)

    print("Tools goods: ")
    for json in tools_json_obj:
        print(json)
    print("*" * 80)

    print("Electronics goods: ")
    for json in electronics_json_obj:
        print(json)
    print("*" * 80)

    print("Books goods: ")
    for json in books_json_obj:
        print(json)
    print("*" * 80)

    # clear goods in Food category
    shop.clear_goods("Food")
    food_json_obj = shop.get_goods("Food")

    # print jsons of goods
    print("Food goods: ")
    for json in food_json_obj:
        print(json)
    print("*" * 80)
