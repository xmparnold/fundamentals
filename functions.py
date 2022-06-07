def add_two_numbers(num1, num2):
    total = num1 + num2
    return total

result = add_two_numbers(20, 30)

print(result)

def print_grades(grade1 = 0.0, grade2 = 0.0, grade3 = 0.0):
    print("grade 1 ", grade1)
    print("grade 2 ", grade2)
    print("grade 3 ", grade3)

# named arguments let us choose which argument slot the value will be placed in as follows:
print_grades(grade2 = 9.2)

def some_function(list):
    print(list)
    total = 0.0
    for element in list:
        print(element)
        total += element
    return total

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = some_function(nums)
print("expecting a 55", f"Got a {total}")


