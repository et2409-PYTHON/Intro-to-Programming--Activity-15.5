import csv

def showMenu():
    "This function provides options to the user"
    print "A) Add to Directory"
    print "B) Display Directory"
    print "X) Exit Directory Program"

def phoneAdd():
    "This function adds new entry to directory"
    phoneDis = open("phonebook.csv", "a")
    phoneDis.write(first + "," + " ")
    phoneDis.write(last + "," + " ")
    phoneDis.write(email + "," + " ")
    phoneDis.write(phone)
    phoneDis.write("\n")
    print "{} {} added to directory.".format(first,last)


showMenu()
option = raw_input("-- ")

while option != "X":
    if option == "A" or option == "B":
        if option == "A":
            print "Add to Directory"
            first = raw_input("First Name: ")
            last = raw_input("Last Name: ")
            email = raw_input("Email Address: ")
            phone = raw_input("Phone Number: ")
            phoneAdd()
            showMenu()
            option = raw_input("-- ")

        elif option == "B":
            print "Display Directory"
            phoneDis = open("phonebook.csv", "r")
            try:
                rtext = ""
                reader = csv.reader(phoneDis)
                for row in reader:
                    for item in row:
                        rtext = rtext + "" + item
                    print rtext
                    rtext = ""
            finally:
                phoneDis.close()
            showMenu()
            option = raw_input("-- ")
