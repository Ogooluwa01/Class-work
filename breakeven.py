import math
cost_to_produce_each_item = 20.00
sale_price_per_item = 40.00 #(item cost + profit per item)
fixed_costs = 50000.00

breakeven = fixed_costs/sale_price_per_item
profit = sale_price_per_item-cost_to_produce_each_item

print("cost to produce each item:", cost_to_produce_each_item)
print("sale price per item:", sale_price_per_item )
print("fixed costs:", fixed_costs )
print("profit:", profit)
print("breakeven:", breakeven)