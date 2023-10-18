from factorial import factorial
import pytest

def test_08():
    assert factorial(8) == 40320

def test_18():
    assert factorial(18) == 6402373705728000

def test_45():
    assert factorial(45) == 119622220865480194561963161495657715064383733760000000000

# print(factorial(8) == 40320)
# print(factorial(18) == 6402373705728000)
# print(factorial(45) == 119622220865480194561963161495657715064383733760000000000)
# Test how high of a number your program can calculate. Can you push it further?
