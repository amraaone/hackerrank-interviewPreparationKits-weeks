## Time Conversion Problem 

In Python package datetime import. 


## Counting Occurrences in a Python List - Sparse Array Problem

In Python, you can use the `count()` method to count the number of occurrences of a specific element within a list. Here's an example:

```python
arr = ['a', 'b', 'c', 'd']
count_of_b = arr.count('b')
print(count_of_b)  # This will output 1, as 'b' appears once in the list 'arr'.

## Lonely Integer - Explanation

use the XOR operation, each element of array 

```python

unique = 0 #initialize
for num in arr:
	unique ^= num
return unique

## Flipping Bits Problem
```python

def flippingBits(n):
    # Create a binary string with leading zeros and flip the bits
    flipped_string = ''.join(['1' if bit == '0' else '0' for bit in f"{n:032b}"])

    # Convert the flipped binary string to an integer
    flipped_value = int(flipped_string, 2)

    return flipped_value

first create n integer number convert to string then integer array
after that flip 0 -> 1 & 1 -> 0 map, convert to 2byte integer

## Counting sort 
The countingSort function counts how many times each integer appears in the given array.

arr = [1,4,3,666,3,2,1] 
output is: result = [1,0,1,0,1,0,1] etc.
