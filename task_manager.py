# TASK 25
# Compulsory Task 1 and 2
# task_manager.py
# written by Tintswalo Anicky Makhubele
# date: 25 march 2020
# Function: This program manages tasks assigned to each team member of a business


def reg_user():
    # Tis function asks the user for a new username and password and The user should also be asked to confirm the password.
    # if the username entered is already in user.txt, the user must be asked to enter a different username 
    # If the value entered to confirm the password matches the value of the password, the username and password should be written to user.txt in the appropriate format.
    
    #condition statememnt should the user trying to regiser a new user not be admin
    if username != "admin":
        print()
        print ("Only admin can register a new user,select another option!\n".upper() ) 
    
    
    else:
        
        print("To register a new user,please enter the following:\n".upper())



        # Ask the user to enter a new username
        new_username=input("Enter a new username: ")

        # open and read user.txt file
        user_file= open ( "user.txt" , "r")

        correct= False

        #loop through each line in the user.txt file and store each line in a list
        for line in user_file:
            
            #remove \n in each line
            line = line.strip()
            details = line.split(", ")

            #check if the username already exist
            if new_username != details[0]:
                correct = False
            else:
                correct = True

            while correct:
                
                #Display an appropriate error message if the user enters a username that is not listed in user.txt or enters a username that already exists.
                print("\nUsername already exist,please enter a different username!\n".upper())
                    
                #The user should repeatedly be asked to enter a new username until they provide different username.
                new_username=input("Username: ")
                correct= False
                
                user_file= open ( "user.txt" , "r")
                for line in user_file:
                #remove \n in each line
                    line = line.strip()
                    details = line.split(", ")

                    if new_username != details[0]:
                        correct = False
                    else:
                        correct = True
                        break
                user_file.close()

        # ask user to enter and confirm a new password for the user-
        new_password=input("Enter a new password: ")
        confirm=input("Confirm password: ")

        if new_password == confirm:
            
            user_file= open ( "user.txt" , "a") #open and append user.txt
            new_user=("\n" + new_username + ", "+ new_password)

            # store the new user in user.txt file
            user_file.write(new_user)

            # close the user.txt file
            user_file.close()

            print(f"\n{new_username} is successfully registered and added to user.txt!\n")
            
            add=False
        else:
            add = True

        while add:
            
            #Display an appropriate error message if the user enters a confirm password that doesn't match the password entered
            print("\nthe value entered to confirm the password does not match the value of the password,please try again!\n".upper())
        
            # The user should repeatedly be asked to enter a password tat matches with confirm password
            new_password=input("Enter a new password: ")
            confirm=input("Confirm password: ")

            if new_password == confirm:

                user_file= open ( "user.txt" , "a") #open and append user.txt
                new_user=("\n" + new_username + ", "+ new_password)

                # store the new user in user.txt file
                user_file.write(new_user)

                # close the user.txt file
                user_file.close()
            
                print(f"\n{new_username} is successfully registered and added to user.txt!\n")
                add = False
    
def add_task():
    
    # This function asks the user to enter the username of the person the task is assigned to, the title of the task, a description of the task and the due date of the task. 
    # The data about the new task should be written to tasks.txt and The date on which the task is assigned should be the current date.   

    #Import packages
    import datetime
    from datetime import date
    
    task_file = open ( "tasks.txt" , "a") #open and append tasks.txt
    
    print("~"*132)
        
    print("\nTo add a task,please enter the following details:\n".upper())

    # get input about the new task from the user    
    username1 =input("Enter the username of the person that you assigning the task to: ")
    task = input("Enter the title of the task: ")
    description = input("Enter the task description: ")
    date = date.today()
    due = input("Enter the due date for the task in this format(YYYY-MM-DD): ")
    completed = "No"
        
    add_task = "\n" + username1 + ", " + task + ", " + description + ", " + str(date) + ", " + due + ", " + completed
    
    # write the task in tasks.txt
    task_file.write(add_task)

    print(f"\nyou have successfuly assigned a task to {username1} in tasks.txt!\n".upper())

    task_file.close #close tasks.txt

