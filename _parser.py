import boolean_operations as op
from lexer import Lexer

class Parser(Lexer):
    def __init__(self, expression):
        self.expression = expression

    def parse(self, values):

        self.operations = {self.operator[0]:op.not_,
              self.operator[1]:op.and_,
              self.operator[2]:op.xor_,
              self.operator[3]:op.or_
              }

        expression = self._replace_variables(values)

        return self._evaluate(expression)

    def _replace_variables(self,values):
        expr = list(self.expression)

        for c in range(len(expr)):
            for v in range(len(self.variables)):
                if expr[c] == self.variables[v]:
                    expr[c] = values[v]

        return expr

    def _is_number(self,x):
        if x in [0,1]:
            return True
        else: return False 

    def _evaluate(self,expr):
        eq = list(expr)
        i = 0
        while len(eq)>1:
            c = str(eq[i])
            if(c == '(' and eq[i+2] == ')') :
                del eq[i+2]
                del eq[i]
                i = 0
            elif c in self.operator :
                pc = eq[i-1]
                nc = eq[i+1]
            
                if self._is_number(nc) and c == self.operator[0]:
                    eq[i] = self.operations[eq[i]](pc,nc)
                    del eq[i+1]
                    i = 0
                elif self._is_number(pc) and self._is_number(nc):
                    eq[i] = self.operations[eq[i]](pc,nc)
                    del eq[i+1]
                    del eq[i-1]
                    i= 0
            
            i += 1
            if(i>=len(eq)):
                i=0
            
            
        if len(eq) > 1:
            raise Exception("erro")
    
        return eq[0]
