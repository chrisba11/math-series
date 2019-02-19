from series import fibonacci


def test_check_n_at_1():
    actual = fibonacci(1)
    expected = 0
    assert actual == expected


def test_check_n_at_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_check_n_at_3():
    actual = fibonacci(3)
    expected = 1
    assert actual == expected


def test_check_n_at_4():
    actual = fibonacci(4)
    expected = 2
    assert actual == expected


def test_check_n_at_8():
    actual = fibonacci(8)
    expected = 13
    assert actual == expected
