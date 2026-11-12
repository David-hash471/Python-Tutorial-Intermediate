'''
LESSON 18 - STATIC METHOD
@staticmethod decerator
'''

class String_manipulator:
    @staticmethod
    def reverse_string(s): #don't need to use self method
        return s[::-1]

    @staticmethod
    def count_vowels(s):
        vowels = 'aeiouAEIOU'
        return sum(1 for char in s if char in vowels)

    @staticmethod
    def remove_symbols(s):
        return ''.join(char for char in s if char.isalnum() or char.isspace())


string = 'Hello world []!!@'
print(String_manipulator.reverse_string(string))
print(String_manipulator.count_vowels(string))
print(String_manipulator.remove_symbols(string))