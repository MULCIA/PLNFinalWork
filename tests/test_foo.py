from unittest import TestCase
from PLNFinalWork.foo import Foo

class TestFoo(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        self.foo = Foo()

    def test_foo(self):
    	self.foo()
        self.assertEqual(self.foo, "foo")

if __name__ == '__main__':
    unittest.main()