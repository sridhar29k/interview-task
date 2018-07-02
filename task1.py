menu_items = {'Salad' :2.53,'Soup': 1.76,'RedCurry': 6.31,
          'Satay' :2.98,'FriedRice':7.07,'IcedTea':1.06 }

_target = 14.08

item_purchased = []
cost = 0
cntr = 0 
import itertools



for  item, prize in menu_items.items():
  item1 , p_menu = '' ,''
  while cost <= _target: 
    cost += prize
    item1 = item1 + '_' + item
    if cost <= _target:p_menu = item1
  item_purchased.append(p_menu)
  cost,item1 = 0,''

menu_costs = menu_items.keys()
for L in range(0, len(menu_costs)+1):
    for subset in itertools.combinations(menu_costs, L):
        if len(subset) <= 1:continue
        cost,item1 = 0, ''
        for i in subset:
            cost += menu_items[i]
            item1 = item1 + '_' + i
        if cost <= _target:
            item_purchased.append(item1)
item_purchased = [i.strip('_') for i in item_purchased]

print(item_purchased)
