from pat import Pat


pat = Pat()


def test_create_pattern():
    tests = {
        1: 'A', 2: 'Aa', 3: 'Aa0'
    }
    for one in tests:
        assert pat.create_pattern(one) == tests[one]


def test_locate_pattern():
    tests = {
        'Aa0': 0, 'Zz9': 20277, 'n2A': 397
    }
    for one in tests:
        assert pat.locate_pattern(one) == tests[one]
