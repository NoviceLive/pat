from pat import Pat


pat = Pat()


def test_create():
    tests = {
        1: 'A', 2: 'Aa', 3: 'Aa0'
    }
    for one in tests:
        assert pat.create(one) == tests[one]


def test_locate():
    tests = {
        'Aa0': 0, 'Zz9': 20277, 'n2A': 397,
        '0x31634130': 62, '0x41326341': 66, '0x63413363': 70
    }
    for one in tests:
        assert pat.locate(one, big_endian=False) == tests[one]


def test_exception():
    try:
        pat.create(20281)
    except IndexError:
        pass
    else:
        assert False
    try:
        pat.locate('Zzz')
    except KeyError:
        pass
    else:
        assert False
