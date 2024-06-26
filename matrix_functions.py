def rref_mod2(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    row = 0
    
    for col in range(cols):
        if row >= rows:
            break
        
        pivot = row
        while pivot < rows and matrix[pivot][col] == 0:
            pivot += 1
            
        if pivot == rows:
            continue
        
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        
        for r in range(rows):
            if r != row and matrix[r][col] == 1:
                matrix[r] = [(matrix[r][c] + matrix[row][c]) % 2 for c in range(cols)]
        
        row += 1
        
    return matrix

def null_space_mod2(matrix):
    rref_matrix = rref_mod2(matrix)
    rows = len(rref_matrix)
    cols = len(rref_matrix[0])
    pivot_cols = []
    
    for r in range(rows):
        for c in range(cols):
            if rref_matrix[r][c] == 1:
                pivot_cols.append(c)
                break
                
    free_vars = [c for c in range(cols) if c not in pivot_cols]
    null_space_vectors = []
    
    for free_var in free_vars:
        vector = [0] * cols
        vector[free_var] = 1
        for r in range(rows):
            if rref_matrix[r][free_var] == 1:
                vector[pivot_cols[r]] = (vector[pivot_cols[r]] + 1) % 2
        null_space_vectors.append(vector)
        
    return null_space_vectors

def transpose(matrix):
    # Calculate dimensions of the original matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Transpose the matrix in place
    for i in range(rows):
        for j in range(i + 1, cols):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Resize the matrix to swap rows and columns
    matrix[:] = [row[:rows] for row in matrix]

    return matrix