import unittest
from hypothesis import given, strategies as st, settings, Verbosity


# Function to test
def add(a: int, b: int) -> int:
    return a + b




class TestAddFunction(unittest.TestCase):
    # Property 1: Commutativity
    @given(st.integers(), st.integers())
    @settings(verbosity=Verbosity.verbose)
    def test_commutativity(self, a, b):
        self.assertEqual(add(a, b), add(b, a))

    # Property 2: Associativity
    @given(st.integers(), st.integers(), st.integers())
    def test_associativity(self, a, b, c):
        self.assertEqual(add(add(a, b), c), add(a, add(b, c)))

    # Property 3: Identity element
    @given(st.integers())
    def test_identity_element(self, a):
        self.assertEqual(add(a, 0), a)
        self.assertEqual(add(0, a), a)

    # Property 4: Closure
    @given(st.integers(), st.integers())
    def test_closure(self, a, b):
        result = add(a, b)
        self.assertIsInstance(result, int)
