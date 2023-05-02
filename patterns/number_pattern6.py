def pattern(rows):
    a=0
    print("The pattern is:",end="\n\n")
    for i in range(rows,0,-1):
        a+=1
        for j in range(1,i+1):
            print(a,end=" ")
        print("\n")

rows=int(input("Enter the number of rows: "))
pattern(rows)
