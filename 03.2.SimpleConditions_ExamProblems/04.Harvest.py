import math

vineyard_area = int(input())
grape_per_square = float(input())
required_wine = int(input())
workers = int(input())
usage = 0.4
grape_for_liter = 2.5

produced_wine = vineyard_area * usage * grape_per_square / 2.5
net_wine = abs(required_wine - produced_wine)

print('It will be a tough winter! More {0} liters wine needed.'.format(math.floor(net_wine))
      if produced_wine < required_wine
      else 'Good harvest this year! Total wine: {0} liters.\n{1} liters left -> {2} liters per person.'
      .format(math.floor(produced_wine), math.ceil(net_wine), math.ceil(net_wine / workers)))
