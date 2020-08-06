from lexer import Lexer
import boolean_operations as op

class Scanner(Lexer):
    def __init__(self):
        self._expected_characters_list = 'abcdefghijklmnopqrstuvwxyz'
        self._brackets = '()'

    def scan(self,expression):
        self.expression = expression

        self._to_lowercase()
        self._remove_whitespaces()
        
        self._check_size()
        self._check_characters()
        

        self._set_global_variables()

        return self.expression

    def _remove_whitespaces(self):
        self.expression = self.expression.replace(' ','')
    
    def _to_lowercase(self):
        self.expression = self.expression.lower()

    def _check_size(self):
        if len(self.expression) <1 or len(self.expression) > 50:
            raise Exception("Invalid number of characters")

    def _check_characters(self):
        expected_chars = self._expected_characters_list + self._brackets + self.operator

        bracket_open = []
        bracket_close = []
        brackets = {}

        ##check for double operation symbols
        if self.expression[0] in self.operator[1:]:
            raise Exception("Invalid syntax at pos[0] : '" +self.expression[0]+ "'")

        if self.expression[-1] in self.operator :
            raise Exception("Invalid syntax at pos["+str(len(self.expression))+"] : '"+ self.expression[-1]+"'")

        for i,c in enumerate(self.expression):
            if i < len(self.expression)-1:
                c2 = self.expression[i+1]
            
            if c not in expected_chars:
                raise Exception('Invalid characters : '+ c + "at pos[" + str(i) + "] '")

            elif c in self._expected_characters_list and c2 in self._expected_characters_list:
                raise Exception("Invalid characters : '"+ c+c2 + "' at pos[" + str(i) + "," + str(i+1)+"]")

            if c in self.operator:
                if c2 in self.operator[1:]:
                    raise Exception("Invalid syntax at pos[" + str(i) + "] '" + c + self.expression[i+1]+"'")
            #check for brackets        
            elif c == '(':
                bracket_open.append(i)
            elif c == ')':
                bracket_close.append(i)

            if(len(bracket_open) > 0 and len(bracket_close) > 0):
                brackets[bracket_open.pop()] = bracket_close.pop()

        if len(bracket_open) != len(bracket_close):
            raise Exception("Invalid syntax")
                
        print(brackets)

    def _set_global_variables(self):
        for c in self.expression:
            if c in self._expected_characters_list and c not in self.variables:
                self.variables = c
        