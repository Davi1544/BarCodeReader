from log import Log

@Log.log
def resizeBinaryList(binaryList : list[int]) -> list[int]:
    # Strategy 1 for finding the correct bar size
    # - Find the first guard bars and get their sizes
    # - Assume the smallest guard bar to have the correct size
    size : int = len(binaryList)        # biggest possible value of size
    counter : int = 0
    barsFound : int = 0
    for bit in binaryList:
        # if the bit is 0
        if bit == 0:
            counter += 1

        # if the bit is 1
        else:
            if counter == 0: continue
            # else

            if size > counter: size = counter
            counter = 0
            barsFound += 1

        if barsFound == 2: break        # stop as soon as the second bar ends
    
    
    # size found

    lo : int = 0                        # first bar first pixel position
    hi : int = 0                        # last bar last pixel position

    # finding lo
    for pos in range(len(binaryList)):
        if binaryList[pos] == 0: 
            lo = pos
            break
    
    # finding hi
    for pos in range(len(binaryList) - 1, -1, -1):
        if binaryList[pos] == 0:
            hi = pos
            break
    
    # defining the code barriers
    code : list[int] = binaryList[lo:hi+1]

    # resizing the code
    resizedCode : list[int] = list()
    counter = 0
    for bit in code:
        counter += 1
        if counter == size:
            resizedCode.append(bit)
            counter = 0
    
    return resizedCode


@Log.log
def breakCodeIntoSides(code : list[int]) -> list[list[int]]:
    codeRemovedSideBars : list = code[3:len(code)-3]
    center : int = int(len(codeRemovedSideBars) / 2)
    return [codeRemovedSideBars[:center-2], codeRemovedSideBars[center+3:]]