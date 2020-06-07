def add(x, y):
    return x + y


nums = [3, 5]
print(add(*nums))  # instead of add(nums[0], nums[1])
