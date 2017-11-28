colors = ['black', 'white']
sizes  = ['S', 'M', 'L']
#  listcomp: generate list of types arranged by color & size
tshirts = [(color, size) for color in colors 
                         for size in sizes]
print('tshirts:', tshirts)
#  listcomp: rearranged as for loops
for color in colors:
  for size in sizes:
    print((color, size))
#  listcomp: generate list of types arranged by size & color
tshirts = [(size, color) for size in sizes 
                         for color in colors]

print('tshirts:', tshirts)