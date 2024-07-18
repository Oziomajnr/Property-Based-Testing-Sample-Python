import random

from hypothesis import given, strategies as st, settings, Verbosity, example, seed


def add(a, b):
    return a + b


def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0


# Property 1: Commutativity
@given(st.integers(), st.integers())
@settings(verbosity=Verbosity.verbose)
def test_commutativity(a, b):
    assert add(a, b) == add(b, a)


# Property 2: Associativity
# @given(st.integers(), st.integers(), st.integers())
# def test_associativity(a, b, c):
#     assert add(add(a, b), c) == add(a, add(b, c))
#
#
# # Property 3: Identity element
# @given(st.integers())
# def test_identity_element(a):
#     assert add(a, 0) == a
#     assert add(0, a) == a
#
#
# # Property 4: Closure
# @given(st.integers(), st.integers())
# def test_closure(a, b):
#     result = add(a, b)
#     assert isinstance(result, int)
