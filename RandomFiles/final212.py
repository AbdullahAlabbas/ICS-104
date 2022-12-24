def main():
    try:
        nameOfFile = input("Enter the name of the file : ")
        infile = open(nameOfFile , "r")
        print("id    Average")
        for line in infile:
            id = line.split()[0]
            scores = line.split()[1:]
            print(id , compAvg(scores))
    
    except FileNotFoundError:
        print("File Not Found.")
        
def compAvg(scores):
    sum = 0
    for number in scores:
        sum += float(number)
    Avg = sum / len(scores)
    return "%.2f" % Avg

main()