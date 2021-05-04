class DpllExpression:
    
    def __init__(self):
        self.noOfVariables=0
        self.checkedVariables=[]
        self.expression=[]
        
    def addCheckedVarible(self,value:int):
        self.checkedVariables.append(value)
        
    def checkInCheckedVariables(self,value:int)-> bool:
        return value in self.checkedVariables
        
    def getExpression(self):
        return self.expression
        
    def setNoOfVariables(self,value):
        self.noOfVariables=value
        
    def getNoOfVariables(self)-> int:
        return self.noOfVariables
    
    def stringToDpllInputConveter(self,expression: list):
        closure=[]
        for item in expression:
            item=item.strip('\n')
            if item:
                val=int(item)
                if val==0:
                  break
                closure.append(val)
        self.expression.append(closure)

def removeClausesContainingTrueLiterals(expression:DpllExpression,partialArgument):
    if len(partialArgument) == 0:
        return
    for closure in expression.getExpression():
        for literal in closure:
            if literal>0 and partialArgument[1]:
                expression.getExpression().remove(closure)
                break
            elif literal < 0 and not(partialArgument[1]):
                expression.getExpression().remove(closure)
                break
    
                
                
def shortenClosuresNotLiterals(expression:DpllExpression,partialArgument):
    if len(partialArgument) == 0:
        return
    for closure in expression.getExpression():
        for literal in closure:
            if literal>0 and not(partialArgument[1]):
                expression.getExpression().remove(closure)
                closure.remove(literal)
                expression.getExpression().append(closure)
                
            elif literal < 0 and partialArgument[1]:
                expression.getExpression().remove(closure)
                closure.remove(literal)
                expression.getExpression().append(closure)

       
            
def checkEmptyClosure(expression:DpllExpression)-> bool:
    for closure in expression.getExpression():
        if len(closure)==0:
            return True
    return False


def checkUnitLiteral(expression:DpllExpression):
    for closure in expression.getExpression():
        if len(closure)==1:
            if closure[0]>0:
                return (True,closure[0],True)
            else:
                return (True,-1*closure[0],False)
    return(False,None,None)
    
    
def choseVariable(expression:DpllExpression)-> int:
    value=expression.getNoOfVariables()
    expression.setNoOfVariables(value-1)
    while expression.checkInCheckedVariables(value):
        value=expression.getNoOfVariables()
        expression.setNoOfVariables(value-1)
    return value
           
      
            
     
def dpllAlgorithm(expression:DpllExpression,partialArgument):
    removeClausesContainingTrueLiterals(expression,partialArgument)
    if len(expression.getExpression())==0:
        return True
    shortenClosuresNotLiterals(expression,partialArgument)
    
    if checkEmptyClosure(expression):
        return False
    
    containUnitClosure,literal,literalValue=checkUnitLiteral(expression)
    if containUnitClosure:
        expression.addCheckedVarible(literal)
        return dpllAlgorithm(expression,(literal,literalValue))
        
    value=choseVariable(expression)
    print(value)
    if dpllAlgorithm(expression,(value,False)):
        return True
    
    return dpllAlgorithm(expression,(value,True))
        
    
    
    