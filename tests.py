import pytest

def check_X_not_divisible_by_3_and_5(fizzbuzz):
    for i in fizzbuzz:
        modulo = 2 % i
        assert modulo != 0

def launch_tests(fizz, buzz):
    fizzbuzz = [fizz, buzz]
    check_X_not_divisible_by_3_and_5(fizzbuzz)

fizz = 3
buzz = 5
launch_tests(fizz, buzz)
