'''
Lesson 1 - Nested function
nested function
f5 button to debug
.vscode button
'''
def extract_valid_triplet(numbers_str):
    def is_triplet(n):
        return len(n) == 3

    def is_float(n):
        try :
            return float(n)
        except ValueError:
            return None

    def process_numbers():
        for num_str in numbers_list:
            num = is_float(num_str)
            if num is not None:
                valid_numbers.append(num)



        
    numbers_list = numbers_str.split(' ')
    valid_numbers = []

    if is_triplet(numbers_list):
        process_numbers()
        if is_triplet(valid_numbers):
            return valid_numbers

    return []



def main():
    number_input = input('Write 3 numbers seperated by a space (example: 1 0.5 3.14): ')
    valid_triplet = extract_valid_triplet(number_input)
    print(valid_triplet)

if __name__ == '__main__':
    main()