"""34: Write a Python program to count the number 4 in a given list
"""
def list_count_4(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1
    return count

print(list_count_4([1, 4, 6, 7, 4]))

print(list_count_4([1, 4, 6, 4, 7, 4]))

"""35:Write a Python program to test whether a passed letter is a vowel or not.
"""
def is_vowel(char):
    vowels = 'aeiou'
    return char in vowels

print(is_vowel("c"))
print(is_vowel("a"))
print(is_vowel("e"))
"""36.Write a Python program to create a histogram from a given list of integers
"""
def histogram(items):
    for n in items:
        output=""
        times=n
        while(times>0):
            output += "*"

            times=times-1

        print(output)

histogram([2,3,6,5])