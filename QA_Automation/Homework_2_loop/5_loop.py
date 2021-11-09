# 5. Перемножить все не чётные значения в диапазоне от 9173 до 9435;
print("5. Перемножить все не чётные значения в диапазоне от 9173 до 9435;")

numFirst = 9173
numSec = 9434
numProduct = 1
print("numFirst = 9173", "numSec = 9435")
nums = list(range(numFirst, numSec + 1))

for i in nums:
    if i % 2 == 0:
        continue
    else:
        numProduct = numProduct * i
print(f"The product of even number in range {numFirst} to {numSec} is:", numProduct)
