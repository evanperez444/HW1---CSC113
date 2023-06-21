#Evan Perez
#Assignment 2
#ID: 24212505

#1.a.
def greet(name):
    print("Hello " + name + "!")

#1.b.

def calculate_area(length, width):
    return length * width #multilplication

#1.c.

def is_even(number):
    #if the number is divisble by 2 without remainders, it is even, else it is not
    if number % 2 == 0:
        return True
    else:
        return False

def calculate_volume(length, width, height):
    #calcualte base area with calculate_area function
    base_area = calculate_area(length, width)

    return base_area * height

def factorial(n):
    if n == 1:
        return n
    else:
        return factorial(n-1) * n

def get_average(nums):
    #average = sum / number of elements
    #loop over elements and add each number to "sum", then divide by the length of the list "nums"
    #calculate the sum of
    sum = 0
    for n in nums:
        sum = sum + n
    return sum / len(nums)

def get_median(nums):

    #median is middle value
    #sort the list first
    nums.sort()

    #check if there are an odd number of elements, if so, middle value is length of list divided by 2 and rounded up
    #if there are an even number of elements, we have to find the two values in the middle of the list and find their average
    if len(nums) % 2 != 0:
        return nums[len(nums)//2]
    else:
        medHigh = nums[len(nums)//2] #right middle
        medLow = nums[(len(nums)//2) - 1 ] #left middle

        return get_average([medHigh, medLow])


#Test greet function
greet("Evan")

#Test calculate area function
print("Area: ")
print(calculate_area(5,3))

#Test is even function
print(is_even(10))
print(is_even(8))
print(is_even(5))
print(is_even(3))

#Test calculate volume
print("Volume: ")
print(calculate_volume(4,3,3))

#Test factorial function
print("Factorials of 4, 5, 7, and 10: ")
print(factorial(4))
print(factorial(5))
print(factorial(7))
print(factorial(10))


#Test get average function
print("Testing average function: ")
print(get_average([70, 80, 90]))

#Test median
print("Return median: ")
print(get_median([1,2,3,4]))
print(get_median([3,6,2,5,8]))