def view_all():

    # This function display the information for each task on the screen
    task_file = open ( "tasks.txt" , "r") #reopen and append tasks.txt
    task_lines = task_file.readlines()
    
    for num, line in enumerate (range(len(task_lines)), start = 0):
        task_line = task_lines[line].split(", ")
        print(f"Task {num} \nASSIGNED TO     : {task_line[0]} \nTASK            : {task_line[1]} \nTASK DESCRIPTION: {task_line[2]} \nDATE ASSIGNED   : {task_line[3]} \nDUE DATE        : {task_line[4]} \nTASK COMPLETED? : {task_line[5]}\n")
    
    task_file.close #close tasks.txt

def view_mine():

    # This function only display all the tasks that have been assigned to the user that is currently logged-in and gives then an option to mark the task as complete or edit the task.
    # If the user chooses to mark a task as complete, the ‘Yes’/’No’ value that describes whether the task has been completed or not should be changed to ‘Yes’
    # When the user chooses to edit a task, the username of the person to whom the task is assigned or the due date of the task can be edited. The task can only be edited if it has not yet been completed
    
    task_file = open ( "tasks.txt" , "r") #reopen and append tasks.txt
    task_lines = task_file.readlines()

    #program will search for the username in text files and print out their allocated tasks
    print (f"{username},the tasks assigned to you, are:\n")
    for num, line in enumerate (range(len(task_lines)), start = 0):
        task_line = task_lines[line].split(", ")
        if username == task_line[0]:
            print(f"Task {num} \nASSIGNED TO     : {task_line[0]} \nTASK            : {task_line[1]} \nTASK DESCRIPTION: {task_line[2]} \nDATE ASSIGNED   : {task_line[3]} \nDUE DATE        : {task_line[4]} \nTASK COMPLETED? : {task_line[5]}\n")
    
    task_file.close #close tasks.txt 
        
    edit = False
    while edit == False: 
        # user chooses which one of their tasks they want to mark as complete or edit. 
        task_number = int(input("Please enter a task number to edit a task or -1 for main menu: "))

        # -1 used to allow the user to return to the main menu
        if task_number == -1:
            edit = True    

        else:
            task_file = open ('tasks.txt', 'r')
            # if the user chooses to mark their task complete, we create a list where we store all the tasks.
            # then we use the number enetered by the user to go to their specific task. 
            my_list = []
            my_list = task_file.read().splitlines()
            my_list_item = my_list[task_number].split(", ") # selecting the task to be marked as complete so that we can edit item task complete
            
            mark_edit = input ("\nDo you want to mark this task as complete or edit? (enter 'c' or 'e')\n")
            # if the user chooses to mark the task complete, we take the line of that task entered by the user, insert 'Yes'
            if mark_edit.lower() == "c":
                my_list_item[5] = 'Yes'
                
                # after inserting 'Yes', we join the line back as it was originally in the list
                my_list_join = ", ".join(my_list_item)
                
                # then after joining the line, we insert it back into the tasks list at the very same position
                my_list[task_number] = my_list_join
                
                # finaly, we write the whole list back in the text file
                task_file1 = open ('tasks.txt', 'w')
                for item in my_list:
                    task_file1.write(f"{item}\n")
                task_file1.close
                print(f"\nTask {task_number} marked as complete!".upper())
                edit = True

            # if the user chooses to edit the task, if the task has already been marked as complete, we let the user know that the task cannot be edited.
            elif mark_edit.lower() == 'e':
                if my_list_item[5] == 'Yes':
                    print(f"\nTask {task_number} has already been completed, you cannot edit it\n".upper())
                else:
                    # if the username can edit the task, then we ask them to choose what they want to edit which can only be either the username or the due date
                    # once the user makes their choice, the same logic used above is applied. We take the specific line in the task list where the changes have to be made
                    # then we change either the username or the due date, then we join the line back to its original form and insert it back in the tasks list with the necessary changes made.
                    choice1 = input ("Enter (u) to edit username or (d) to edit the task due date: ")
                    if choice1.lower() == "u":
                        usernameChange = input("\nEnter the new username: ")
                        my_list_item[0] = usernameChange
                        my_list_join = ", ".join(my_list_item)
                        my_list[task_number] = my_list_join
                        #print(my_list)
                        task_file2 = open ('tasks.txt', 'w')
                        for item in my_list:
                            task_file2.write(f"{item}\n")
                        task_file2.close()
                        print(f"\nTask {task_number} is now assigned to {usernameChange}\n")

                    elif choice1.lower() == "d":
                        date_modification = input ("Enter the new due date (YYYY-MM-DD): ")
                        my_list_item[4] = date_modification
                        my_list_join = ", ".join(my_list_item)
                        my_list[task_number] = my_list_join
                        
                        task_file3 = open ('tasks.txt', 'w')
                        for element in my_list:
                            task_file3.write(f"{element}\n")
                        task_file3.close
                        print (f"\nThe new due date for Task {task_number} is {date_modification}\n")
                        break 
            
            task_file.close()

