## This program stores the data of students in a file. ,And you are able to modify,remove and search the data

def main():
    # This dictionary will work as the database for all information
    studentData = {}
    # A loop to ask the user for requested task untill the user terminates the program
    while True:
        # Display menu to user
        displayMenu()
        # Ask user for choice from menu
        choice = input("Choose a number: ")
        # Add
        if choice == "1":
            # Read data from  user and store it in "data"
            data = readData(studentData)
            # print a message if id entered already exist (check readData function for more information about returned values)
            if data == 1:
                print("A student with the same id was enterd already")
            # print a message if use enter nothing 
            elif data == 2:
                print("This option cannot be empty")
            # Print a message if a non numerical data was entered where it should have been
            elif data == 3:
                print("Please enter a valid numeriacal value")
            else:
                # Store data in studentData and use the id as key
                studentData[data["id"]] = data
                # Write Data in file
                writeData(studentData)
        # Remove
        elif choice == '2':
            # The spaces variable will work as an indent for the output (Note: that the variable will do the same thing in other positions in the program)
            spaces = 8*" "
            # Show option to user
            print(spaces+"please select an option:")
            print(spaces+"a. by id")
            print(spaces+"b. by student first name")
            print(spaces+"c. return to menu")
            # Ask for option
            choice = input(spaces+"please select an option:").rstrip().lower()
            if choice == "a":
                # Ask user for id
                id = input(spaces+"please enter student id: ").rstrip()
                # Remove student 
                removeById(studentData, id)
            elif choice == "b":
                # Ask user for name
                name = input(spaces+"please enter student first name: ").rstrip().lower()
                # Remove student
                removeByName(studentData,name)
            elif choice!= "c":
                print("Select choice is not available")
            # Write data in file after removal
            writeData(studentData)
        # Modify  
        elif choice == '3':
            # Ask user for id to be modify
            id = input("Please enter studnet id: ")
            # Modify
            modify(id,studentData)
            # Write Data after modifcation
            writeData(studentData)
        # Show Students to user
        elif choice == "4":
            # show students to user
            showStudents(studentData)
        # Display top 5 students by marks
        elif choice == "5":
            # Display students
            displayTop5(studentData)
        # Show students with highest absences
        elif choice == "6":
            displayTopAbsences(studentData)
        # Terminate program
        elif choice == "7":
            print("Bye :)")
            break
        else:
            print("Select option is not available")
        print()
        
       
    
    
    
    
        
## A function that reads data from user
# Arguments : a dictionay where the whole data is stored to validate input
# Returns: returns a dictionary where inputed data is stored
# Error returns: Returns 1 if entered data by user already exists in Argument.
# returns two if user enters nothing for id, first name and family name
# returns 3 if enterd data is not numerical where it should be
def readData(studentData):
    # Create a dictionary where the data will be stored at
    data = {}
    spaces = 8*" "
    # Ask user for id
    data["id"] = input(spaces+"Enter student id: ")
    # Check entered id already exists
    if data["id"] in studentData:
        # Return 1
        return 1
    # Check if user entered something
    if data["id"] == "":
        return 2
    # Ask user for first name
    
    data["first name"] = input(spaces+"Enter student first name: ").rstrip().lower()
    # Check if user entered something
    if data["first name"] == "":
        return 2
    # Ask user for last name
    
    data["family name"] = input(spaces+"Enter student family name: ").rstrip().lower()
    # Check if user entered something
    if data["family name"] == "":
        return 2
    # Ask user for number absences
    data["absences"] = input(spaces+"Enter student number of absences: ").rstrip()
    # Check if entered data is a digit
    if not isNumber(data["absences"]):
        return 3
    # Ask user for exam one grade
    data["exam1"] = input(spaces+"Enter student exam one grade: ").rstrip()
    # Check if entered data is a digit
    if not isNumber(data["exam1"]):
        return 3
    # Ask user for exam two grade
    data["exam2"] = input(spaces+"Enter student exam two grade: ").rstrip()
    # Check if entered data is a digit
    if not isNumber(data["exam2"]):
        return 3
    # Calculate total mark by adding exam1 and 2exam grades
    data["total marks"] = str(int(data["exam2"]) + int(data["exam1"]))
    # Return data read from user
    return data







# A function that removes a student by id
# Arguments : a dictionay where the whole data is stored and the id of the student to be removed
def removeById(studentData, id):
    spaces = 8*" "
    # Check if a student with the same id exists
    if id not in studentData:
        print("No matching id was found")
        return
    # Store student data in "student"
    student = studentData[id]
    # Print student data
    print(2*spaces,"data found with id: %s" %id)
    print(2*spaces,student["first name"],student["family name"],student["absences"],student["exam1"],student["exam2"],student["total marks"])
    # Ask user for confirmation
    choice = input(2*spaces+" write 'yes' to confirm removal or 'no' to return to menu").rstrip().lower()
    if choice == "yes":
        # Remove data
        studentData.pop(id)
    # Check if choice is valid
    elif choice != "no":
        print("Select choice is not available")
        
        


