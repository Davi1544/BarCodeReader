from log import Log

encondings = {
    # L encoding
    "1110010": 0,
    "1100110": 1,
    "1101100": 2,
    "1000010": 3,
    "1011100": 4,
    "1001110": 5,
    "1010000": 6,
    "1000100": 7,
    "1001000": 8,
    "1110100": 9,

    # R encoding
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9,
}

def code2number(code : str) -> int:
    return encondings[code] if code in encondings else None

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
def breakCodeIntoSides(code : list[int]) -> list[list[list[int]]]:
    codeRemovedSideBars : list = code[3:len(code)-3]
    center : int = int(len(codeRemovedSideBars) / 2)
    leftSide : list[int] = codeRemovedSideBars[:center-2]
    rightSide : list[int] = codeRemovedSideBars[center+3:]
    leftEncodedNumbers : list[list[int]] = [leftSide[i:i + 7] for i in range(0, len(leftSide), 7)]
    rightEncodedNumbers : list[list[int]] = [rightSide[i:i + 7] for i in range(0, len(rightSide), 7)]
    return [leftEncodedNumbers, rightEncodedNumbers]

@Log.log
def fixSides(sides : list[list[list[int]]]) -> list[str]:
    isCorrect : bool = True

    # checking for upside down readings
    for encodedNumber in sides[0]: 
        # if the encodedNumber does not have an even amount of 1s, than the code was read upside-down
        if sum(encodedNumber) % 2 != 0:
            if code2number("".join(str(n) for n in encodedNumber)) in encondings:
                isCorrect = False
                break

    # joining sides and converting numbers into strings
    joinedSides = []
    
    # joining left
    for encodedNumber in sides[0]:
        number : str = "".join([str(i) for i in encodedNumber])
        joinedSides.append(number)

    # joining right
    for encodedNumber in sides[1]:
        number : str = "".join([str(i) for i in encodedNumber])
        joinedSides.append(number)
    
    # if the code was read upside down
    if not(isCorrect):
        joinedSides = joinedSides[::-1]
        joinedSides = [number[::-1] for number in joinedSides]
    
    # returning joined sides
    return joinedSides


@Log.log
def decode(encondedNumbers : list[str]) -> list[int]:
    return [code2number(encodedNumber) for encodedNumber in encondedNumbers]

@Log.log
def numberString(decodedNumbers : list[int]) -> str:
    return "".join(str(number) for number in decodedNumbers)

def isCodeComplete(decodedFinds : list) -> bool:
    for find in decodedFinds:
        if find == None: 
            return False
    return True
    
def countUnknowns(decodedFinds : list) -> int:
    count : int = 0
    for find in decodedFinds:
        if find == None:
            count += 1
    return count

@Log.log
def isCodeValid(decodedNumbers : list[int]) -> bool:
    # if the code is not complete, then it can still be valid
    # (this function will only be called after confirming that, at most, one digit is missing)
    if not(isCodeComplete(decodedNumbers)): return True

    # from here on, the code is complete
    checkDigit = decodedNumbers[11]
    oddSum : int = sum(decodedNumbers[::2])
    oddSum = oddSum * 3
    evenSum : int = sum(decodedNumbers[1:11:2])
    totalSum = oddSum + evenSum
    remainder = (totalSum % 10)
    
    # if the remainder is not 0, subtract it from 10
    if remainder != 0:
        remainder = 10 - remainder
    
    # matching the checkdigit
    if remainder != checkDigit:
        return False
    return True

@Log.log
def fixUnknown(decodedFinds : list[int]) -> list[int]:
    # finding the position of the unknown
    positionUnknown : int = 1
    for positon in range(len(decodedFinds)):
        if decodedFinds[positon] == None: 
            positionUnknown += positon
            break
    
    # case 1: checkDigit uknown
    if positionUnknown == 12:
        oddSum : int = sum(decodedFinds[::2])
        oddSum = oddSum * 3
        evenSum : int = sum(decodedFinds[1:11:2])
        totalSum = oddSum + evenSum
        remainder = (totalSum % 10)
        
        # if the remainder is not 0, subtract it from 10
        if remainder != 0:
            remainder = 10 - remainder

        decodedFinds[positionUnknown-1] = remainder

    # case 2: odd position
    elif(positionUnknown % 2 == 1):
        checkDigit = decodedFinds[11]
        remainder = 0
        if checkDigit != 0:
            remainder = 10 - checkDigit

        oddSum : int = 0
        evenSum : int = sum(decodedFinds[1:11:2])
        for num in decodedFinds[::2]:
            if num != None:
                oddSum += num
        
        decodedFinds[positionUnknown-1] = (10 - 3*(remainder - (oddSum*3 + evenSum) % 10))%10

    # case 3 - even unknown position
    else:
        checkDigit = decodedFinds[11]
        remainder = 0
        if checkDigit != 0:
            remainder = 10 - checkDigit

        oddSum : int = sum(decodedFinds[::2])
        oddSum *= 3
        evenSum = 0
        for num in decodedFinds[1:11:2]:
            if num != None:
                evenSum += num
        
        decodedFinds[positionUnknown-1] = remainder - ((oddSum + evenSum) % 10)

    return decodedFinds