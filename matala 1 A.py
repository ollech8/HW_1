##Q1
def my_func(x1,x2,x3):
    numbers=[x1,x2,x3]
    for i in numbers:
        if not isinstance(i,float):
            if not isinstance(i,int):
                return 'None'
            else:
               return "Error: parameters should be float"

    if x1+x2+x3==0:
       return "Not a number- denominator equals zero"

    return ((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)
print(my_func(2,1,3))
 ###Q2
def revword (word):
    reverse_lower=(word[::-1]).lower()
    return reverse_lower


def countword ():
    with open("text.txt",'r') as f:
        word = f.readline().strip()
        count = 1
        for i in f:
            a = i.split()
            for j in a:
                if revword(j) == word:
                    count = count+1
        return count

print(countword())


