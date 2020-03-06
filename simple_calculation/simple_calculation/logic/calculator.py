class Calculator:
	"""
    A class used to represent a basic calculator that performs an arithmetic operation on two operands

    ...

    Attributes
    ----------
    operand_1 : int
        An interger value that represents the first operand
    operand_2 : int
        An interger value that represents the first operand
    operation : str
        The string value representing arithmetic operation to be performed on the operands

    Methods
    -------
    calculate_result (operand_1, operand_2, operation)
        Performs the specified operation on the operans and return the result of the operation
    """
	
	def __init__(self, operand_1, operand_2, operation):
		"""
        Parameters
        ----------
		operand_1 : int
			An interger value that represents the first operand
		operand_2 : int
			An interger value that represents the first operand
		operation : str
			The string value representing arithmetic operation to be performed on the operands
        """
		self.operand_1 = operand_1
		self.operand_2 = operand_2
		self.operation = operation


	def calculate_result(self):
		"""
		Performs the specified operation on the operans and return the result of the operation

        If the argument `operand_2` is 0 and `operation` is `%`, then infinity is returned.

        Parameters
        ----------
		operand_1 : int
			An interger value that represents the first operand
		operand_2 : int
			An interger value that represents the first operand
		operation : str
			The string value representing arithmetic operation to be performed on the operands
        """
		
		# If parameter 'operation' is '+' then add the operands 
		if self.operation == '+':
			return self.operand_1 + self.operand_2
			
		# If parameter 'operation' is '-' then sibtract the operands 
		elif self.operation == '-':
			return self.operand_1 - self.operand_2
			
		# If parameter 'operation' is '*' then multiply the operands 			
		elif self.operation == '*':
			return self.operand_1 * self.operand_2
			
		# Finally when parameter 'operation' is '%' then divide the operands 			
		else:
			# Check if the parameter 'operand_2' is 0, if not return result of division, else return infinity 
			try:
				self.operand_1 / self.operand_2
				return self.operand_1 / self.operand_2
			except ZeroDivisionError:
				return float('Inf')	
