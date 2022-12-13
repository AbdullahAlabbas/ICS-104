# This program simulates the supermarket system by showing, adding, removing, modifying and sorting different kinds of products.
# The information of the system will be stored inside a file “store.txt” where each line in the file represents a unique product inside the supermarket.
# We rewrite the entire "store.txt" file each time we do a task which resulted in a large code.

def main():      # This function handles most of the work of other functions. It is considered as the main interface of the program.
    
    try:
        while True:
            projectMenu()
            userChoice = input("Enter your choice: ") # Also, we called each function for its specified purpose. We made sure that each function has a name
                                                    # that describes its job.
            if userChoice == "1":
                productInfo()
                
            elif userChoice == "2":
                searchProduct()
                
            elif userChoice == "3":
                addProduct()
                
            elif userChoice == "4":
                removingProduct()
                
            elif userChoice == "5":
                modifyProduct()
                
            elif userChoice == "6":
                filterByPrice()
                
            elif userChoice == "7": # To Exit
                print("The Application Closed Successfully.")
                quit()
            
            else:
                print("You entered an invalid option.")   # This case when the user inputs a choice that is not included in the menu.
    except FileNotFoundError:
        print("The file does not exist.")
        main()
    
def projectMenu(): # This function designs the menu interface.
    numberOfdashes = 31
    print("┌" + "─" * numberOfdashes + "┐") 
    print("│" +" Supermarket Management System " + "│")
    print("└" + "─" * numberOfdashes + "┘")

    print("┌" + "─" * numberOfdashes + "┐") 
    print("│  1. Print products info       │")
    print("│  2. Search a product          │")
    print("│  3. Add a product             │")
    print("│  4. Remove a product          │")
    print("│  5. Modify a product          │")
    print("│  6. Filter by Price           │")
    print("│  7. Exit                      │")
    print("└" + "─" * numberOfdashes + "┘")
    print("=" * numberOfdashes) 


def productInfo(): # This function is going to Show all the information of all products (id, name, price, quantity, discount).

    totalProducts = 1
    txtList = []
    csvFile = open("store.txt", "r")  # We used this peice of code several times in our code, and its job is to take every line in the "store.txt" file
    for line in csvFile:              # and convert it to a list so we can easily deal with it.
        wordList = line.split(",")      
        for word in wordList:
            if "\n" in word:         
                totalProducts +=1         # We couldn't use the makingList() function because we need to count the total number of products.
                word = word.replace("\n","")
                txtList.append(word)
            else:
                txtList.append(word)

    productID = 0      # These are in indecies of each product's information.
    productName = 1
    productPrice = 2
    productQuantity = 3
    productDiscount = 4
    print("\n\nTotal", totalProducts,"products:" )
    print("-" * 46) # 46 is the number of dashes. No need to store it in a variable because we're only going to use it once.
    while True:
        try:
            print("Id:          ", txtList[productID])
            print("title:      ", txtList[productName])
            print("price:      ", txtList[productPrice], "$")
            print("quantity:   ", txtList[productQuantity])
            print("discount:   ", txtList[productDiscount])
            print("-" * 46)
            productID += 5    # Now we increment each index by 5 because 5 is the number between each ID, Name.... etc. and the other.
            productName +=5
            productPrice += 5
            productQuantity += 5
            productDiscount +=5
        except IndexError:
            break
        
        finally:
            csvFile.close()