def reports():

    # When the user chooses to generate reports, two text files, called task_overview.txt and user_overview.txt , should be generated

    #Import packages
    import datetime
    from datetime import date

    # the reports function writes reports in 2 different text files. The users_overview file and the task overview file.
    read_task3 = open ('tasks.txt', 'r')
    task_count_list = read_task3.read().splitlines()
    read_task3.close()
    list_length = len(task_count_list)
    #print(f"Total tasks is {list_length}")

    #counters used to count rhe number of tasks done, incomplete and overdue
    countYes = 0
    countNo = 0
    overdue = 0
    today = date.today() # stores the current date

    # counting the number of tasks completed and tasks that are not yet completed  
    for line in task_count_list:
        if "Yes" in line:
            countYes +=1
        else:
            countNo +=1
    #print (f"completed tasks is {countYes} and uncompleted is {countNo}")

    # taking each portion of the due date in order to convert it to a datetime format so that we can compare it to the current date and determin if a task is overdue
    for item in task_count_list:
        due_date = item.split(", ")[4]
        date_month = due_date[5:7]
        date_year = due_date[0:4]
        date_day = due_date[8::]

        # casting the due date into a date format
        dueDateInt = date(int(date_year), int(date_month), int(date_day))

        # comparing the dates to determine if the task is overdue
        if dueDateInt < today and "No" in item:
            overdue +=1
    #print(f"Overdue is {overdue}")
    # the following lines calculates the percentage of incomplete tasks and the percentage of tasks that are overdue.
    percentage_incomplete = (countNo/list_length) * 100
    #print(f"The percentage of incomplete tasks is {percentage_incomplete:.2f}%")
    percentage_overdue = (overdue/list_length) * 100
    #print(f"The percentage of overdue tasks is {percentage_overdue:.2f}%")

    # once all the necessary calculations are done, we write the results in the overview text file
    outfile = open('task_overview.txt', 'w')
    outfile.write(f"The total number of tasks is {list_length} \nThe total number of completed tasks is {countYes} \nThe total number of uncompleted tasks is {countNo} \nThe total number of tasks that are overdue and uncompleted is {overdue} \nThe percentage of incomplete tasks is {percentage_incomplete:.2f}% \nThe percentage of tasks that are overdue is {percentage_overdue:.2f}%")
    outfile.close()

    
    # the same logic used above is applied here but this time for each user. 
    open_overview = open ('user_overview.txt', 'w')
    line_out = ""

    
    users_read = open ('user.txt', 'r')
    list_users = users_read.read().splitlines()
    users_read.close()
    list_users_length = len(list_users)

    tasks_read = open ('tasks.txt', 'r')
    tasks_list = tasks_read.read().splitlines()
    tasks_list_length = len(tasks_list)
    tasks_read.close()
    #print(tasks_list_length)
    #print(list_users_length)

    user_tasks_count = 0
    user_completed_tasksCount = 0
    user_incomplete_tasksCount = 0
    user_overdue_taskCount = 0
    usernames = [] # stores the usernames so that we can display details for each username
    user_tasks = []
    
    # for each username, we display the number of tasks assigned to that user, the percentage of tasks assigned to that user, the percentage of tasks completed, uncompleted and overdue.
    for line in list_users:
        usernames.append(line.split(", ")[0])

    # writing in the first line, the total number of users and tasks.
    # then for each user, we find the total number of tasks, the percentage of tasks completed, uncompleted and overdue.
    # To do this, we use counters which are set to 0 above and incremented once a specific condition is met.
    open_overview.write(f"The total number of users is {list_users_length} and the total number of tasks is {tasks_list_length}\n")
    for username in usernames:
        for task in range(0, len(tasks_list)):
            due_date1 = tasks_list[task].split(", ")[4]
            date_month1 = due_date1[5:7]
            date_year1 = due_date1 [0:4]
            date_day1 = due_date1 [8::]
            due_date_int1 = date(int(date_year1), int(date_month1), int(date_day1))
            today1 = date.today()
            if f"{username}" in f"{tasks_list[task]}":
                user_tasks_count += 1
            if f"{username}" in f"{tasks_list[task]}" and "Yes" in f"{tasks_list[task]}":
                user_completed_tasksCount += 1
            if f"{username}" in f"{tasks_list[task]}" and "No" in f"{tasks_list[task]}":
                user_incomplete_tasksCount += 1
            if f"{username}" in f"{tasks_list[task]}" and "No" in f"{tasks_list[task]}" and due_date_int1 < today1:
                user_overdue_taskCount += 1
        user_tasks.append(username)
        user_tasks.append(user_tasks_count)
        user_taskPer = round((user_tasks_count/tasks_list_length)*100, 2)
        user_tasks.append(user_completed_tasksCount)
        user_completed_tasksPer = round((user_completed_tasksCount/tasks_list_length)*100, 2)
        user_tasks.append(user_incomplete_tasksCount)
        user_incomplete_tasksPer = round((user_incomplete_tasksCount/tasks_list_length)*100, 2)
        user_tasks.append(user_overdue_taskCount)
        user_overdue_tasksPer = round((user_overdue_taskCount/tasks_list_length)*100, 2)
        # for each user, we write the necessary details in the user overview text file
        line_out = username + " " + "has" + " " + str(user_tasks_count) + " tasks, " + str(user_taskPer) + "%" + " of tasks, " + " " + str(user_completed_tasksPer) + "%" + " tasks completed" + ", " + str(user_incomplete_tasksPer) + "%" + " incomplete tasks" + ", "+ str(user_overdue_tasksPer) + "% " + " tasks overdue" + "\n"
        open_overview.write(line_out)
        # reseting the counters so that the calculations are done properly for each user.
        user_tasks_count = 0
        user_completed_tasksCount = 0
        user_incomplete_tasksCount = 0
        user_overdue_taskCount = 0
    open_overview.close()

