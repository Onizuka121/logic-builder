import sympy 
from sympy.logic.boolalg import truth_table
from texttable import Texttable
from collections import deque


exp_str = input("expression : ");


def get_gray_code(n):
    code = [[0],[1]]
    
    for _ in range(n-1):
        tmp = code[::-1]
        for c in tmp:
            code.append(c)
        j = 0
        while j < len(code):
            d = deque(code[j])
            if j < len(code)/2:
                d.appendleft(0)
            else: 
                d.appendleft(1)
            
            code[j] = list(d)
            j += 1
    print(code) 
    return code
    

def get_modified_tb(table):
    nt = []
    for i in range(len(table)):
        t = 0
        c = len(table[i][0])-1
        for bit in table[i][0]:
            t += bit*(2**c)
            c-=1

        nt.append((t,table[i][1]))

    return nt



def get_k_map(vars,table):
    c = int(len(vars)/2)
    a = get_gray_code(c)
    b = get_gray_code(len(vars)-c)
    print(table)
    print(get_modified_tb(table))

    map = []
    for ia in range(len(a)):
        map.append([])
        for ib in range(len(b)):
            print(a[ia])
    
            #convert a[ia]+b[ib] to integer so its easy to map to table  



def get_tb_from_fromula(formula):
    try:
        f = sympy.sympify(formula)
    except:
        print("[>] invalid formula")
        exit() 
    vars = sorted(list(f.atoms()),key= lambda x: x.name)
    table = list(truth_table(f, vars))

    t = Texttable()

    get_k_map(vars,table)

    vars.append("F")

    t.add_row(vars)

    for inputs, output in table:
        t.add_row(list(inputs) + [1 if output else 0])

    return t.draw()


get_tb_from_fromula(exp_str)


    
    


















    
