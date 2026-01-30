# item_amount= 12
# print(f"Initial Item Amount: {item_amount}")
# print(f"Initial Item id: {id(item_amount)}")

# item_amount=15
# print(f"Second Item Amount: {item_amount}")
# print(f"Second Item id: {id(item_amount)}")



# immutable
shop_item_names=set()
shop_item_names.add("Apple Juice")
print(f"Shop Items: {shop_item_names}")
print(f"Shop Items id: {id(shop_item_names)}")

shop_item_names.add('Banana Juice')
print(f"Shop Items second time: {shop_item_names}")
print(f"Shop Items id second time: {id(shop_item_names)}")