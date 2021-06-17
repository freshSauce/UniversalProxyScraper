import re
import string
digs = string.digits + string.ascii_letters

class Deofuscator:
    def __init__(self, p, r, o, x, y, s) -> None:
        """
        Parameters
        ----------
        p, r, o, x, y, s : str
            Data that will be used for proxy's ports deofuscation

        Return
        ------
        None : None
        """
        self.p = p
        self.r= int(r)
        self.o = int(o)
        self.x = eval(x)
        self.y = int(y)
        self.s = eval(s)
        

    def int2base(self, x, base):
        if x < 0:
            sign = -1
        elif x == 0:
            return digs[0]
        else:
            sign = 1

        x *= sign
        digits = []

        while x:
            digits.append(digs[int(x % base)])
            x = int(x / base)

        if sign < 0:
            digits.append('-')

        digits.reverse()

        return ''.join(digits)

    def Anonymous(self, p, r, o, x, y, s):
        def y(c):
            if c < r:
                val = ''
            else:
                val = y(int(c) / int(r))


            if c % r > 35:
                val_2 = chr(c + 29)
            else:
                val_2 = self.int2base(c, 36)
            variable = str(val) + str(val_2)
            return variable

        if True:
            while o:
                o -= 1
                s[y(o)] = x[o] if x[o] else y(o) if y(o) else False
                
        
        p_processed = p.split(';')[:-1]
        
        to_exec = list()

        for i in p_processed:
            splited = i.split('=')
            first = s[splited[0]]

            second_split = splited[1].split('^')
            if len(second_split) == 2:
                second = s[second_split[0]]
                third = s[second_split[1]]

                second = f'{second} ^ {third}'
            else:
                second = second_split[0]
            
            final = f'{first} = {second}'
            
            to_exec.append(final)
        
        final = '\n'.join(to_exec)

        exec(final, globals())
        return True

    def setup(self, expression):
        expression = expression.replace('))', ')')
        return str(eval(expression))

    def deofuscator(self, expressions):
        self.Anonymous(self.p, self.r, self.o, self.x, self.y, self.s)
        expressions = expressions.split('+')
        done = ''.join([self.setup(x) for x in expressions])

        return done







