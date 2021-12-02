#! /usr/bin/python3

def CalculatePosition(file):
    with open(file) as f:
        h_pos = 0
        v_pos = 0
        aim = 0
        depth = 0
        for line in f:
            line = line.split()
            if line[0] == "forward":
                h_pos += int(line[1])
                if aim != 0:
                    depth += int(line[1])*aim
            elif line[0] == "down":
                aim += int(line[1])
            elif line[0] == "up":
                aim -= int(line[1])

    return (h_pos, depth)

if __name__ == "__main__":

    # Exercise 1
    test_h_position, test_depth = CalculatePosition('test_input')
    assert test_h_position == 15 and test_depth == 60
    h_position, depth = CalculatePosition('input')
    print("Horizontal position: ", h_position)
    print("Depth position: ", depth)
    print("Result: ", (h_position * depth))
