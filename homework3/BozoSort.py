# Help taken from Java implementation of Bozo-Sort: 
# http://www.dreamincode.net
# /forums/blog/114/entry-595-bozosort-definitive-c-c%23-vbnet-java-php/

import random

def BozoSort(array):
	while (not is_sorted(array)):
		index1 = random.randint(0, len(array) - 1)
		index2 = random.randint(0, len(array) - 1)

		array[index1], array[index2] = array[index2], array[index1]
	return array;

def is_sorted(array):
	for i in range(0, len(array) - 1):
		if (array[i] > array[i + 1]):
			return False
	return True