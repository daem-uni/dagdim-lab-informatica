nums_in = input("Inserisci una lista di numeri separati da spazi: ")

nums = nums_in.split(" ")

running_sum = 0

for i in range(len(nums)):
    if i % 2 == 0:
        running_sum += int(nums[i])
    else:        
        running_sum -= int(nums[i])

print("Il risultato è", running_sum)