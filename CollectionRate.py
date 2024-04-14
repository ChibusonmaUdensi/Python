def CollectionRate():
	number = int(input("Number of successful delivery: "))



if number < 50:
	result = (number * 160) + 5000
	return result

elif  50 <= number <= 59:
	result = (number * 200) + 5000
	return result

elif 60 <= number <=69:
	result = (number * 250) + 5000
	return result

elif number >= 70:
	result = (number * 500) + 5000
	return result


print(CollectionRate())