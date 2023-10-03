travel_mode = {"1": "car", "2": "plane"}

items = {
    "can opener",
    "fuel",
    "jumper",
    "knife",
    "matches",
    "matches",
    "razor blades",
    "razor",
    "scissors",
    "shampoo",
    "shaving cream",
    "shirts (3)",
    "shorts",
    "sleeping bag(s)",
    "soap",
    "socks (3 pairs)",
    "stove",
    "tent",
    "mug",
    "toothbrush",
    "toothpaste",
    "towel",
    "underwear (3 pairs)",
    "water carrier"
 }

restricted_items = {
    "catapult",
    "fuel",
    "gun",
    "knife",
    "razor blades",
    "scissors",
    "shampoo"
}

print("Please choose your mode of travel")
for key, value in travel_mode.items():
    print(f"{key}: {value}")
    # Python 3.5 and earlier
    # print("{}: {}".format(key, value))

mode = "-"
while mode not in travel_mode:
    mode = input("> ")

if mode == "2":
    # travelling by plane, remove restricted items
    # for restricted_items in restricted_items:
    #     # remove throws an error when you remove an item that doesn't exist
    #     items.discard(restricted_items)
    # items -= restricted_items
    items.difference_update(restricted_items)

# print the packing list
print("You need to pack:")
for item in sorted(items):
    print(item)