def searchProduct(): # This function offers some options to choose from. Each option takes a specific peice of information and searches for it in the file,
    print("\nChoose an option") # then it prints the whole information of the product.
    print("=" * 31) # Again, 31 is the number of dashes in the menu's interface.
    print("  1. Search by id")
    print("  2. Search by name")
    print("  3. Return to Main Menu")   
    print("=" * 31)

    searchChoice = input("Enter your choice: ")
    txtList = makingList()
    position = 0
    count = 0

    if searchChoice == "1": # This choice depends on the ID of the product.
    
        idNumber = input("Enter the id: ") 
        
        for word in txtList:
            word = word.lstrip() # We used the function lstrip() because there is a space on the left of the inputs e.g [" 123"].
            if word.startswith(str(idNumber)): # We used the function startswith() because we might search for a part of a product's name
                count +=1                      # to also show other products that might have the same starting letters.
        
        print()
        print("Matched products "+ "(" + str(count) + ")") # We made it as a string because we don't want any spaces.
        print("=" * 31)        
        if count == 0:
            print("This item doesn't exist ")  # Because when there is no product satrting with some letters detected, the count variable will not be incremented.
        
        for word in txtList:
            word = word.lstrip()
            if word == idNumber:
                
                print("Id:          ", txtList[position])
                print("title:      ", txtList[position + 1])
                print("price:       ", float(txtList[position + 2]), "$")
                print("quantity:   ", txtList[position + 3])
                print("discount:   ", txtList[position + 4])
                print("-" * 46)
                break
            else:
                position +=1
    elif searchChoice == "2": # This statement is smilar to searchChoice "1", except that it depends on the name of the product.

        nameOftheProduct = input("Enter the name: ")
               
        for word in txtList:
            word = word.lstrip()
            if word.startswith(nameOftheProduct):
                count +=1
            
        print()
        print("Matched products "+ "(" + str(count) + ")")
        print("=" * 31)
        if count == 0:
            print("This item doesn't exist ")
            
        for word in txtList:
            word = word.lstrip()
            if word.startswith(nameOftheProduct):
            
                print("Id:          ", txtList[position -1])
                print("title:      ", txtList[position])
                print("price:       ", float(txtList[position + 1]), "$") # It is a float in the sample run.
                print("quantity:   ", txtList[position + 2])
                print("discount:   ", txtList[position + 3])
                print("-" * 46)
                
            position +=1
        
    elif searchChoice == "3":
        main() # Returns to the main menu.
        
        
    else:
        print("Invalid Option.")
                
                
def addProduct(): # This function adds a new product to the "store.txt" file. It takes the ID, name, price, quantity, and discount of the products.

    addingProduct = []
    csvFile = open("store.txt", "r")
    for line in csvFile:
        wordList = line.split(",")      # We can not use makingList() function because we need the \n character.
        for word in wordList:
            addingProduct.append(word)


    productID = input("Enter id: ")

    count = 0

    for word in addingProduct:
        word = word.lstrip() # Same reason as stated before.
        if word.startswith(str(productID)):
            count +=1 # To know if the product is already in the file or not such that if it is already existed, only its quantity will be incremented.
            

    if count == 0:               # The adding of the items starts here.
        addingProduct.append("\n") 
        addingProduct.append(productID)
        addingProduct.append(" ")

        productName = input("Enter name: ")
        addingProduct.append(productName)
        addingProduct.append(" ")


        productPrice = input("Enter price: ")
        addingProduct.append(productPrice)
        addingProduct.append(" ")

        productQuantity = input("Enter quantity: ")
        addingProduct.append(productQuantity)
        addingProduct.append(" ")

        productDiscount = input("Enter discount: ")
        addingProduct.append(productDiscount)

        print("New product was added successfully")

        storeFile = open("store.txt" , "w")

        for word in addingProduct: # We used this peice of code several times in our code. its job is 
            word = word.replace(" ",", ") # to write all the file again because we opened the file for writing "w"
            storeFile.write(word)         # and this "w" clears all of the file's contents.
            
        storeFile.close()      
    
    
    else: # Here is the increment in the quantity of the existed product.
        productQuantity = int(input("Enter quantity: "))
        index = 0
        for id in addingProduct:
            if id == productID:
                oldQuan = addingProduct.pop(index + 3) # +3 is the position of the quantity. We remove the quantity.
                sumOfQuantity = " " + str(int(oldQuan) + productQuantity) 
                addingProduct.insert(index + 3 ,sumOfQuantity ) # Here we put back the quantity after modifying it.
            else:
                index +=1
        storeFile = open("store.txt" , "w")

        for word in addingProduct:
            word = word.replace(" ",", ")
            storeFile.write(word) # As first stated above.
            
        storeFile.close()
        

