# 2022-02-28, generator of 
from math import ceil, floor, log10
import sys

glb_n = 4
# Results from https://en.wikipedia.org/wiki/Sums_of_three_cubes
STC_still_unknowns_1000 = [114, 390, 627, 633, 732, 921, 975]


def STC(dir, minInt, maxInt):
    # sum of three cubes
    for i in range(minInt, maxInt+1):
        with open('./'+dir+'/'+str(i).rjust(glb_n, '0')+'.smt2', 'w') as f:
            f.write("(set-info :smt-lib-version 2.6)\n")
            f.write("(set-logic QF_NIA)\n")
            f.write("(set-info :source |\n" +
                "Problem: Sum of three cubes\n" +
                "Generate by: Fuqi Jia, Minghao Liu, Pei Huang, Feifei Ma, Jian Zhang\n" + 
                "Generated on: 2022-02-28\n" +
                "Generator: https://github.com/MRVAPOR/math_puzzles_smtlib_generator\n" +
                "Application: Solving hard mathematical problems\n" + 
                "Target solver: z3\n" +
                "|)\n")
            f.write("(set-info :license \"https://creativecommons.org/licenses/by/4.0/\")\n")
            f.write("(set-info :category \"crafted\")\n")
            f.write("(set-info :status " + ("unknown" if i in STC_still_unknowns_1000 else ("unsat" if (i % 9 == 4 or i % 9 == 5) else "sat")) + ")\n")
            f.write("(declare-fun x () Int)\n")
            f.write("(declare-fun y () Int)\n")
            f.write("(declare-fun z () Int)\n")
            f.write("(assert (= (+ (* x x x) (* y y y) (* z z z)) " + str(i) + "))\n")
            f.write("(check-sat)\n")
            f.write(";;(get-assignment)\n")
            f.write(";;(get-model)\n")
            f.write("(exit)\n")


def RTA(dir, minInt, maxInt):
    # relaxed taxicab number
    for i in range(minInt, maxInt+1):
        with open('./'+dir+'/RTA_'+str(i).rjust(glb_n, '0')+'.smt2', 'w') as f:
            f.write("(set-info :smt-lib-version 2.6)\n")
            f.write("(set-logic QF_NIA)\n")
            f.write("(set-info :source |\n" +
                "Problem: Relaxed taxicab number\n" +
                "Generate by: Fuqi Jia, Minghao Liu, Pei Huang, Feifei Ma, Jian Zhang\n" + 
                "Generated on: 2022-02-28\n" +
                "Generator: https://github.com/MRVAPOR/math_puzzles_smtlib_generator\n" +
                "Application: Solving hard mathematical problems\n" + 
                "Target solver: z3\n" +
                "|)\n")
            f.write("(set-info :license \"https://creativecommons.org/licenses/by/4.0/\")\n")
            f.write("(set-info :category \"crafted\")\n")
            f.write("(set-info :status sat)\n")
            f.write("(declare-fun t () Int)\n")
            for j in range(i):
                f.write("(declare-fun x"+ str(j) +" () Int)\n")
                f.write("(declare-fun y"+ str(j) +" () Int)\n")
                
            for j in range(i):
                x = "x" + str(j)
                y = "y" + str(j)
                f.write("(assert (= (+ (* "+x+" "+x+" "+x+") (* "+y+" "+y+" "+y+")) t))\n")
            
            for j in range(i):
                x_j = "x" + str(j)
                y_j = "y" + str(j)
                for k in range(j+1, i):
                    x_k = "x" + str(k)
                    y_k = "y" + str(k)
                    f.write("(assert (distinct "+ x_j +" "+ x_k +"))\n")
                    f.write("(assert (distinct "+ x_j +" "+ y_k +"))\n")
                    f.write("(assert (distinct "+ y_j +" "+ x_k +"))\n")
                    f.write("(assert (distinct "+ y_j +" "+ y_k +"))\n")
            
            f.write("(check-sat)\n")
            f.write(";;(get-assignment)\n")
            f.write(";;(get-model)\n")
            f.write("(exit)\n")


