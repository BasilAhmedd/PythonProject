def multiply_positives_by_four(numbers):
    for i in range(len(numbers)):
        if numbers[i] > 0:
            numbers[i] *= 4
    return numbers


input_str = input("Enter numbers separated by commas: ")
lis = list(map(int, input_str.split(',')))

result = multiply_positives_by_four(lis)
print(result)

# x = str(input("Enter Data (first_name age grade) : "))
# y = x.split()
# if y[2]=="A" or y[2]=="B" or y[2]=="C" :
#     f = True
# else :
#     f = False
# my_dict={
#      "name":y[0],
#      "age":y[1],
#      "Grade": y[2],
#      "Passed": f
#
# }
# print(my_dict)