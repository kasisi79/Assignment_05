#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2022-Jan-01, Created File
# KHarris, 2022-AUG-04, Modified code to use dictionaries as inner data type
#------------------------------------------#

# Declare variables
dicRow = {} # Dictionary Row
strChoice = '' # User input
lstTbl = [] #list declaration
lstTbl.append(dicRow)
lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        objFile = open(strFileName, 'r')
        for row in objFile:
            if not row.strip():
                continue
            else:
                lstRow = row.strip().split(',')
                dicRow = {'ID': int(lstRow[0]), 'CD Title': str(lstRow[1]), 'Artist Name': str(lstRow[2])}
                lstTbl.append(dicRow)
        objFile.close()
        #pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID': intID, 'CD Title': strTitle, 'Artist Name': strArtist}
        lstTbl.append(dicRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('Current CD Inventory')
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(row.values(), sep = ', ')
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        print('Current CD Inventory')
        for row in lstTbl:
            print(row, sep=', ',)
        delEntry = int(input('Enter ID of CD information you wish to delete: '))
        lnNum = 0
        successfulDel = False
        for row in lstTbl:
            if not row:
                continue
            lnNum += 1
            if row['ID'] == delEntry:
                del lstTbl[lnNum]
                successfulDel = True
                print('Info Deleted')
                break
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            savedRow = str(row.values()).strip('dict_values([]) ')
            print(savedRow)
            objFile.write(savedRow)
            objFile.write('\n')
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