def view_statistics():

    choice = input ("\nPlease enter what you want to see 'users overview' or 'tasks overview'(enter 'u' or 't') ")
    # when admin chooses 'users overview', we create a list to store all the lines in the file users_overview.txt.
    # then the reports read from the text file is printed to the user in a user friendly manner.
    if choice.lower() == "u":
        user_overview = open ('user_overview.txt', 'r')
        user_overview_list = user_overview.read().splitlines()
        user_overview.close()
        for line1 in user_overview_list:
            print(line1)      

    # similarly, when the user chooses tasks overview, we create a list containing all the necessary details from the text file and we print the details in a user friendly manner.      
    elif choice.lower() == "t":
        task_overview = open('task_overview.txt', 'r')
        task_overview_list = task_overview.read().splitlines()
        task_overview.close()
        for line in task_overview_list:
            print(line)

user_file = open ( "user.txt" , "r")

#the user must enter a username and password.
print("~"*132)

print("ENTER YOUR LOGIN DETAILS:")

print()

username=input("USERNAME: ")
password=input("PASSWORD: ")

#use a for loop to varify if the login details entered by the user are valid and registered in the user.txt file
correct= False

#loop through each line in the user.txt file and store each line in a list
for line in user_file:
    
    #remove \n in each line
    line = line.strip()
    details = line.split(", ")

    if username == details[0] and password == details[1]:
        correct = False
        break
    else:
        correct = True

