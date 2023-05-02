def pattern(rows):
    print("The pattern is:",end="\n\n")
    for i in range(rows,0,-1):
        for j in range(rows,i-1,-1):
            print(j,end=" ")
        print("\n")

rows=int(input("Enter the number of rows: "))
pattern(rows)
