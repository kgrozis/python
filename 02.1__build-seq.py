# python3

symbols = '$¢£¥€¤'

# build seq with iterator
codes = []
for symbol in symbols:
  codes.append(ord(symbol))
print('iterator: ', codes)

# build seq with listcomp
# line breaks are ignored inside pairs: [], {}, or ()
codes = [ord(symbol) for symbol in symbols]
print('listcomp: ', codes)

# listcomp have own local scop in python3
# won't clobber value, value of x is preserved
x = 'ABC'
dummy = [ord(x) for x in x]
print(x, dummy)

# listcomp
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print('listcomp:', beyond_ascii)
# lambda + map functions = additional complexity with less readibility 
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print('lambda:', beyond_ascii)