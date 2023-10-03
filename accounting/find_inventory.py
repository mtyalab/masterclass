def find_inventory(cost_of_goods: float, ending_inventory: float, purchases: float) -> float:
    """
     Finds the beginning inventory
    :param cost_of_goods: The cost of the goods
           in the inventory
    :param ending_inventory: The amount of the goods
           in the inventory
    :param purchases: The amount of the purchases
           in the inventory
    :return:
    """
    return (cost_of_goods + ending_inventory) - purchases
