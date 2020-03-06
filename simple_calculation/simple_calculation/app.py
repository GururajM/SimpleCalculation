from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
import re
from logic.calculator import Calculator


def simple_calculation(request):
	"""
	View function for the simple calculation.
	
	Returns the result of the arithmetic operation on the specified operands.
    """
	
	# Patten to match from the URL, e.g. 3+2
	match_pattern = '^[0-9]+[\+\-\*\%][0-9]+$'
	# Part of the URL to be matched with the pattern
	match_string = request.matchdict['input']
	# Get the match status
	matched = re.match(match_pattern, match_string)
	
	# Check if string matches the pattern 
	if matched:
		# if matched, get the group of numbers and operations [+,-,*,%]
		operands = re.findall('\d+', match_string)
		opeartion = re.findall('[\+\-\*\%]', match_string)[0]
		
		# Create a basic calculator object and get the result of the operation
		calc_object = Calculator(int(operands[0]), int(operands[1]), opeartion)
		result = calc_object.calculate_result()
		del calc_object
		
		# Return the result as JSON
		return {'Result':result}
	else:
		# If not matched, return as 'Incorrect input' as JSON
		return {'Result':'Incorrect input'}



if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('simpleCalculation', '/simpleCalculation/{input}')
        config.add_view(simple_calculation, route_name='simpleCalculation', renderer='json')
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)