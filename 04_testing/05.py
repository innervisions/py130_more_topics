import unittest

class TestSomething(unittest.TestCase):
    def test_xyz_not_in_lst(self):
        lst = ['abc', 'def']
        # Your code here
        self.assertNotIn('xyz', lst)

unittest.main()
