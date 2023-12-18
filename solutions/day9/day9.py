lines = open('solutions/day9/input.txt').read().splitlines()


    
def get_differences(nums):
    differences = []
    for i in range(len(nums)-1):
        differences.append(nums[i+1] - nums[i])
    return differences

def oasis(nums, total_sum):
    differences = get_differences(nums)
    if any(differences) != 0:
        total_sum += oasis(differences, total_sum)
    total_sum += nums[len(nums) - 1]
    return total_sum
        
    
part = 2
    
sum = 0
for line in lines:
    nums = [int(x) for x in line.split()]
    if part == 2:
        nums = nums[::-1]
    sum += oasis(nums, 0)
    
print(sum)

