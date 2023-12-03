# program to sort and find median of numbers

# sortAndFindMedian: function that calls sort function and calculates median 
def sortAndFindMedian(numbers):
    # sortedNumbers: calls insertionSort function and stores sorted numbers
    sortedNumbers = insertionSort(numbers)
    print('sorted numbers', sortedNumbers)

    # n: stores length of sorted numbers
    n = len(sortedNumbers)

    # if n is even returns average of numbers else returns number
    if n%2 == 0:
        return (sortedNumbers[(n//2) - 1] + sortedNumbers[n//2])/2
    else:
        return sortedNumbers[n//2]

# insertionSort: function that sorts given numbers
def insertionSort(numbers):
    for i in range(1, len(numbers)):

        p = numbers[i]

        j = i-1

        while j >= 0 and p < numbers[j]:
            numbers[j+1] = numbers[j]
            j = j-1

        numbers[j + 1] = p

    return numbers

# Enter coma separated values as input
numbers = input("Enter list of numbers ")

# Converts numbers to List
numbers = list(numbers.split(','))
# Converts numbers in list from string to integer
numbers = [int(x) for x in numbers]


print(sortAndFindMedian(numbers))
