def permuting_two_array(k,A,B):
    A.sort()
    B.sort(reverse = True)

    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"
    return "YES"

if __name__ == '__main__':
    q = int(input("Enter no. of testcase you want to execute: ").strip())

    for q_itr in range(q):
        n_and_k_input = input("Enter comma separated length of array and value with which sum is to be compared:").rstrip().split()
        n = int(n_and_k_input[0])
        k = int(n_and_k_input[1])

        A = list(map(int, input("Enter all element of array A").rstrip().split()))
        B = list(map(int, input("Enter all element of array B").rstrip().split()))

        result = permuting_two_array(k, A, B)
        print(result)