import sympy 
from sympy.logic.boolalg import truth_table
from texttable import Texttable


#1.accept xor operator
#2.thruth table to formula 



exp_str = input("expression : ");


try:
    f = sympy.sympify(exp_str)
except:
    print("[>] invalid formula")
    exit() 

vars = list(f.atoms())
table = list(truth_table(f, vars))

t = Texttable()

vars.append("F")
t.add_row(vars)

for inputs, output in table:
    t.add_row(list(inputs) + [1 if output else 0])


print(t.draw())