while correct:
    user_file.close()
    user_file= open ( "user.txt" , "r+")
    #Display an appropriate error message if the user enters a username that is not listed in user.txt or enters a valid username but not a valid password
    print("Username or password is incorrect,please enter the correct username and password!\n")
        
    #The user should repeatedly be asked to enter a valid username and password until they provide appropriate credentials.
    username=input("USERNAME: ")
    password=input("PASSWORD: ")
    correct= False
    
    for line in user_file:
    #remove \n in each line
        line = line.strip()
        details = line.split(", ")

        if username == details[0] and password == details[1]:
            correct = False
            break
        else:
            correct = True

print("~"*132)
print(f"\nwelcome {username}, you have successfully logged in.\n".upper())

#while username is not admin
while username != "admin":
    print("~"*132)
    # display a menu once a user have successfully logged in
    user_menu = input("\nPLEASE SELECT ANY OF THE FOLLOWING:\nr - register user \na - add task \nva - view all tasks \nvm - view my tasks \ne - exit \n")
    print()

    # If the user chooses ‘r’ to register a user, the function reg_user() must be called.
    if user_menu.lower()=="r":
        print("~"*132)
        reg_user()

    # If the user chooses ‘a’ to register a user, the function add_task() must be called.
    if user_menu.lower()=="a":
        print("~"*132)
        add_task()
        
    #If the user chooses ‘va’ to view all tasks, the function view_all() must be called.
    if user_menu.lower()=="va":
        print("~"*132)
        view_all()
   
    #If the user chooses ‘vm’ to view all tasks, the function view_mine() must be called.
    if user_menu.lower()=="vm":
        print("~"*132)
        view_mine()
            
    if user_menu.lower()=="e":
        print("\nTHANK YOU FOR LOGGING IN, UNTIL NEXT TIME!\n")
        break

#while the logged in user is the admin   
while username == "admin": 
    print("~"*132) 

    # display a new menu that includes viewing stats
    admin_menu=input("\nPLEASE SELECT ANY OF THE FOLLOWING:\n\nr - register user \na - add task \nva - view all tasks \nvm - view my tasks \ngr - generate reports \nvs - view statistics of tasks and users \ne - exit \n")
    print()
    
    # If the user chooses ‘r’ to register a user, the function reg_user() must be called.
    if admin_menu.lower() == "r":
        print("~"*132)
        reg_user()
    
    # If the user chooses ‘a’ to register a user, the function add_task() must be called.    
    if admin_menu.lower() == "a":
        print("~"*132)
        add_task()

    #If the user chooses ‘va’ to view all tasks, the function view_all() must be called. 
    if admin_menu.lower() =="va":
        print("~"*132)
        view_all()
    
    #If the user chooses ‘vm’ to view all tasks, the function view_mine() must be called.
    if admin_menu.lower() =="vm":
        print("~"*132)
        view_mine()

    # if the user chooses to generate reports, two text files, called task_overview.txt and user_overview.txt , should be generated
    if admin_menu.lower() =="gr":
        print("~"*132)
        reports()

        print("Reports generated. Please check 'task_overview.txt' and 'user_overview.txt' to see them.\n")

    #for admin to view the statistics of the task if needed
    if admin_menu.lower() == "vs":
        
        print("~"*132)
        generate_stats = input("To view statistics,please enter 'gr' to genarate stats firts: ")

        if generate_stats == "gr":
            reports()

        print("Reports generated.\n")

        view_statistics()

    
    if admin_menu.lower()=="e":
        print("\nTHANK YOU FOR LOGGING IN, UNTIL NEXT TIME!\n")
        break

#close both user and task files
user_file.close()

#***********************************************************END**********************************************************