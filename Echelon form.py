def fixRowTwo(A) :
    # Insert code below to set the sub-diagonal elements of row two to zero (there are two of them).
    A[2] = A[2]- A[2,0]*A[0]
    A[2] = A[2]- A[2,1]*A[1]
    
    
    # Next we'll test that the diagonal element is not zero.
    if A[2,2] == 0 :
        # Insert code below that adds a lower row to row 2.
        A[2] = A[2]+A[3]
        
        
    
        
        # Now repeat your code which sets the sub-diagonal elements to zero.
        A[2] = A[2]- A[2,0]*A[0]
        A[2] = A[2]- A[2,1]*A[1]
        
        
    if A[2,2] == 0 :
        
        raise MatrixIsSingular()
    # Finally set the diagonal element to one by dividing the whole row by that element.
    A[2] = A[2] / A[2,2]
    
    return A
    
   
  def fixRowThree(A) :
    # Insert code below to set the sub-diagonal elements of row three to zero.
    A[3] = A[3] - A[3,0] * A[0]
    A[3] = A[3] - A[3,1] * A[1]
    A[3] = A[3] - A[3,2] * A[2]
    
    
    
    # Complete the if statement to test if the diagonal element is zero.
    if A[3,3] == 0 :
        raise MatrixIsSingular()
    # Transform the row to set the diagonal element to one.
    A[3] = A[3] / A[3,3]
    return A
