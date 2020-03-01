import time


def squareNum(arr):
    for i in arr:
        yield i*i


my_arr = squareNum([1, 2, 3, 4, 5])
for num in my_arr:
    print(num)


def people_list(num_of_times):
    result = []
    for i in range(num_of_times):
        person = {
            'name': 'pramila',
            'age': 25
        }
        result.append(person)
    return result


def people_generator(num_of_times):
    for i in range(num_of_times):
        person = {
            'name': 'pramila',
            'age': 25
        }
        yield person


        # print(people_list(5))
# t1 = time.process_time()
# print(t1)
# people = people_list(1000000)
# t2 = time.process_time()
# print(t2)
people = people_generator(4)
for x in people:
    print(x)
