class MinSumOfProduct:

    def __init__(self, arr1, arr2):
        self.arr2 = arr2
        self.arr1 = arr1

    def min_sum_of_product_3(self):
        # Time Complexity: O(n^2)
        self.arr1.sort()
        self.arr2.sort(reverse=True)
        sum_of_product = 0
        for i in range(len(self.arr1)):
            sum_of_product += self.arr1[i] * self.arr2[i]
        return sum_of_product


a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5, 6]

obj = MinSumOfProduct(a, b)
print(obj.min_sum_of_product_3())
print(obj.arr1)
obj.arr2.__setitem__(0, 10)
print(obj.arr2.__len__())
print(print(obj.arr2))
