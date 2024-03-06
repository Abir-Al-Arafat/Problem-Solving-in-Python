for idx in range(1, len(input)):
    if maxLeft[idx-1] < input[idx]:
        maxLeft.append(biggestLeft)
        biggestLeft = input[idx]
    else:
        maxLeft.append(biggestLeft)

for idx in range(len(input)-2, 0, -1):
    print("input[idx+1] input[idx]")
    print(input[idx+1], "-------------",input[idx])
    if biggestRight < input[idx]:
        # if len(maxRight) == 0:
        #     maxRight.append(biggestRight)
        # else:
        maxRight.insert(0, biggestRight)
        # [biggestRight] + maxRight
        biggestRight = input[idx]
        print("input[idx] bigger", maxRight)
    else:
        maxRight.insert(0, biggestRight)
        print("input[idx]", maxRight)
        # [biggestRight] + maxRight