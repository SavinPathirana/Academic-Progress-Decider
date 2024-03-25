# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1985684 
# Date: 21/03/2023
print('Welcome!')
dic_data = {}              #a dictionary was created

while True:
    try:
        studentid = input('Please enter the student ID: ')           #the variable to take the student id
        if studentid[0] != 'w':
            print('Please enter a valid student id')
            continue
        if len(studentid) != 8:
            print('Please enter a valid student id')
            continue
        if studentid[1:8].isnumeric() == False:
            print('Please enter a valid student id')
            continue 
        credits_at_pass = int(input('Please enter the credit at pass: '))    # to check whether the input is in the given range and to find whether the input is integer
        if credits_at_pass not in [0,20,40,60,80,100,120]:
            print('Out of Range.')
            continue
        credits_at_differ = int(input('Please enter the credit at defer: '))  # to check whether the input is in the given range and to find whether the input is integer
        if credits_at_differ not in [0,20,40,60,80,100,120]:
            print('Out of Range.')
            continue
        credits_at_fail = int(input('Please enter the credit at fail: '))   # to check whether the input is in the given range and to find whether the input is integer
        if credits_at_fail not in [0,20,40,60,80,100,120]:
            print('Out of Range.')
            continue
        total = credits_at_pass+credits_at_differ+credits_at_fail   #the total of credits
    except:
        continue
    if total !=120:                           #the outcomes according to the inputs that were given
        print('Total incorrect')
        break
    elif credits_at_pass == 120:
        output = 'Progress'
    elif credits_at_pass == 100:
        output = 'Progress (module trailer)'
    elif credits_at_fail >= 80:
        output = 'Exclude'
    else:
        output = 'Do not progress - module retriever'
    print(output)
    if studentid not in dic_data:                                                                                   #to check whether the student id is in the dictionary already.
        dic_data[studentid] = { 'output':output, 'credits': [credits_at_pass, credits_at_differ, credits_at_fail]} #reference - https://stackabuse.com/
    else:
        print('This student id is already in the system., please input another id.')                               #what to display when the student id is in dictionary
        continue
    type = input('Would you like to enter another set of data? \n Enter "y" for yes or "q" to quit and view results:')    #to ask whether the user want to continue or exit
    if type == 'q':
        break
    elif type == 'y':
        continue
    else:
        print('Please enter a valid input.')
        break
print(str(dic_data).replace('{','').replace('}','').replace('[','').replace(']','')) #reference - https://stackoverflow.com/
print('Thank you for using this program!')