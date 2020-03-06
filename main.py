import pytest

X = 1
fizz = 3
buzz = 5
fizzbuzz = [3, 5]

def check_X_not_divisible_by_3_and_5(X, fizzbuzz):
    for i in fizzbuzz:
        assert not X % i == 0
        X += 1

if __name__ == '__main__':
    main()
