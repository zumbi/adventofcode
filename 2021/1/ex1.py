#! /usr/bin/python3

def File2Array(file):
    with open(file) as f:
        array = []
        for line in f:
            array.append([int(x) for x in line.split()])

    return array

def CheckIncreasingValues(array):
    length = len(array)
    count = 0
    for i in range (0, length-1):
        if (array[i] < array[i+1]):
            count = count + 1;

    return count

if __name__ == "__main__":

    array = File2Array('test_input')
    num = CheckIncreasingValues(array)
    # print("[test] Number of increasing values %s" % num)
    assert num == 7

    array = File2Array('input')
    num = CheckIncreasingValues(array)
    print("Number of increasing values %s" % num)

