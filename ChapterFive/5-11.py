nums = list(range(1,11))
print(nums)
for num in nums:
	num_to_string = str(num)

	if num == 1:
		print(num_to_string + 'st')
	elif num in [2, 3]:
		print(num_to_string + 'nd')
	else:
		print(num_to_string + 'th')