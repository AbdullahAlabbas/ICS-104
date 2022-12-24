def main():
    
    firstFile = input("Enter first file name : ")
    listOfFirstFile = readInput(firstFile)
    secondFile = input("Enter second file name: ")
    listOfsecondFile = readInput(secondFile)
    
    if len(listOfFirstFile) == len(listOfsecondFile):
        answer = dotProduct(listOfFirstFile,listOfsecondFile)
        print(answer)
    else:
        print("The two sequences numbers are not equal in length.")
    
    
    
def readInput(filename):
    try:
        listOfNumbers = []
        infile = open(filename , "r")
        for line in infile:
            line = line.rstrip("\n")
            listOfNumbers.append(line)
   
        infile.close()
        return listOfNumbers
    except FileNotFoundError:
        return "Error: the input file:",filename," is not found"
    
    
def dotProduct(list1,list2):
    
    sum = 0
    for numbers in range(len(list1)):
        sum = sum + (float(list1[numbers]) * float(list2[numbers]))
    
    return sum
main()