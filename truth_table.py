from scanner import Scanner
from _parser import Parser
from lexer import Lexer
import math

class TruthTable(Lexer):
    def __init__(self,expression):
        self.expression = expression
        self.var = []
        self.table = []
        self._create(expression)

    def _create(self,expression):
        parser = Parser(Scanner(expression))

        self.var = self.variables.copy()

        var_len = len(self.var)
        values = []
        for i in range(var_len):
            values.append(0)
            
        for i in range(0,int(math.pow(2,var_len))):
            for j in range(0,var_len):
                values[var_len - j - 1] = int((i//math.pow(2,j))%2)
            result = parser.parse(values)
            tmp = values.copy()
            tmp.append(result)
            self.table.append(tmp)

        self._reset_static_var()

    def print(self):
        print("[S] = " + self.expression.upper())
        print()
        print(' '+'  '.join(self.var).upper() + ' [S]')
        for l in self.table:
            print(l)
        print()


if __name__ == "__main__":
    #debug
    while(1):
        try:
            TruthTable(input("Expression: ")).print()
        except:
            break
    
        