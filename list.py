nums = [] #initialize an empty list
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    nums.append(num) #append each input to the list

print("Numbers:", nums) #print the list of numbers
print("Max", max(nums)) #print the maximum number in the list
print("Min", min(nums)) #print the minimum number in the list
print("Avg", sum(nums)/len(nums)) #print the average of the numbers in the list