#! /usr/bin/python3

def CalculatePosition(file):
    with open(file) as f:
        h_pos = 0
        v_pos = 0
        for line in f:
            line = line.split()
            if line[0] == "forward":
                h_pos += int(line[1]) 
            elif line[0] == "down":
                v_pos += int(line[1])
            elif line[0] == "up":
                v_pos -= int(line[1])

    return (h_pos, v_pos)

if __name__ == "__main__":

    # Exercise 1
    test_h_position, test_v_position = CalculatePosition('test_input')
    assert test_h_position == 15 and test_v_position == 10
    h_position, v_position = CalculatePosition('input')
    print("Horizontal position: ", h_position)
    print("Depth position: ", v_position)
    print("Result: ", (h_position * v_position))