# A function that removes a student by name
# Arguments : a dictionay where the whole data is stored and the name of the student to be removed           
def removeByName(studentData,name):
        spaces = 8*" "
        # A list where all match result ids will be stored
        ids = []
        # Check studentData for match names
        for student in studentData.values():
            if student["first name"] == name:
                # If match was found store its id in 'ids'
                ids.append(student["id"])
        # Check if no match is found
        if not ids:
            # Print a message and return
            print("No matching name was found")
            return
        print(2*spaces,"Data found with name %s" %name)
        # Print all match student data with indexs as choices
        for i in range(len(ids)):
            student = studentData[ids[i]]
            print(2*spaces+" "+str(i+1)+":",end="")
            print(student["first name"],student["family name"],student["absences"],student["exam1"],student["exam2"],student["total marks"])
        # Ask user for choice    
        choice = int(input(spaces+"please select which record to remove: "))
        try:
            # remove student from data 
            studentData.pop(ids[choice-1])
        except:
            # print a message if choice is not valid (out of list range)
            print("selected choice is not available")
      
    
        
 # A function that modifies a student data
# Arguments : a dictionay where the whole data is stored and the id of the student to be removed          
def modify(id,studentData):
    spaces = 8*" "
    # Check if a student with the same id exists
    if id not in studentData:
        print("entered id not availabe")
        return
    # Ask user for the data to be modified
    print(spaces,"a. ID")
    print(spaces,"b. NAME")
    print(spaces,"c. Absences")
    print(spaces,"d. Exam1")
    print(spaces,"e. Exam2")
    print(spaces,"f. Return to Main Menu")
    choice = input(spaces+" "+"Please select a choice: ")
    
    
    if choice == "a":
        # Ask user for id
        new = input(spaces+" "+"please enter new id: ")
        # Check if a student with the same id exists
        if new in studentData and new != id:
            print("entered id already exists in records")
            return
        # Check if no id was entered
        if new =="":
            print("This option cannot be empty")
            return
        # Replace the old id with new id from both the specfic student data and the whole data base
        studentData[id]["id"] = new
        tmp = studentData[id]
        studentData.pop(id)
        studentData[new] = tmp
        
        
    elif choice =="b":
        # Ask user for first name
        new = input(spaces+" "+"please enter new first name: ")
        # Check if no name was entered
        if new =="":
            print("This option cannot be empty")
            return
        # Ask user for second name
        new1 = input(spaces+" "+"please enter new family name: ")
        # Check if no name was entered
        if new1 =="":
            print("This option cannot be empty")
            return
        # replace old name with new name
        studentData[id]["first name"] = new
        studentData[id]["family name"] = new1
        
        
    elif choice == "c":
        # Ask user for number of abseces
        new = input(spaces+" "+"please enter new number of absences: ")
        # Check if no absences was entered
        if new =="":
            print("This option cannot be empty")
            return
        # Check if entered data is a number
        if not isNumber(new):
            print("Please enter a valid numeriacal value")
            return
        # Replace old number of absences with new number of absences
        studentData[id]["absences"] = new
        
    elif choice == "d":
        # Ask user for exam 1 grade
        new = input(spaces+" "+"please enter new exam one grade: ")
        # Check if no grade was entered
        if new =="":
            print("This option cannot be empty")
            return
        # Check if entered data is a number
        if not isNumber(new):
            print("Please enter a valid numeriacal value")
            return
        # Replace old grade with new
        studentData[id]["exam1"] = new
        studentData[id]["total marks"] = str(int(studentData[id]["exam1"]) + int(studentData[id]["exam2"]))
        
        
    elif choice == "e":
         # Ask user for exam 2 grade
        new = input(spaces+" "+"please enter new exam two grade: ")
        # Check if no grade was entered
        if new =="":
            print("This option cannot be empty")
            return
        # Check if entered data is a number
        if not isNumber(new):
            print("Please enter a valid numeriacal value")
            return
        # Replace old grade with new
        studentData[id]["exam2"] = new
        studentData[id]["total marks"] = str(int(studentData[id]["exam1"]) + int(studentData[id]["exam2"]))
    # Check if entered choice is valid
    elif choice != "f":
        print("Selected option is not available")


        
        
# A function that creates a list with pairs of an id and a key
# Arguments : a dictioanary where the data is stored at and a key that you want to associate the ids with
# This function is useful for sorting a data based on a certain key
def associate(data,key):
    # A list where the pairs will be stored at
    list = []
    # Loop through all the data
    for student in data.values():
        
        if key != "first name":
            # Create a list to store pairs of key values and id (value associated with key will have index 0)
            pair = []
            # Append the value associated with key then append the id
            # If the key is not a name turn the value into an intger(This is nesscary for sorting regarding to numbers)
            pair.append(int(student[key]))
            pair.append(student["id"])
        else:
            # Same thing as above without turning the value to an intger since its a name, and we join first and family name for better sorting
            pair = []
            pair.append(student[key]+" "+student["family name"])
            pair.append(student["id"])
        # Append pair to list
        list.append(pair)
    return list        
        
        
        
        
        
        
        
        
        
        
        