def TA(dir, minInt, maxInt):
    # relaxed taxicab number
    for i in range(minInt, maxInt+1):
        with open('./'+dir+'/TA_'+str(i).rjust(glb_n, '0')+'.smt2', 'w') as f:
            f.write("(set-info :smt-lib-version 2.6)\n")
            f.write("(set-logic QF_NIA)\n")
            f.write("(set-info :source |\n" +
                "Problem: Taxicab number\n" +
                "Generate by: Fuqi Jia, Minghao Liu, Pei Huang, Feifei Ma, Jian Zhang\n" + 
                "Generated on: 2022-02-28\n" +
                "Generator: https://github.com/MRVAPOR/math_puzzles_smtlib_generator\n" +
                "Application: Solving hard mathematical problems\n" + 
                "Target solver: z3\n" +
                "|)\n")
            f.write("(set-info :license \"https://creativecommons.org/licenses/by/4.0/\")\n")
            f.write("(set-info :category \"crafted\")\n")
            f.write("(set-info :status sat)\n")
            f.write("(declare-fun t () Int)\n")
            for j in range(i):
                f.write("(declare-fun x"+ str(j) +" () Int)\n")
                f.write("(declare-fun y"+ str(j) +" () Int)\n")
                
            for j in range(i):
                x = "x" + str(j)
                y = "y" + str(j)
                f.write("(assert (= (+ (* "+x+" "+x+" "+x+") (* "+y+" "+y+" "+y+")) t))\n")

            for j in range(i):
                x = "x" + str(j)
                y = "y" + str(j)
                f.write("(assert (>= "+ x +" 0))\n")
                f.write("(assert (>= "+ y +" 0))\n")
            
            for j in range(i):
                x_j = "x" + str(j)
                y_j = "y" + str(j)
                for k in range(j+1, i):
                    x_k = "x" + str(k)
                    y_k = "y" + str(k)
                    f.write("(assert (distinct "+ x_j +" "+ x_k +"))\n")
                    f.write("(assert (distinct "+ x_j +" "+ y_k +"))\n")
                    f.write("(assert (distinct "+ y_j +" "+ x_k +"))\n")
                    f.write("(assert (distinct "+ y_j +" "+ y_k +"))\n")
            
            f.write("(check-sat)\n")
            f.write(";;(get-assignment)\n")
            f.write(";;(get-model)\n")
            f.write("(exit)\n")


def MSName(s):
    if(s=="MS"):
        return "Magic sqaure of squares"
    elif(s=="SC"):
        return "Semi-magic sqaure of cubes"
    elif(s=="MC"):
        return "Magic sqaure of cubes"
    elif(s=="SQ"):
        return "Semi-magic sqaure of fourth power"
    elif(s=="MQ"):
        return "Magic sqaure of fourth power"
    elif(s=="SF"):
        return "Semi-magic sqaure of fifth power"
    elif(s=="MF"):
        return "Magic sqaure of fifth power"
    else:
        sys.exit(1)


# Results from http://www.multimagie.com/
MS_results = {
    "MS":{
        0: "sat", 1: "sat", 
        2: "unsat", 3: "unknown", 4: "sat", 5: "sat", 6: "sat",
        7: "sat", 8: "sat", 9: "sat", 10: "sat", 11: "sat", 12: "sat"
    },
    "SC":{
        0: "sat", 1: "sat", 
        2: "unsat", 3: "unknown", 4: "sat", 5: "sat", 6: "sat",
        7: "sat", 8: "sat", 9: "sat", 10: "sat", 11: "sat", 12: "sat"
    },
    "MC":{
        0: "sat", 1: "sat", 
        2: "unsat", 3: "unsat", 4: "unknown", 5: "unknown", 6: "unknown",
        7: "sat", 8: "sat", 9: "sat", 10: "sat", 11: "sat", 12: "sat"
    },
    "SQ":{
        0: "sat", 1: "sat", 
        2: "unsat", 3: "unknown", 4: "sat", 5: "unknown", 6: "unknown",
        7: "unknown", 8: "sat", 9: "sat", 10: "unknown", 11: "unknown", 12: "sat"
    },
    "MQ":{
        0: "sat", 1: "sat", 
        2: "unsat", 3: "unsat", 4: "unknown", 5: "unknown", 6: "unknown",7: "unknown", 
        8: "unknown", 9: "unknown", 10: "unknown", 11: "unknown", 12: "unknown"
    },
    "SF":{
        0: "sat", 1: "sat", 
        2: "unsat", 3: "unknown", 4: "unknown", 5: "unknown", 6: "unknown",7: "unknown", 
        8: "unknown", 9: "unknown", 10: "unknown", 11: "unknown", 12: "unknown"
    },
    "MF":{
        0: "sat", 1: "sat", 
        2: "unsat", 3: "unsat", 4: "unknown", 5: "unknown", 6: "unknown",7: "unknown", 
        8: "unknown", 9: "unknown", 10: "unknown", 11: "unknown", 12: "unknown"
    }
}


