numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

MISSED_ELEM_INDEX = 4
part_of_numbers = numbers[:MISSED_ELEM_INDEX] + numbers[MISSED_ELEM_INDEX+1:]
numbers[MISSED_ELEM_INDEX] = sum(part_of_numbers) / len(numbers)
print("Измененный список:", numbers)
