from lexer import Lexer
import boolean_operations as op

class Scanner(Lexer):
    def __init__(self):
        self._expected_characters_list = 'abcdefghijklmnopqrstuvwxyz()'

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
        expected_chars = self._expected_characters_list + self.operator
        for c in self.expression:
            if c not in expected_chars:
                raise Exception('Invalid character : '+ c)
        
        #remove redundant brackets

        ##check for double operation symbols
        for i,c in enumerate(self.expression,start=0):
            if c in self.operator:
                if self.expression[i+1] in self.operator[1:]:
                    raise Exception("Invalid syntax at pos[" + str(i) + "] '" + c + self.expression[i+1]+"'")
                if self.expression[i+1] in self._expected_characters_list:
                    return 0

            ##check for number after operator

    def _set_global_variables(self):
        expected_vars = 'abcdefghijklmnopqrstuvwxyz'
        for c in self.expression:
            if c in expected_vars and c not in self.variables:
                self.variables = c
        