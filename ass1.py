
def lower_triangular(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()
    print()

n = 5
lower_triangular(n)
def upper_triangular(n):
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()
    print()

n = 5
upper_triangular(n)
def pyramid(n):
    for i in range(1, n+1):
        # Print leading spaces
        for j in range(n-i):
            print(" ", end=" ")
        # Print stars
        for k in range(2*i-1):
            print("*", end=" ")
        print()
    print()

n = 5
pyramid(n)

