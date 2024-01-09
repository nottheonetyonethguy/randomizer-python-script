import random

test_list = [1,2,3,4,5,6,7,8,9,10,11,12]
length = len(test_list)
new_list = []
for x in range(length):
    random_num = random.choice(test_list)
    new_list.append(random_num)
    test_list.pop(test_list.index(random_num))
print(new_list)

