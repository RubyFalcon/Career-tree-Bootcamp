def print_matrix(start,finish):
    for i in range(start,finish+1):
        for j in range(start,finish+1):
            print(f"{i*j:3}", end=" ")
        print()