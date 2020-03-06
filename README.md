# SimpleCalculation

simple Pyramid web application that exposes result of an arithmetic expression provided in the URL as JSON endpoint.

# Features

The project is a simple calculation application that performs the basic arithmetic operation on two opearnds. The operands and the operation are provided as a single expression in the URL, e.g. http://localhost:6543/simpleCalculation/10-45. In the URL the last bit represents the arithmetic expression, i.e. 10-45. The four basic arithmetic supported are {+, -, *, %}. 

Limitations: The application currently only takes into account positive integer numbers.
 
 # Examples
 
 1. http://localhost:6543/simpleCalculation/3+2   output: {"Result": 5}
 
 2. http://localhost:6543/simpleCalculation/10-45   output: {"Result": -35}
 
 3. http://localhost:6543/simpleCalculation/2*5   output: {"Result": -10}
 
 4. http://localhost:6543/simpleCalculation/3%2   output: {"Result": 1.5}
 
 5. http://localhost:6543/simpleCalculation/3%0   output: {"Result": infinity} 
 
 
