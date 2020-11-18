def sumWithoutSmallest(array):
    min_num = array[0]
    running_sum = 0

    for e in array:
        running_sum += e

        if e < min_num:
            min_num = e

    return running_sum - min_num

nums = input("Inserire una lista di numeri separati da uno spazio: ")

nums_list = []

for n in nums.split(" "):
    nums_list.append(int(n))

final_sum = sumWithoutSmallest(nums_list)
print("La somma meno il numero più piccolo è:", final_sum)