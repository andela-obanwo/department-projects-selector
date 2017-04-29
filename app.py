import random
import names
import itertools

print (names.get_first_name())

data = dict([('marketing',[5, 3]),('sales',[5, 3]), ('accounting', [5, 3]), ('technology', [5, 3]), ('management', [5, 3])])
glimit = len(data)
# print (data)

expandeddata = {}

for k, v in data.items():
  # print (k, v)
  expandeddata[k] = {'data': {}, 'limit': v[1]}
  for number in range(v[0]):
    expandeddata[k]['data'][names.get_first_name()] = random.randrange(100, 1000, 100)
    
    
print (expandeddata)


def findsubsets(id, iterable, limit):
  sets = itertools.combinations(iterable, limit)
  tup = []
  for item in sets:
    tup.append([id, item])
    
  # print (tup)
  return tup
 


def possibilities(expandeddata):
  possibilities = []
  for dept, deptdata in expandeddata.items():
    possibilities.append((findsubsets(dept, deptdata['data'], deptdata['limit'])))
  # return possibilities
  return [users for dept in possibilities for users in dept]
  # return [item for item in possibilities for i in item]


# print (itertools.chain(possibilities(expandeddata)))
def merged_possibilities(possibilities):
  limit = glimit
  possibilities = itertools.chain(possibilities)
  return (findsubsets('GROUP', possibilities, limit ))

# raw_data = merged_possibilities(possibilities(expandeddata))

# for item in itertools.chain(raw_data):
#   print (item)

groups = merged_possibilities(possibilities(expandeddata))

for group in groups:
  if sum([expandeddata[grp[0]]['data'][name] for grp in group[1] for name in grp[1]]) <=4000:
    print (group)
