import stck

def isInt(e):
    try:
        int(e)
        return True
    except ValueError:
        return False


def isOp(e):
    return "+-*/".find(e) != -1


def pr(e):
    priority = {'+' : 2,
            '-' : 2,
            '/' : 3,
            '*' : 3}
    return priority[e]


def operation(op, rnum, lnum):
    res = {
        '+': float(lnum) + float(rnum),
        '-': float(lnum) - float(rnum),
        '/': float(lnum) / float(rnum),
        '*': float(lnum) * float(rnum)
    }
    return res[op]


def brackets(s):
    l = 0
    r = 0
    for i in s:
        if(i == '('):
            l+=1
        elif(i == ')'):
            r+=1
    return l == r

class Calculator:

    def postfix(inpStr):

        inpStr = inpStr.replace(' ', '')
        i = -1
        outStr = ""
        stackOp = stck.Stack()
        
        while(i < len(inpStr)):
            if(i < len(inpStr)-1):
                i+=1
            else:
                i += 1
                continue
            if((isOp(inpStr[i]) or isInt(inpStr[i]) or inpStr[i] == '(' or inpStr[i] == ')') and brackets(inpStr)):
                if(inpStr[i] == '-' and ((i > 0 and not isInt(inpStr[i-1]) and inpStr[i-1] != ')') or i == 0)):
                    outStr += '-'
                    continue
                if(isInt(inpStr[i])):
                    outStr += inpStr[i]
                    continue
                if(len(outStr) > 0 and outStr[len(outStr)-1] != ' '):
                    outStr += ' '
                if(isOp(inpStr[i])):
                    if(stackOp.isEmpty() or stackOp.peek() == '('):
                        stackOp.push(inpStr[i])
                        continue
                    if(pr(inpStr[i]) > pr(stackOp.peek())):
                        stackOp.push(inpStr[i])
                        continue
                    if(pr(inpStr[i]) <= pr(stackOp.peek())):
                        while(not stackOp.isEmpty() and stackOp.peek() != '(' and pr(inpStr[i]) <= pr(stackOp.peek()) ):
                            outStr += stackOp.pop() + ' '
                        stackOp.push(inpStr[i])
                        continue
                if(inpStr[i] == '('):
                    stackOp.push('(')
                    continue
                if(inpStr[i] == ')'):
                    while(stackOp.peek() != '('):
                        outStr += stackOp.pop() + ' '
                    stackOp.pop()
            else:
                outStr = ''
                break
        if(len(outStr) > 0):
                if(outStr[len(outStr)-1] != ' '):
                    outStr += ' '
                while(not stackOp.isEmpty()):
                    outStr += stackOp.pop() + ' '
        return outStr

    def calc(inpStr):

        stackNum = stck.Stack()

        try:
            outStr = Calculator.postfix(inpStr)
            for i in outStr.split():
                if(isInt(i)):
                    stackNum.push(i)
                elif(isOp(i)):
                    stackNum.push(operation(i, stackNum.pop(), stackNum.pop()))
            return stackNum.peek()
        except Exception as e:
            return e
   
