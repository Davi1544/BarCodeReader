from log import Log

@Log.log
def listlist2list(arr : list[list]) -> list:
    return [i[0] for i in arr]

@Log.log
def colorlist2binarylist(arr : list[int], breakpoint : int) -> list:
    return [0 if i < breakpoint else 1 for i in arr] 