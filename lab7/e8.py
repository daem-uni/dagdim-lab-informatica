def clean_noise(arr):
    if len(arr) < 2:
        return arr

    last = 0

    for i in range(len(arr)):
        tmp = arr[i]
        if i == len(arr) - 1:
            arr[i] = (last + arr[i]) / 2
        elif i == 0:
            arr[i] = (arr[i] + arr[i + 1]) / 2
        else:
            arr[i] = (last + arr[i] + arr[i + 1]) / 3
        
        last = tmp

    return arr

nums_input = input("Inserire una lista di numeri separati da uno spazio: ")
nums = []
for n in nums_input.split(" "):
    nums.append(int(n))


print(clean_noise(nums))
