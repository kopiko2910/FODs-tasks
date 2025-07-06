import numpy as np

def input_matrix(name):
    while True:
        try:
            rows = int(input(f"Enter number of rows for matrix {name}: "))
            cols = int(input(f"Enter number of columns for matrix {name}: "))
            
            print(f"Enter elements for matrix {name} (row-wise, space separated):")
            elements = []
            for i in range(rows):
                row = list(map(float, input(f"Row {i+1}: ").split()))
                if len(row) != cols:
                    raise ValueError(f"Expected {cols} elements, got {len(row)}")
                elements.append(row)
            
            return np.array(elements)
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def main():
    print("Matrix Operations Program")
    print("------------------------")
    
   
    A = input_matrix("A")
    B = input_matrix("B")
    
    print("\nMatrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)
    
   
    try:
        
        if A.shape == B.shape:
            print("\nMatrix Addition (A + B):")
            print(A + B)
        else:
            raise ValueError("Matrices must have same dimensions for addition")
        
      
        if A.shape == B.shape:
            print("\nMatrix Subtraction (A - B):")
            print(A - B)
        else:
            raise ValueError("Matrices must have same dimensions for subtraction")
        
       
        if A.shape[1] == B.shape[0]:
            print("\nMatrix Multiplication (A × B):")
            print(np.matmul(A, B))
        else:
            raise ValueError("Number of columns in A must match number of rows in B for multiplication")
            
       
        if A.shape == B.shape:
            print("\nElement-wise Multiplication (A * B):")
            print(A * B)
        else:
            raise ValueError("Matrices must have same dimensions for element-wise multiplication")
            
    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()