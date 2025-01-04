#Python Challenges 
# (1) Reverse a String
def reverse_string(string):
    return string[::-1]

print(reverse_string("Hello")) 
#General slicing uses [:] but then [::] tells python to move backwards and reverses it

# (2) Count Vowels
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0 #We also initiate count when we are going to count things 
    for char in string: #This will go through each letter inputted in the string individually
        if char in vowels: #Checks if the character is a vowel 
            count += 1 #Keeps checking in increments, if one is a vowel it will add (1) to the count
    return count #Returns the total number of vowels 

print(count_vowels("Hello World!"))
#Outputs 3 vowels here 

# (3) Check for Palindrome
def palindrome(string):
    if string[::-1] == string:
        return True
    return False

print(palindrome("hello")) #Completed correct 

# (4) Find the Maximum Number in a List (did not complete myself - sadface)
def maximum_number(numbers):
    largest = numbers[0] #Initialises a variable to hold the largest numnber and we assume the first number is the largest
    for num in numbers: #Now we compare every number to the first one 
        if num > largest: #If num is larger then the current value 
            largest = num #The largest then becomes that num 
    return largest
    
print(maximum_number([3, 1, 4, 1, 5, 9]))

# (5) Find the Minimum Number
def minimum_number(numbers):
    smallest = numbers[0]
    for num in numbers: 
        if num < smallest:
            smallest = num 
    return smallest

print(minimum_number([3, 1, 4, 1, 5, 9]))

# (6) Count Occurrences of a Number in a List (Had help here)
def count(numbers, number):
    counter = 0
    for num in numbers: #Here we loop through all the numbers individually
        if num == number: #If then there is a num which = number then we count
            counter += 1
    return counter
print(count([1, 2, 3, 4, 1, 2, 1], 1))

# (7) Count Even numbers in a list
def count(numbers):
    counter = 0
    for num in numbers:
        if num % 2 == 0: #This checks for the even numbers: when dividing num by two giving the reminader of 0
            counter += 1
    return counter
print(count([1, 2, 3, 4, 5, 6]))
print(count([11, 13, 15, 16, 18]))

# (7) Find the sum of all Odd Numbers in a List
def odd_numbers(numbers):
    total = 0 #We start with everything being added up to 0
    for num in numbers:
        if num % 2 == 1:
            total += num #This basically is just total + num 
    return total
print(odd_numbers([1, 2, 3, 4, 5]))

# (8) Find the longest String in a List (Had help)
def longest(strings):
    longest_string = strings[0]
    for string in strings:
        if len(string) > len(longest_string): #we are comparing lengths!!
            longest_string = string #This makes the longest string = to the current string if we did += it would add the current string to the longest string
    return longest_string
print(longest(["apple", "banana", "cherry", "date"]))

# (9) Find the shortest string in a list 
def shortest(strings):
    shortest_string = strings[0]
    for string in strings:
        if len(string) < len(shortest_string):
            shortest_string = string
    return shortest_string
print(shortest(["apple", "banana", "cherry", "fig"]))

# (10) Find the second largest number in a List (completed fucked this one up)
def second_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num 

    second = float('-inf') #This is edge case handling: makes sure code works even in unusual cases 
    #This float thing is a negative infinity, it is a value smaller then any possible number 
    for num in numbers:
        if num == largest:
            continue #Skip the largest 
        if num > second:
            second = num 
    return second if second != float('inf') else None #Short hand if-else statement 

print(second_largest([10, 20, 4, 45, 99]))

# (11) Find all Even Numbers and their Sum (Had a bit of help)
def even_sum(numbers):
    #Find the even numbers first 
    even_numbers = []
    total = 0
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
            total += num
    return even_numbers, total
print(even_sum([1, 2, 3, 4, 5, 6]))

# (12) Find all the Odd Numbers and their Product
def odd_product(numbers):
    odd_numbers = []
    product = 1 #When it is multiplication you need to start with 1 as its neutral, if it is 0 it will always be 0
    for num in numbers: 
        if num % 2 != 0:
            odd_numbers.append(num)
            product *= num 
    return odd_numbers, product
print(odd_product([1, 2, 3, 4, 5, 6]))

# (13) Count and Sum Negative Numbers 
def count_sum(numbers):
    negative_numbers = []
    total = 0
    for num in numbers: 
        if num < 0:
            negative_numbers.append(num)
            total += num 
    return negative_numbers, total
print(count_sum([-1, -2, 3, 4, -5, 6]))

# (14) Negative and Positive (My own attempt)
def sep_count(numbers):
    count_neg = 0
    count_pos = 0
    positive_numbers = []
    negative_numbers = []
    for num in numbers: 
        if num < 0:
            negative_numbers.append(num)
            count_neg += 1
        else:
            positive_numbers.append(num)
            count_pos += 1
    return positive_numbers, negative_numbers, count_neg, count_pos
print(sep_count([-1, -2, 3, 4, -5, 6]))

    #To make the code cleaner 
def sep_count(numbers):
    positive_numbers = []  # List for positive numbers
    negative_numbers = []  # List for negative numbers

    for num in numbers:  # Loop through each number
        if num < 0:
            negative_numbers.append(num)  # Add to negatives
        else:
            positive_numbers.append(num)  # Add to positives

    return {
        "positive_numbers": positive_numbers,
        "negative_numbers": negative_numbers,
        "count": {"positives": len(positive_numbers), "negatives": len(negative_numbers)},
    }
print(sep_count([-1, -2, 3, 4, -5, 6]))

