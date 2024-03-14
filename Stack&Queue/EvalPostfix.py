from ArrayStack import ArrayStack


def evalPostfix( expr ):
    s = ArrayStack(100)
    for token in expr :
        if token in "+-*/" :
            val2 = s.pop()
            val1 = s.pop()
            if   (token == '+'): s.push(val1 + val2)
            elif (token == '-'): s.push(val1 - val2)
            elif (token == '*'): s.push(val1 * val2)
            elif (token == '/'): s.push(val1 / val2)
        else :
            s.push( float(token) )

    return s.pop()

