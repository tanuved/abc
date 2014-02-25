'''
Problem: Find the intersection of two lists
Should be the most efficient

Solution: Add list1 to hashmap/dictionary loop over elements in list2 and compare results
Assumptions: Elements of lists are ints
'''

def listToMap(lst):
    'Adds elements of a list to a dictionary'
    d = {}
    for x in lst:
        d[x] = x #mapping to itself, using element as key for best lookup
    return d

def listAndMapIntersect(lst, dictiond):
    #Added exception handling: Getting "KeyError" when not dictionary out of range
    'takes in a lst and a dictionary looks up and adds common values into new list'
    commonList = []
    for x in lst:
        try:
            if dictiond[x]:
                commonList.append(x)
        except KeyError:
            pass
    return commonList

def printResult(lst):
    'takes in a list and displays it'
    for x in lst:
        print x
    
def main():
    l1 = [1,2,3,4,5]
    l2 = [3,4,5,6,7]
    l3 = [6,7,3,5,1,6,8,9]
    
    d = listToMap(l1)
    lst = listAndMapIntersect(l2, d)
    printResult(lst)

main()
