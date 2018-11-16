base_syntax_universe = {}

def evaluate(expression):
    symbols = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    return read_from_tokens(symbols)

def eval(tree):
    symbol = tree[0]
    if symbol == 'define':
        
        #add new definition
        #arg 1 is the new definition
        #arg 2 is what happens when new definition is used
        pass
    elif symbol == '+':
        #add arguments after evaluating
        pass
    elif symbol == 'output':
        #print argument after evaluating
        pass
    elif symbol == 'if':
        #arg 1 is boolean condition
        #arg 2 is what happens if condition is true
        #arg 3 is what happens if condition is false
        pass
    elif symbol == 'do':
        #do a noop then do another thing, evaluates to the other thing
        pass
    elif symbol is int:
        pass
    else:
        #look up what this symbol means
            

def read_from_tokens(symbols):
    symbol = symbols.pop(0)
    if symbol == '(':
        L = []
        while symbols[0] != ')':
            L.append(read_from_tokens(symbols))
        symbols.pop(0) # pop off ')'
        return L
    else:
        return atom(symbol)

def atom(symbol):
    "Numbers become numbers; every other token is a symbol."
    try: return int(symbol)
    except ValueError:
        try: return float(symbol)
        except ValueError:
            return symbol

def repl():
    expression = ''
    while expression != 'q':
        expression = input()
        print(evaluate(expression))
