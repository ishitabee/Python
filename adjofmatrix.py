#adjoint of a matrix

#selecting values inside the matrix
#a12= element of the 1st row and 2nd column
#a21= element of the 2nd row and 1st column

i=int(input("Enter the number of rows you want in the matrix: "))
j=int(input("Enter the number of columns you want in the matrix: "))

if i!=j:
    print("Adjoint is not possible, as the matrix is not square.(Made up of equal number of rows and columns)")
else:
    for a  in (1,i+1):
        print("Enter the elements of the matrix row-wise a: ")
  