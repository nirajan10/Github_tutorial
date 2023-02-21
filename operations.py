def find_common(list1, list2):
	common = []
	for i in list1:
		if i in list2:
			common.append(i)
	return common

def find_disjoint(list1, list2):
	disjoint = []
	for i in list2:
		if i not in list2:
			disjoint.append(i)
	return disjoint

def nothing():
	pass

