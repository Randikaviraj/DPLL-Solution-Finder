import sys


class DpllExpression:
    
    def __init__(self):
        self.noOfVariables=0
        self.expression=[[]]
        
    def setNoOfVariables(self,value):
        self.noOfVariables=value
        
    def getNoOfVariables(self)-> int:
        return self.noOfVariables
    
    def stringToDpllInputConveter(self,expression: list):
        closure=[]
        for item in expression:
            item=item.strip('\n')
            closure.append(item)
        self.expression.append(closure)
              
         



if __name__ =="__main__":
    
    try:
        dplE=DpllExpression()
        with open(sys.argv[1],"r") as file:
            print(f"{sys.argv[1]} Reading..")
            line=file.readline()
            noOfVariables=line.split(" ")[2]
            dplE.setNoOfVariables(noOfVariables)
            line=file.readline()
            while line:
                list=line.split(" ")
                dplE.stringToDpllInputConveter(list)
                line=file.readline()
    except Exception as e:
        print(e)
        print('Invalid no of Arguments :: python Dpll.py <filename>')