from unittest import TestCase
from PLNFinalWork.foo import Foo

class TestFoo(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        self.foo = Foo()

    def test_foo(self):
        self.assertTrue(True, True)

if __name__ == '__main__':
    unittest.main()