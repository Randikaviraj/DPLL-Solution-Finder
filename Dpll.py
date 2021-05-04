from Dpllfunc import dpllAlgorithm,DpllExpression
import sys
import time




if __name__ =="__main__":
    try:
        dplE=DpllExpression()
        with open(sys.argv[1],"r") as file:
            print(f"{sys.argv[1]} Reading..")
            line=file.readline()
            noOfVariables=line.split(" ")[2]
            dplE.setNoOfVariables(int(noOfVariables))
            line=file.readline()
            while line:
                list=line.split(" ")
                dplE.stringToDpllInputConveter(list)
                line=file.readline()
            print('Algorithm Started::')
            seconds = time.time()
            print('Answer to SAT problem :'+str(dpllAlgorithm(dplE,tuple())))
            seconds = seconds-time.time()
            print('Finished::')
            print('Running Time in second'+str(seconds))
    except Exception as e:
        print(e)
        print('Invalid no of Arguments :: python Dpll.py <filename>')