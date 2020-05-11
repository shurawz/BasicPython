def oddnumbers():
    n = 1
    while True:
        yield n
        n += 2


def pi_series():
    odds = oddnumbers()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation


pi_ser = pi_series()

for x in range(1000000):
    print(next(pi_ser))

# It has to be looped more than 100000000 I guess to get the true result.
