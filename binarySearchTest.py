import unittest
from binarySearch import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_case1(self):
        # Test: If the target 1 is in the array, return the index 0
        arr = [1, 2, 3, 4, 5]
        self.assertTrue(binary_search(arr,1) == 0, "test1 failed")
        print("test passed")

    def test_case2(self):
        # Test: If the target 6 is not in the array, return -1
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr,6), -1, "test2 failed")
        print("test passed")

if __name__ == '__main__':
    unittest.main()