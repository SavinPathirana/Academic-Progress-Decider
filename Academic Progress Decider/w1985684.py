# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1985684 
# Date: 17/03/2023
creditpass = 0         #variable for the input for credit at pass
total = 0              #variable for the total of three marks
creditdef = 0          #variable for the input for credit at defer
creditfail = 0         #variable for the input for credit at fail
students = 0           #number of students entered
progressedstudents = 0 #number of students progressed
trailingstudents = 0   #number of students trailed
retrieverstudents = 0  #number of students retrieved
excludedstudents = 0   #number of students excluded


progresslist = []      #list for collecting inputs of progressing students
trailinglist = []      #list for collecting inputs of trailing students
retrieverlist = []     #list for collecting inputs of retrieveing students
excludedlist = []      #list for collecting inputs of excluded students

def inputcheck(prompt):   #user defined function to find whether the input marks are in the range given and to check whether the input is integer
    while True:           #reference - https://www.geeksforgeeks.org/
        try:
            mark=int(input(prompt))
            if mark not in [0,20,40,60,80,100,120]:
                print('Out of Range')
                continue
        except:
            print('Integer required.')                                     
            continue
        return mark
    
identitycheck = input('Welcome! \n If you are a staff member enter (s), \n If you are a student enter (st), \n If you are not either of them enter (o): \n')

while True:     #the while loop that takes the inputs, calculate the total and student count, decide whether the students have progressed,did not progressed or excluded and count them
        if identitycheck == 'o':  #to check whether the user of the program has access
            print('You do not have permission to use this program')
            break
        elif  identitycheck != 's' and identitycheck != 'st':
            print('Please enter a valid input and restart the program.')
            break
        creditpass = inputcheck('Please enter your credit at pass:')
        creditdef = inputcheck('Please enter your credit at defer:')
        creditfail = inputcheck('Please enter your credit at fail:')
        students = students +1
        total =creditpass + creditdef+ creditfail
        if total != 120:
            print('Total incorrect.')
            continue
        elif creditpass == 120:
            print('Progress')
            progresslist.append([creditpass,creditdef,creditfail])
            progressedstudents = progressedstudents +1
        elif creditpass == 100:
            print('Progress(module trailer)')
            trailinglist.append([creditpass,creditdef,creditfail])
            trailingstudents = trailingstudents +1
        elif creditfail >= 80:
            print('Exclude')
            excludedlist.append([creditpass,creditdef,creditfail])
            excludedstudents = excludedstudents +1
        else:
            print('Do not progress - module retriever')
            retrieverlist.append([creditpass,creditdef,creditfail])
            retrieverstudents = retrieverstudents +1
           
        if identitycheck == 'st':
            print('Thank you for using this program!')
            break
        loopcheck = input('Would you like to enter another set of data? \n Enter "y" for yes or "q" to quit and view results:') #to check whether the user want to continue or exit the loop
        if loopcheck == "q":
            print('-'*100)         #a line to break the histogram from the rest.
            
            print('Histogram')     # a histogram that represents the number of students and their outcomes with stars (1 star = 1 student)
            print ('Progress   :',str(progressedstudents),':', '*'*progressedstudents)
            print ('Trailer    :',str(trailingstudents),':', '*'*trailingstudents)
            print ('Retriever  :',str(retrieverstudents),':', '*'*retrieverstudents)
            print ('Excluded   :',str(excludedstudents),':', '*'*excludedstudents)
            print()
            print(str(students),('outcomes in total.'))
            print('-'*100)              #a line to break the histogram from the rest.
            print()

            print('...Part 2...')       #a list of the outcomes 
            for x in range (len(progresslist)):                  #reference - https://stackabuse.com/
                print('Progress -',end='')
                print (str(progresslist[x]).replace('[','').replace(']',''))   #reference for replace - https://stackoverflow.com/
            for x in range (len(trailinglist)):
                print('Progress(module trailer) -',end='')
                print(str(trailinglist[x]).replace('[','').replace(']',''))
            for x in range (len(retrieverlist)):
                print('Module retriever -',end='')
                print(str(retrieverlist[x]).replace('[','').replace(']',''))
            for x in range (len(excludedlist)):
                print('Exclude -',end='')
                print(str(excludedlist[x]).replace('[','').replace(']',''))
            

            with open('outputtext.txt', 'w') as outputtext:          # a text output of the outcomes
                outputtext.write('...Part 3...\n')
                for x in range (len(progresslist)):
                    outputtext.write('Progress - {}\n'.format(progresslist[x]).replace('[','').replace(']',''))
                for x in range (len(trailinglist)):
                    outputtext.write('Progress(module trailer) - {}\n'.format(trailinglist[x]).replace('[','').replace(']',''))
                for x in range (len(retrieverlist)):
                    outputtext.write('Module retriever - {}\n'.format(retrieverlist[x]).replace('[','').replace(']',''))
                for x in range (len(excludedlist)):
                    outputtext.write('Exclude - {}\n'.format(excludedlist[x]).replace('[','').replace(']',''))

                print('Output written to file: outputtext.txt')      # a text that say the text file was created
                print('Thank you for using this program!')
            break
        elif loopcheck == "y":
            continue
        else:
            print('Please enter "y" or "q"')   #what to display when y or q wasnt the input
            break

        

        