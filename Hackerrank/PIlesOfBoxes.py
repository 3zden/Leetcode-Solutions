def getTotalSteps(heights):
    # write your code here
    heights.sort(reverse = True)
    out = 0
    count = 1
    print(heights)
    for i in range(len(heights)-1):
        # count = 0
        if heights[i] == heights[i+1]:
            count += 1
        else : 
            # print(count)
            out += count
            count += 1
    return out



