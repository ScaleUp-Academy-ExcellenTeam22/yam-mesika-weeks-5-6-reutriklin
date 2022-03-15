def get_recipe_price(prices,optionals=None,**ingredients):
  pricesCopy=copy.deepcopy(prices)
  if optionals:
    for optional in optionals:
      pricesCopy.pop(optional)
  sum=0
  for ingredient, amount in ingredients.items():
    sum+=prices[ingredient]*amount/100
  print( sum)
  return sum