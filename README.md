# DPLL-Solution-Finder

This code solve the SAT problem using the DPLL solution,here we have to give CNF form problem in a text file in the following way.
For Example: {{!B A !C}{B A !C}{!B !A !C}{B}{C}} will be written in SAT instance in DIMACS CNF input format.

p cnf 3  5
-2 1 -3
2 1 -3
-2 -1 -3
2
3
 
First line contain the  'p cnf <no of variables>  <no of lines>'
All variable has a unique no and not is signify by the negative sign
  
run programme using

python3 Dpll.py  '<data input file name>' 
