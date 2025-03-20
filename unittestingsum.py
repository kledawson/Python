import unittest # testing framework for python

def sum_integers(numbers):
    # check if list and elements are ints
    if not isinstance(numbers, list):
        raise TypeError("Not a list")
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("Elements are not ints")
    
    return sum(numbers) # python's built in sum function instead of for loop

class TestSumInts(unittest.TestCase): # both valid and invalid test cases
    
    def test_valid(self):
        # valid cases
        self.assertEqual(sum_integers([]), 0)
        self.assertEqual(sum_integers([256]), 256)
        self.assertEqual(sum_integers([42, 17, 23, 8, 11]), 101)
        self.assertEqual(sum_integers([-14, 7, 3, 4]), 0)
    
    def test_invalid(self):
        # string instead of list
        with self.assertRaises(TypeError):
            sum_integers("not a list")
        # integer instead of list
        with self.assertRaises(TypeError):
            sum_integers(12345)
        # none instead if list
        with self.assertRaises(TypeError):
            sum_integers(None)

        # string in list
        with self.assertRaises(TypeError):
            sum_integers([1, 2, "3", 4, 5])
        # float in list
        with self.assertRaises(TypeError):
            sum_integers([1, 2, 3.5, 4, 5])
    

if __name__ == '__main__': # runs the test
    unittest.main()
