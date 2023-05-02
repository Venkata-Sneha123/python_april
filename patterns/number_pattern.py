def pattern(rows):
    print("The pattern is:",end="\n\n")
    for i in range(1,rows+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print("\n")

rows=int(input("Enter the number of rows: "))
pattern(rows)
