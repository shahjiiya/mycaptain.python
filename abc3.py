#Input: list1 = [12, -7, 5, 64, -14]
#Output: 12, 5, 64
list1 = [12, -7, 5, 64, -14]
num=0
while(num < len(list1)):
     
    # checking condition
    if list1[num] >= 0:
        print(list1[num], end = " ")
     
    # increment num
    num += 1


#Input: list2 = [12, 14, -95, 3]
#Output: [12, 14, 3]
list2 = [12, 14, -95, 3]
num=0
while(num < len(list2)):

    #checking condition
    if list2[num] >= 0:
        print(list2[num], end = " ")

    #increment num
    num += 1