def power(var, power):
    num = 2
    if(power=='S'): num = 2 # square
    elif(power=='C'): num = 3 # cube
    elif(power=='Q'): num = 4 # fourth power
    elif(power=='F'): num = 5 # fifth power
    
    ret = "(* "
    for _ in range(num):
       ret += var + " "
    return ret[:-1] + ") "

def MS(dir, mode, minInt, maxInt):
    # four kinds of magic squares
    s = MSName(mode)
    res = MS_results[mode]
    for i in range(minInt, maxInt+1):
        with open('./'+dir+'/'+ mode + "_" +str(i).rjust(glb_n, '0')+'.smt2', 'w') as f:
            f.write("(set-info :smt-lib-version 2.6)\n")
            f.write("(set-logic QF_NIA)\n")
            f.write("(set-info :source |\n" +
                "Problem: " + s + "\n" +
                "Generate by: Fuqi Jia, Minghao Liu, Pei Huang, Feifei Ma, Jian Zhang\n" + 
                "Generated on: 2022-02-28\n" +
                "Generator: https://github.com/MRVAPOR/math_puzzles_smtlib_generator\n" +
                "Application: Solving hard mathematical problems\n" + 
                "Target solver: z3\n" +
                "|)\n")
            f.write("(set-info :license \"https://creativecommons.org/licenses/by/4.0/\")\n")
            f.write("(set-info :category \"crafted\")\n")
            f.write("(set-info :status " + res[i] + ")\n")
            f.write("(declare-fun t () Int)\n")

            for j in range(i):
                for k in range(i):
                    f.write("(declare-fun x_"+ str(j) + "_" + str(k) +" () Int)\n")
            
            # assertions

            # sum of row elements are the same 
            for j in range(i):
                f.write("(assert (= (+ ")
                for k in range(i):
                    x = "x_"+ str(j) + "_" + str(k)
                    f.write(power(x, mode[1]))

                f.write(") t))\n")

            # sum of column elements are the same     
            for j in range(i):
                f.write("(assert (= (+ ")
                for k in range(i):
                    x = "x_"+ str(k) + "_" + str(j)
                    f.write(power(x, mode[1]))

                f.write(") t))\n")

            
            # sum of diagnal elements are the same not for semi-magic sqaure
            if(mode[0]=='M'):
                # diagnal
                f.write("(assert (= (+ ")
                for j in range(i):
                    x = "x_"+ str(j) + "_" + str(j)
                    f.write(power(x, mode[1]))
                f.write(") t))\n")

                # anti-diagnal
                f.write("(assert (= (+ ")
                for j in range(i):
                    x = "x_"+ str(j) + "_" + str(i-j-1)
                    f.write(power(x, mode[1]))
                f.write(") t))\n")
            
            # all elements are distinct
            for j in range(i):
                for k in range(i):
                    x = "x_"+ str(j) + "_" + str(k)
                    # the same row
                    for n in range(k+1, i):
                        y = "x_"+ str(j) + "_" + str(n)
                        f.write("(assert (distinct "+x +" "+y+"))\n")

                    # next rows
                    for m in range(j+1, i):
                        for n in range(i):
                            y = "x_"+ str(m) + "_" + str(n)
                            f.write("(assert (distinct "+x +" "+y+"))\n")
            
            f.write("(check-sat)\n")
            f.write(";;(get-assignment)\n")
            f.write(";;(get-model)\n")
            f.write("(exit)\n")

if __name__ == "__main__":
    dir = str(sys.argv[1])
    mode = str(sys.argv[2])
    minInt = int(sys.argv[3])
    maxInt = int(sys.argv[4])
    glb_n = floor(log10(maxInt)) + 1

    if mode=="STC":
        assert(minInt>=0)
        assert(maxInt<=1000)
        STC(dir, minInt, maxInt)
    elif mode=="RTA":
        assert(minInt>=0)
        assert(maxInt<=100)
        RTA(dir, minInt, maxInt)
    elif mode=="TA":
        assert(minInt>=0)
        assert(maxInt<=100)
        TA(dir, minInt, maxInt)
    else:
        assert(minInt>=2)
        assert(maxInt<=12)
        MS(dir, mode, minInt, maxInt)
