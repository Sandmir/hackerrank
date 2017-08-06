__author__ = 'marina_senyutina'
import unittest

def productExceptSelf(nums):

    if nums.count(0)>1:
        return [0]*len(nums)

    p = 1
    n = len(nums)
    output = []
    for i in range(0,n):
        output.append(p)
        p = p * nums[i]
    print(output)
    p = 1
    for i in range(n-1,-1,-1):
        output[i] = output[i] * p
        p = p * nums[i]
    return output

class ProductExceptSelf(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_positive(self):
        self.assertEqual(productExceptSelf([1,2,3,4]),[24,12,8,6])
        self.assertEqual(productExceptSelf([4,2,3,5]),[30,60,40,24])


if __name__=='__main__':
   unittest.main()