class Lexer():
    _operator_list = ['!*#+','~∧⊻∨','¬&⊕ǀ','!&#|']
    _operator = _operator_list[0]
    _variables = []

    def _reset_static_var(self):
        self._variables.clear()

    @property
    def operator(self):
        return self._operator
    
    @operator.setter
    def operator(self,n):
        if(n >= 0 and n <= len(self._operator_list)):
            self._operator = self._operator_list[n]
        else:
            raise Exception("Invalid operator set")

    @property
    def variables(self):
        return self._variables

    @variables.setter
    def variables(self,var):
        self._variables.append(var)