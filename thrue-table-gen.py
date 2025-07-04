import re
from operator import xor
import sympy 
from sympy.core import Symbol, symbol, sympify
from sympy.logic.boolalg import truth_table
from texttable import Texttable
from sympy.parsing.sympy_parser import parse_expr



#1.accept xor operator
#2.thruth table to formula 


exp_str = input("expression : ");

def get_variables(exp_str): 
    vars = {}
    for c in exp_str:
        if c not in "^~|&":
            vars[c] = Symbol(c)
    
    return vars

def parse_logical_expr(expr_str, variables):
    replacements = {
        r'\bnot\b|~': 'Not',
        r'\band\b|&': 'And',
        r'\bor\b|\|': 'Or',
        r'\bxor\b|\^': 'Xor'
    }

    for pattern, repl in replacements.items():
        expr_str = re.sub(pattern, repl, expr_str)

    return parse_expr(expr_str, evaluate=False, local_dict=variables)

#exp_str = parse_logical_expr(exp_str,get_variables(exp_str))


try:
    f = sympy.sympify(exp_str)
except:
    print("[>] invalid formula")
    exit() 

vars = sorted(list(f.atoms()),key= lambda x: x.name)
table = list(truth_table(f, vars))

t = Texttable()

vars.append("F")
t.add_row(vars)

for inputs, output in table:
    t.add_row(list(inputs) + [1 if output else 0])


print(t.draw())
