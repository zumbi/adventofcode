#! /usr/bin/python3


def File2Array(file):
    with open(file) as f:
        array = []
        for line in f:
            array.append([int(x) for x in line.split()])

    return array


def CheckIncreasingValues(array):
    count = 0
    for i in range(len(array)-1):
        if (array[i] < array[i+1]):
            count = count + 1;

    return count


def SlidingWindow(array, window):
    array2 = []
    total = 0
    if len(array) <= window:
        return array
    for i in range(len(array) - window + 1):
        temp_array = array[i:i+window]
        import numpy as np
        total = np.sum(temp_array)
        array2.append(total)

    return array2


if __name__ == "__main__":

    # Exercise 1
    test_array = File2Array('test_input')
    res = CheckIncreasingValues(test_array)
    assert res == 7

    array = File2Array('input')
    res = CheckIncreasingValues(array)
    print("ex1) Number of increasing values: %s" % res)

    # Exercise 2
    sw = 3
    test_array2 = SlidingWindow(test_array, sw)
    res = CheckIncreasingValues(test_array2)
    assert res == 5

    array2 = SlidingWindow(array, sw)
    res = CheckIncreasingValues(array2)
    print("ex2) Number of increasing values with sliding window (%s): %s" % (sw, res))
