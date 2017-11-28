
# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to 
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
  # Returned string pair should be ordered by dictionary order
  # I.e., if the highest affinity pair is "foo" and "bar"
  # return ("bar", "foo"). 

  dic = {}
  siteSet = set()
  for i in site_list:
  	siteSet.add(i)
  for i in siteSet:
  	dic[i] = []
  for i in range(len(site_list)):
  	dic[site_list[i]].append(user_list[i])
  max = 0
  keyList = list(dic.keys())
  for i in range(len(keyList)):
  	for j in range(i + 1, len(keyList)):
  		if common_number(dic[keyList[i]], dic[keyList[j]]) > max:
  			max = common_number(dic[keyList[i]], dic[keyList[j]])
  			result = (keyList[i], keyList[j])
  if result[0] < result[1]:
  	return result
  else:
  	return (result[1], result[0])


def common_number(list1, list2):
	counter = 0;
	for i in list1:
		for j in list2:
			if i == j:
				counter += 1
	return counter

##########useless#####################

def dont(n):
  counter = 0
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1

def mess(n):
  counter = 0
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1

def withh(n):
  counter = 0
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1

def me(n):
  counter = 0
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1

def seriously(n):
  counter = 0
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1

def cus(n):
  counter = 0
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1

def you(n):
  counter = 0
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1

def cant(n):
  counter = 0
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1
  for i in range(n):
    counter = counter + 1

