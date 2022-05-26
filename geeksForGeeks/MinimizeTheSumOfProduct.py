class MinSumOfProduct:

    def __init__(self, arr1, arr2):
        self.arr2 = arr2
        self.arr1 = arr1

    def minSumOfProduct_3(self, arr1, arr2):
        # Time Complexity: O(n^2)
        arr1.sort()
        arr2.sort(reverse=True)
        sum_of_product = 0
        for i in range(len(arr1)):
            sum_of_product += arr1[i] * arr2[i]
        return sum_of_product


obj = MinSumOfProduct()
print(obj.minSumOfProduct_3([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]))
# print(obj.arr1)
obj.arr2.__setitem__(0, 10)
print(obj.arr2.__len__())
print(print(obj.arr2))
