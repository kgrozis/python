#  python3 required
#  Similiar to listcomps
#  Build tuples
import array

symbols = '$¢£¥€¤'
#  if a simple expression you do not need parenthesis 
print(tuple(ord(symbol) for symbol in symbols))
#  array takes 2 args and is a complex expression so parenthesis are required
print(array.array('I', (ord(symbol) for symbol in symbols)))

colors = ['black', 'white']
sizes  = ['S', 'M', 'L']
#  uses generator but does not create a list
for tshirt in ('%s %s' % (c,s) for c in colors for s in sizes):
  print(tshirt)