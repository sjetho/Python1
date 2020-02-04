# Medium 1 and 2

# def list(input):
#     sorted_list = sorted(input)
#     print(sorted_list[0])
# list([9,10,3,5,8,7])
# def list(input):
#     sorted_list = sorted(input, reverse=True)
#     print(sorted_list[0])
# list([1,4,5,2,10,9])

#Medium 3 and 4
# strings = ("These", "are", "words", "that", "i", "am", "testing")

# def small(st):
#     sm = min(st, key=len)
#     return sm
# result = small(strings)
# print(result)

# def large(st):
#     sm = max(st, key=len)
#     return sm
# result = large(strings)
# print(result)

list = [1,2,3,2,8,7,4]

def small(list):
    y = list[0]
    for i in list:
        if i < y:
            y = i
    return(y)
print(small(list))

