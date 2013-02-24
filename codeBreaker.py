import unittest
import random

#code length for generation
code_length=4
colours=['R', 'A', 'M', 'V', 'N', 'I']

def generate_security_code(length, dict):
  sec_code = []
  for i in range(0,length):
    sec_code.append(dict[random.randrange(0, len(dict))])
  return sec_code
  
def check_code(security, guess):
  x=0
  ast=0
  for i in range(0, len(security)):
    if (guess[i]==security[i]):
      x+=1
    elif security.count(guess[i]) > 0:
      ast+=1
  return 'X'*x + '*'*ast
  
  
def test(expected, security, code): 
    output = check_code(security, code) 
    assert expected == output
    print output, "is the outut for ", code ,"over " , security
    

test("X*", ['R','A','N','I'], ['Y','N','Y','I'])
test("XX", ['R','A','N','I'], ['R','M','V','I'])
test("X**", ['N','R','R','I'], ['R','R','V','N'])
    
if __name__ == '__main__':
  #print str(generate_security_code(code_length, colours))
  unittest.main()