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
#def oneway(a, b):

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
    