# (15) Find the longest word in a function 
def longest_string(sentence):
    strings = sentence.split()
    longest = strings[0]
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest, len(longest)
print(longest_string("The quick brown fox jumps over the lazy dog"))

#If we then wanted to have an output of all the max length words 
def longest_strings(strings):
    longest_words = []  # List to store words with the longest length
    max_length = 0  # Track the maximum length

    for string in strings:
        if len(string) > max_length:
            max_length = len(string)  # Update the max length
            longest_words = [string]  # Reset list with the new longest word
        elif len(string) == max_length:
            longest_words.append(string)  # Add word if it matches the max length

    return longest_words, max_length  # Return all longest words and their length

# (16) Sum Numbers in a List using for i in range()
#for i in range(start, stop, step)
def sum(numbers):
    total = 0 
    for i in range(len(numbers)):
        total += numbers[i] #Adds the element at index i to the total
    return total
        
print(sum([1, 2, 3, 4, 5]))

# (17) Reversing a list using indexes 
def reverse(lst):  # Avoid using 'list' as a variable name since it's a Python keyword
    reversed_list = []  # Create an empty list to store the reversed elements
    for i in range(len(lst) - 1, -1, -1):  # Loop through indices in reverse order
        reversed_list.append(lst[i])  # Add the element at index i to the new list
    return reversed_list  # Return the reversed list

print(reverse([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]

# (18) Remove all occurrences 
def removal(lst, number):
    new_list = [] #creates the new list 
    for i in range(len(lst)): #can access all the index using lst[i]
        if lst[i] != number: #if lst[i] is not equal to number 
            new_list.append(lst[i]) #then we add that to the new list 
    return new_list
print(removal([1, 2, 3, 2, 4, 2, 5], 2))

def removal(lst, number):
    new_list = []
    for num in lst:
        if num != number:
            new_list.append(num)
    return new_list
print(removal([1, 2, 3, 2, 4, 2, 5], 2))

# (19) Find the second smallest No. 
def second_small(numbers):
    # Find the smallest number
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    
    # Find the second smallest number
    second = float('inf')  # Start with the largest possible value
    for num in numbers:
        if num != smallest and num < second:  # Skip the smallest and check for smaller numbers
            second = num
    return second
print(second_small([3, 1, 4, 1, 5, 9]))  # Output: 3

# (20) Count consonants in a string 
def counting(string):
    count = 0
    vowels = "aeiou"
    for char in string:
        if char.isalpha() and char not in vowels: #For this we need to filter out non-alphabetic characters
            count += 1
    return count
print(counting("hello world"))

# (21) Reverse words in a sentence 
def reverse(string):
    reversed_words = []
    words = string.split() #Splits the words seperatly 
    for word in words:
        reversed_words.append(word[::-1]) #Reverses the words
        final_sentence = " ".join(reversed_words) #Join here adds a space between the words 
    return final_sentence
print(reverse("hello world"))

# (22) Find the most common character (New content)
def common_char(string):
    count = {}  # Initialize an empty dictionary to store character counts

    for char in string:  # Loop through each character in the string
        if char != " ":  # Skip spaces
            count[char] = count.get(char, 0) + 1  # Increment the count

    # Find the character with the highest frequency
    most_common = max(count, key=count.get)
    return most_common

# Test cases
print(common_char("hello world"))       # Output: "l"
print(common_char("aabbbccde"))         # Output: "b"
print(common_char("1122334455"))        # Output: "1"
print(common_char("Keep practicing!"))  # Output: "i"

# Using a shortcut in the same code 
def common_char(string):
    count = {}  # Initialize an empty dictionary to store character counts

    for char in string:  # Loop through each character in the string
        if char != " ":  # Skip spaces
            count[char] = count.get(char, 0) + 1  # Increment the count

    # Find the character with the highest frequency
    most_common = max(count, key=count.get)
    return most_common

# Test cases
print(common_char("hello world"))       # Output: "l"
print(common_char("aabbbccde"))         # Output: "b"
print(common_char("1122334455"))        # Output: "1"
print(common_char("Keep practicing!"))  # Output: "i"

#If i wanted to do this and print all the terms which are repeated an equal amount 
# 1. Find the max frequency 
# 2. Collect all the char 
# 3. Return the list 

 def common_char(string):
    count = {}  # Initialize an empty dictionary to store character counts
# For example it would look like this count = {'h': 1, 'e': 1, 'l': 2, 'o': 1}

    for char in string:  # Loop through each character in the string
        if char != " ":  # Skip spaces
            count[char] = count.get(char, 0) + 1  # Increment the count
            # count[char] updates the count dic for current char 
            # count.get(char, 0) checks if char is already in the dic, if it is it returns its current count, if it isnt then it returns 0 
            # .get() is used to get values from the dic 
            # +1 just adds 1 to the count for EACH char 
    # Find the maximum frequency
    max_freq = max(count.values())
    # count.values() just retrieves the values from the dic 
    # max() just finds the largest within the values 

    # Collect all characters with the maximum frequency
    most_common = [char for char, freq in count.items() if freq == max_freq]
    # This creates a list of the char where the frequencies match this is the == max_freq
    # count.items() returns the key value pairs from the dic 
    # (char, freq) this is list comprehension 
    return most_common

# Test cases
print(common_char("hello world"))       # Output: ['l']
print(common_char("aabbbccde"))         # Output: ['b']
print(common_char("1122334455"))        # Output: ['1', '2', '3', '4', '5']
print(common_char("Keep practicing!"))  # Output: ['e', 'i']







