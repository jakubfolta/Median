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

def countMedian(numbers):
    numbers = sorted(numbers)
    print(len(numbers))
    print(numbers[len(numbers) / 2 - 1])
    if len(numbers) % 2 == 0:
        print('Median from this list is a ') + str(((numbers[len(numbers) / 2 - 1]) + (numbers[len(numbers) / 2])) / 2)


countMedian([1, 2, 3, 5, 7, 4, 3, 4])









































    
  
