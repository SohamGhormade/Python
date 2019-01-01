d = {'cat':'cute','dog':'furry'}# use curly brackets for declaring dictionaries
print(d['cat']) # access value for dictionary
print('cat' in d) # checks if key is present in dictionary
d['fish'] = 'wet' # set value
print(d['fish'])# prints 'wet'
print(d.get('monkey', 'N/A'))# get key with default
del d['fish'] # remove key from dictionary
print(d.get('fish', 'N/A'))# prints 'N/A'
d = {'person':2,'cat':4, 'spider':8}
for animal in d:
    legs = d[animal]
    print('A %s has %d legs' %(animal, legs))

for animal, legs in d.items():    # access to keys AND values
  print('A %s has %d legs ' %(animal, legs))

nums = [0,1,2,3,4]
even_num_to_square = {x:x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square)