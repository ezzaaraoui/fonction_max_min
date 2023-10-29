
def Max(tab):
    return max(tab)


def Min(tab):
    return min(tab)

def inverse(tab):

    t=[]
    for i in range(3,-1,-1):
        t.append(tab[i])
    return t
    



t=[]
for i in range(0,4):
    t.append(float(input(f"donner element de la case {i+1} : ")))

print(inverse(t))