# A function that shows the students with the highest absences       
def displayTopAbsences(studentData):
    # Get the list that associates absences with id
    data = associate(studentData,"absences")
    # Display header of table
    displayHeader()
    # Set max to -1
    max = -1
    # Iterate through sorted data from highest to lowest absences
    for pair in sorted(data,reverse = True):
            # Set id to pair[1] since pair 0 is the key value
            id = pair[1]
            # Do this untill the number of absences decreases (since we only want the hightest ones)
            if pair[0] < max:
                break
            # Print data
            print("%-15s %-15s %-15s %-15s %-15s %-15s %s"%(studentData[id]["id"],studentData[id]["first name"],studentData[id]["family name"],studentData[id]["absences"],studentData[id]["exam1"],studentData[id]["exam2"],studentData[id]["total marks"]))
            # Set max to value associated with key
            max = pair[0]





# A function that shows sorted students data
# The function takes the student data as arguement
def showStudents(studentData):
        # A dictionary where every choice selected from user is associated with a certain key
        choices= {"a":"id","b":"first name","c":"total marks","d":"absences"}
        spaces = 8*" "
        # Ask user for choice
        print(spaces,"a. Sort by ID")
        print(spaces,"b. Sort by Name")
        print(spaces,"c. Sort by Total Marks")
        print(spaces,"d. Sort by Absences")
        print(spaces,"e. Return to Main Menu")
        choice = input("please select a choice: ").rstrip().lower()
        if choice == "e":
            return
        # Check if choice is invalid
        if choice not in choices:
            print("Selected option is unavailable")
            return
        # Get a key based on choice
        key = choices[choice]
        # Get a list that associated id with key
        data = associate(studentData,key)
        # Display header for table
        displayHeader()
        # Iterate for every pair in sorted data
        for pair in sorted(data):
            # Get id
            id = pair[1]
            # Print Data
            print("%-15s %-15s %-15s %-15s %-15s %-15s %s"%(studentData[id]["id"],studentData[id]["first name"],studentData[id]["family name"],studentData[id]["absences"],studentData[id]["exam1"],studentData[id]["exam2"],studentData[id]["total marks"]))

    
    
    
    
    
# A function to display the header of the table
def displayHeader():
    # print the top 110 dashes (the number of dashes was choosen after a process of trial and error)
    print("-"*110)
    # print the title for each column 
    # Note that between number of characters the frst character in the column and the last chararter in the next column is 15
    # This was done to give it a tablur look
    print("%-15s %-15s %-15s %-15s %-15s %-15s %s" %("id","first name","family name","absences","exam 1 grade","exam 2 grade","total marks"))
    # print the bottom 110 dashes
    print("-"*110) 
    
    
 # A function that writes data to a file  
def writeData(data):
    # Open a file to write at
    file = open("data.txt",'w')
    # Write table Header
    file.write("-"*110+"\n")
    file.write("%-15s %-15s %-15s %-15s %-15s %-15s %s \n" %("id","first name","family name","absences","exam 1 grade","exam 2 grade","total marks"))
    file.write("-"*110+"\n")
    # Write every student in the arguement
    for student in data.values():
        file.write("%-15s %-15s %-15s %-15s %-15s %-15s %s \n"%(student["id"],student["first name"],student["family name"],student["absences"],student["exam1"],student["exam2"],student["total marks"]))
    # Close file   
    file.close()

    
    
    
    
    
    
    
# A function that check if a variable in a number 
def isNumber(num):
    try:
        # Check if int() function doesnt raise any errors
        int(num)
        #  Return true if not
        return True
    except:
        # Return false if it raises an error
        return False
    
# A function that displays the top 5 students with the highest total marks   
def displayTop5(studentData):
    # Get a list that associated id with total marks
    data = associate(studentData,"total marks")
    # Set count to zero
    count = 0
    # Display header of table
    displayHeader()
    # Iterate to through sorted data from highest to lowest total marks
    for pair in sorted(data,reverse = True):
        # Display students untill the count is 5 (Only show 5 students)
        if count != 5:
            count +=1
            # Get id of student
            id = pair[1]
            print("%-15s %-15s %-15s %-15s %-15s %-15s %s"%(studentData[id]["id"],studentData[id]["first name"],studentData[id]["family name"],studentData[id]["absences"],studentData[id]["exam1"],studentData[id]["exam2"],studentData[id]["total marks"]))
        
    
    
        
        
        
        
        
        
# A function that dispalys the main menu        
def displayMenu():
    print(8*" "+"USER MENU")
    print("1- Adding Students to a class")
    print("2- Removing students from a class")
    print("3- Modifying student information")
    print("4- Showing all students")
    print("5- Showing the top 5 students")
    print("6- Showing students with the largest number of absences ")
    print("7- Terminating a program")
    
    
    
main()