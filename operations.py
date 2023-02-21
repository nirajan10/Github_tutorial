def find_common(list1, list2):
	common = []
	for i in list1:
		if i in list2:
			common.append(i)
	return common

