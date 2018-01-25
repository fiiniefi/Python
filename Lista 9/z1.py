from l4z1 import pierwsze_skladana, pierwsze_funkcyjna, pierwsze_iterator, PierwszeIterator, KolekcjaPierwszych
import unittest


class PrimeNumbersTests(unittest.TestCase):
    """Tests for prime numbers lists"""
    def __init__(self, x):
        self.it = PierwszeIterator()
        self.it.__next__()
        self.it.__next__()
        self.prime = getattr(self.it, '_PierwszeIterator__pierwsza')
        super(PrimeNumbersTests, self).__init__(x)

    def test_prime_lc(self):
        """Is length of a list correct? (list comprehension implementation)"""
        self.assertTrue(len(pierwsze_skladana(20)) == 8)

    def test_prime_functional(self):
        """Is length of a list correct? (functional implementation)"""
        self.assertTrue(len(pierwsze_skladana(20)) == 8)

    def test_if_prime_f(self):
        """Is a prime number? (expected false)"""
        self.assertFalse(self.prime(9))

    def test_if_prime_t(self):
        """Is a prime number? (expected true)"""
        self.assertTrue(self.prime(98387))

    def test_if_correct(self):
        """Is returned value a prime number?"""
        self.assertTrue(self.prime(self.it.__next__()))

    def test_if_generator(self):
        """Is an object iterable?"""
        self.assertTrue(isinstance(pierwsze_iterator(20), list))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(PrimeNumbersTests)
    unittest.TextTestRunner(verbosity=3).run(suite)
