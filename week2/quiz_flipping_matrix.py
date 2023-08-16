#!/bin/python3
import os

def flippingMatrix(matrix):
    result = 0
    n = len(matrix)//2
    for i in range(n):
        for j in range(n):
            max_sum = max(
                matrix[i][j], matrix[i][(2*n-1)-j],
                matrix[(2*n-1)-i][j], matrix[(2*n-1)-i][(2*n-1)-j]
                )
            result += max_sum
    return result
            
if __name__ == '__main__':

    q = int(input("Give No. of query").strip())

    for q_itr in range(q):
        n = int(input("Give n value").strip())

        matrix = []

        for _ in range(2 * n):
            
            matrix.append(list(map(int, input("Give matrix element element").rstrip().split())))

        result = flippingMatrix(matrix)

        print(result)
