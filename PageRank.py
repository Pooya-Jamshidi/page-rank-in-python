#! python3
# PageRank.py - This program get a matrix with list in list and return a list contains page Rank of every element of it
# author : Pooya Jamshidi
# ....

# importing a method from that page and using is_float method
import functions as func

def page_rank(matrix, epsilon):
    """
        This function get a list of names and sort it by length of names
        :param matrix: its a list in list like a matrix(n * n)
        :param epsilon: its a double number
        :return: a list with page ranks
    """
    # Searching for bad inputs
    for lis in matrix:
        if len(lis) != len(matrix):
            return "Your Matrix is wrong"

    for lis in matrix:
        for i in lis:
            if not func.is_float(str(i)):
                return "Your Matrix is wrong"
            if i < 0 or i > 1:
                return "Your Matrix is wrong"

    # variables
    pr = []
    outputs = []

    # Raising iteration 0 and by default sending 1
    for i in range(0, len(matrix)):
        pr.append(1)

    # Finding outputs of every page
    for lis in matrix:
        f = 0
        c = 0
        for i in lis:
            c += i
            if i != 0:
                f += 1
        outputs.append(c * f)

    # Calculating iteration 1,2 and replace every one of them with perivious one
    for i in range(2):
        for j in range(len(pr)):
            sigma = 0
            k = 0
            for lis in matrix:
                if lis[j] != 0:
                    if outputs[k] != 0:
                        sigma += pr[k] / outputs[k]
                k += 1
            pr[j] = (1 - epsilon) + (epsilon * sigma)

    # Returning a list contains iteration 2
    return pr;

# Testing the function
matrix = [[0, 0.5, 0.5], [0, 0, 1], [1, 0, 0]]
print(page_rank(matrix, 0.85))

# Testing the function
matrix = [[0, 0.5, 0.5, 0, 0, 0], [0.25, 0, 0, 0.25, 0.25, 0.25], [0.5, 0, 0, 0, 0, 0.5], [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0]]
print(page_rank(matrix, 0.8))
