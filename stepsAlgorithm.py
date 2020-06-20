"""
There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function
that returns the number of unique wass you can climb the staircase. The order of the steps matters.

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
For example if X = {1, 3, 5}, you could climb 1, 3, 5 steps at a time.

Generalize your function to take in X.
"""
from itertools import permutations

combinations = []
tempComb = []
N = 5
steps = [1,3,2,5,6] 
newSteps = []

# We discard all elements greater tan number of stairs and in one 
# element is equal, we add the unique combination in the list 
# of the possible ones
for index, num in enumerate(steps[:]):
    if num > N:
        steps.pop(index)
    elif num==N:
        combinations.append([num])
    else:
        newSteps.append(num)
# Ordering the element in the list
newSteps.sort()

def returnDiffN(array, element=0):
    return N - (sum(array) + element)
    
# we create combination of numbers that sum up to N
for index in range(len(newSteps)):
    n_max = N//newSteps[index]
    print("first loop", n_max)

    # return all possible temporary arrays with different numbers of selected element based on n
    for occurrencies in range(1,n_max+1):
        print(" Occurrencies")
        tempComb = [newSteps[index]]*occurrencies
        print(" ", tempComb)
        print(returnDiffN(tempComb))
        if returnDiffN(tempComb) == 0:
            combinations.append(tempComb)
        elif returnDiffN(tempComb) < 0:
            break
        else:
            print("     the sum of the items is less than ", N, " and is: ", sum(tempComb))
            for newIndex in range(index+1, len(newSteps)):
                if len(tempComb) == 0:
                    break
                print("second loop", newIndex)
                while sum(tempComb) < N:
                    
                    if returnDiffN(tempComb, newSteps[newIndex]) == 0:
                        tempComb.append(newSteps[newIndex])
                        combinations.append(tempComb)
                        tempComb=[]
                        print(tempComb)
                        break

                    elif returnDiffN(tempComb, newSteps[newIndex]) > 0:
                        tempComb.append(newSteps[newIndex])
                    else:
                        break
        tempComb=[]

print(len(combinations), newSteps, combinations)
