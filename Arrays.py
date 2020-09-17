#1.2 - Check permutation
def ifpermute(a,b):

    l1 = len(a)
    l2 = len(b)

    if l1 != l2:
        return False

    a = sorted(a)
    b = sorted(b)
    for i in range(0,l1):
        if a[i] != b[i]:
            return False
    
    return True

#1.3 - URLif
def URLify(s):

    s = s.strip() #Removes spaces in the beginning and end
    
    return s.replace(" ","%20")

#1.4 - Palindrome Permutation
def Pal(s):
    a = []
    s = s.replace(" ","").lower()
    
    for i in range(len(s)):
        if s[i] in a:
            a.remove(s[i])
        else:
            a.append(s[i])
    
    l1 = len(s)
    l2 = len(a)

    if (l1%2 == 0 and l2==0) or (l1%2 == 1 and l2==1):
        return True
    else:
        return False


#1.5 - One Way
def oneway(s1, s2):
    l1 = len(s1)
    l2 = len(s2)

    if abs(l1-l2)>1:
        return False
    
    m = 0
    n = 0

    count = 0

    while m<l1 and n<l2:

        if s1[m]!=s2[n]:
            if count==1:
                return False

            if m>n:
                n += 1
            elif m<n:
                m += 1
            else:
                m += 1
                n += 1
            
            count += 1

        else:
            m += 1
            n += 1
        
    if m<l1 or n<l2:
        count += 1
    
    return count == 1

#1.6 - String Compression
def strcomp(s):
    st = []
    count = 1
    n = s[0]

    for i in range(1, len(s)):
        if n == s[i]:
            count += 1
        else:
            st.append(n)
            st.append(count)
            n = s[i]
            count = 1
    
    st.append(n)
    st.append(count)


    return "".join(map(str, st)) # Maps the list to string since join cant have int

#1.7 - Rotate Matrix (Left-side rotation)
def rot(matrix):
    l = len(matrix)
    for i in matrix:
        i.reverse()
    for i in range(l):
        for j in range(l):
            if i<j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    return matrix

#1.8 - Zero Matrix
def zermat(matrix):

    A = len(matrix)
    B = len(matrix[0])

    row = set()
    col = set()

    for i in range(A):
        for j in range(B):

            if matrix[i][j]==0:
                row.add(i)
                col.add(j)
    
    for i in range(A):
        for j in range(B):

            if i in row or j in col:
                matrix[i][j]=0
    
    return matrix
    


#1.9 - String Rotation
def strrot(s1, s2):
    l1 = len(s1)
    l2 = len(s2)

    if l1 != l2:
        return False
    
    for i in range(l1):
        if s2.startswith(s1[i:]) and s2.endswith(s1[:i]):
            return True
    
    return False




# main
if __name__ == "__main__":
    a = 'abc'
    b = 'cab'

    s = 'aaabbbcccc'

    s1 = 'watera'
    s2 = 'terwaa'

    matrix = [[1,2,3],[4,5,6],[7,8,9]]

    print(strrot(s1, s2))
    
