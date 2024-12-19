"""
Roman Numbers
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500 
M = 1000
"""
s = 'MCMXCIV' #Input
roman_numbers = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000} #Tuple keeps Roman numbers and their integer values
given_number = list(s)  #   The list() function splits a string input into individual characters, one by one.
print(given_number)
output = 0
i= 0  


while i < len(given_number):
    if i == len(given_number) + 1:
        break
    else:
        try:
            if roman_numbers.get(given_number[i]) >= roman_numbers.get(given_number[i+1]):
                output += roman_numbers.get(given_number[i])
            else:
                output -= roman_numbers.get(given_number[i])
        except:
            output += roman_numbers.get(given_number[i])    
    i += 1

print(output)            
