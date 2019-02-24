def chooseMedian(numbers):
    numbers = sorted(numbers)
    print(numbers)
    lengthNum = len(numbers)
    if lengthNum % 2 == 0:
        median = (numbers[int(lengthNum / 2)] + numbers[int(lengthNum / 2 - 1)]) / 2.0
    else:
        median = numbers[int(lengthNum / 2)]
    return median

    
print(chooseMedian([1, 2, 3, 8, 5, 2, 6, 5, 9, 4, 1, 2]))


def count_median(numbers):
    numbers = sorted(numbers)
    print(numbers)
    if len(numbers) % 2 == 0:
        print((numbers[int((len(numbers) / 2) - 1)]) + (numbers[int(len(numbers) / 2)]))
    else:
        print(numbers[int(len(numbers) // 2)])

count_median([1, 2, 3, 5, 7, 4, 3, 1, 4])









































    
  