def removingProduct(): # This function has the same job as addProduct() function except that it decrements/removes already existed products.
    
    products = []
    csvFile = open("store.txt", "r")  # As we first stated above.
    for line in csvFile:
        wordList = line.split(",")      
        for word in wordList:
            products.append(word)


    productID = input("Enter product id: ")    
    
    productQuantity = int(input("Enter quantities to remove: "))
    remove = input("Are you sure you want to remove (y/n): ")
    print("-----------------------------------------------")

    if remove == ("y"):  # We make sure if the user really wants to decrement/remove the product or he/she chose the option by mistake.
        index = 0
        for id in products:
            if id == productID:
                oldQuan = products.pop(index + 3) 
                strOfdiffOfQuantity = " " + str(int(oldQuan) - productQuantity) 
                products.insert(index + 3 ,strOfdiffOfQuantity )
                diffOfQuantity = int(oldQuan) - productQuantity
            else:
                index +=1
        storeFile = open("store.txt" , "w")

        for word in products:
            word = word.replace(" ",", ")
            storeFile.write(word) 
                
        storeFile.close()   
    
    elif remove == "n": # If the user chose the option by mistake, he/she can return to the main menu.
        main()
        
    if diffOfQuantity <=0:  # Here if the quantity after decrementing was equal to 0, the whole line of information of the product would be removed.
        count = 0
        for word in products:
            word = word.lstrip() 
            if word.startswith(str(productID)):
                break  
            else:
                count +=1 
        
        products.pop(count)
        products.pop(count)
        products.pop(count)
        products.pop(count)
        products.pop(count)
        storeFile = open("store.txt" , "w")
        for word in products:
            word = word.replace(" ",", ")
            storeFile.write(word) 
            
        storeFile.close()   
        print("Product with id %s was completely removed"% productID)
    else:
        print("Product with id %s was reduced by %d quantity"% (productID,productQuantity)) # Here if the quantity after decrementing was not qual to 0, it would be
                                                                                            # reduced by said quantity.
                
def modifyProduct(): # This function modifies already existed products in the "store.txt" file usign their ID by changing the name, price, quantity, or discount 
                     # of the product. If the entered ID does not exist in the file, an error message will be displayed.
    products = []
    csvFile = open("store.txt", "r") # As stated above.
    for line in csvFile:
        wordList = line.split(",")      
        for word in wordList:
            products.append(word)
    
    
    productID = input("Enter id: ")
    print("=" * 31)
    
    if productID in products:
        print("Found product: Enter its info")
        newName = input("Enter name: ")       # These are the information to be replaced with the old ones.
        newPrice = input("Enter price: ")
        newQuantity = input("Enter quantity: ")
        newDiscount = input("Enter discount: ") + '\n' # The \n character is for moving the cursor to a new line.
        idx = products.index(productID)  # We wanna change the elements of the indecies according to the product's ID index.
        
        for id in products:
            if id == productID: # Here as we stated, we will use the index of the ID such that to sorting of the elements becomes as follows.
                products.pop(idx+1)  
                products.insert(idx+1,' '+newName)
                products.pop(idx+2)
                products.insert(idx+2,' '+newPrice)
                products.pop(idx+3)
                products.insert(idx+3,' '+newQuantity)
                products.pop(idx+4)
                products.insert(idx+4,' '+newDiscount)
                
            storeFile = open("store.txt" , "w")
            for word in products:
                word = word.replace(" ",", ")
                storeFile.write(word) 

            storeFile.close()
        print("Product was modified successfully")
    else:
        print("There is no product with such ID.")
        main()

def filterByPrice(): # This function seraches in the "store.txt" file for products that are ranging between a min and a max value,
                     # it then prints the products with said min to max range.
    minToMax = input('Enter a price range "min-max": ')
    dashPosition = minToMax.find('-')  # We will use the poisition of the dash character to extract the min and max values.
    minimum = int(minToMax[:dashPosition])
    maximum = int(minToMax[dashPosition+1:]) 
    print("=" * 31)
    
    txtList = makingList()
    length = len(txtList)
    count = 0
    
    for price in range(2,length+1,5): # Here the we change in the range depending on the index of every and each price element in the list that we made
        if minimum <= float(txtList[price]) <= maximum: # from the "store.txt" file.
            count += 1 # We increment the variable count each time a product takes place inside said range to find how many product is existed.
    if count == 0:
        print("There are no products in such range.")
    print("Matched products " + '(' + str(count) + ')')
    print("=" * 31)
    
    for price in range(2,length+1,5):
        if minimum <= float(txtList[price]) <= maximum:
            print("Id:          ", txtList[price - 2])
            print("title:      ", txtList[price - 1])
            print("price:       ", float(txtList[price]), "$")
            print("quantity:   ", txtList[price + 1])
            print("discount:   ", txtList[price + 2])
            print("-" * 31)

def makingList(): # This function creates a list from the "store.txt" file.
    txtList = []
    csvFile = open("store.txt", "r")  # csv = comma separated values.
    for line in csvFile: 
        wordList = line.split(",")   # comma between each element.
        for word in wordList: # for each word separately.
            if "\n" in word: # remove \n because it will cause a trouble with the printing later.
                word = word.replace("\n","")
                txtList.append(word)
            else: # to deal with each word separately.
                txtList.append(word)
    return(txtList)   # return the list






if __name__ == "__main__":
    main()