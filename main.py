import os
from os import system, name
import time

class ProjectCollection:

    project_queue = []

    def __init__ (self):
        pass

    def retrieve_projects(self):
        """
            Retrieve projects data from a file.
            Put retrieved data into a queue.
            Completed Projects are not put into queue.
            Arranged by id, title, size, priority.
        """

        try:
            completed_file = open("CompletedProjects.txt", "r")
            completed_list = completed_file.readlines()
            completed_file.close()

            project_file = open("InputProjectFile.txt", "r")
            
            self.project_queue.clear()

            for file_line in project_file:
                if file_line in completed_list:
                    continue

                id, title, size, priority = file_line.split(", ")
                
                self.project_queue.append([id, title, size, priority])

            project_file.close()

            if self.schedule_exists():
                print("Schedule Successfully Created!")
            else:
                print("No schedule to be created yet. You completed all the existing project!")
            
        except FileNotFoundError:
            print("File path not found.")

    def sort_project_queue(self):
        """
            Sort project queue into ascending order.
            Sort by priority first, then size.
        """

        self.project_queue = sorted(self.project_queue, key = lambda attribute: (attribute[3], attribute[2]))

    def print_projects(self):
        """
            Print projects queue
        """

        if not(self.schedule_exists()):
            print("All projects have been completed.")

        print("ID Number : Title                      : Size : Priority ")

        for projects in self.project_queue:
            print(projects[0], " " * (8 - len(projects[0])), ":",
                  projects[1], " " * (25 - len(projects[1])), ":",
                  projects[2], " " * (3 - len(projects[2])), ":",
                  projects[3], end="")

        print("")

    def schedule_exists(self) -> bool:
        """
            Returns true if a project queue exist.
            If not, returns false
        """

        if not self.project_queue:
            return False
        else:
            return True



    def completedproject(self):

        """
                Delete the uppermost project in Queue
                Write the Completed Project in a txt file
                Display The Queue
        """
        # Delete the uppermost project in a queue
        result = self.project_queue.pop(0)
        print(f'Topmost project from the queue ({result}) is  removed')
        time.sleep(2)

        # Write the deleted uppermost project in a textfile
        write_file = open("CompletedProjects.txt", "a")
        write_file.write(f"{result[0]}, {result[1]}, {result[2]}, {result[3]}")
        write_file.close()



class Navigation:

    def __init__ (self, given_project_queue: ProjectCollection):
        self.project_queue = given_project_queue

    def menu(self):
        """
            Display the menu and get the user choice.
        """
        
        try:
            while True:
                self.clear_screen()
                self.display_header("Menu")
                print('[1] Input Project Details')
                print('[2] View Projects')
                print('[3] Schedule Projects')
                print('[4] Get a Project')
                print('[5] Exit')

                print("")
                choice = int(input('Enter your choice: '))
                print("")

                if choice == 1:
                    self.clear_screen()
                    self.input_project_submenu()
                
                elif choice == 2:
                    self.clear_screen()
                    self.view_projects_submenu()
                
                elif choice == 3:
                    self.clear_screen()
                    self.schedule_projects_submenu()
                    
                elif choice == 4:
                    self.clear_screen()
                    self.get_project_submenu()
                
                elif choice == 5:
                    break
        
        except ValueError:
            print('Invalid Entry')


    def input_project_submenu(self):

        """
        This method will ask the user to input a project.
        Each project entered by the user will automatically be written in the 'InputProjectFile.txt' file.
        """
        
        self.display_header("Input Project Details")

        print("")
        # Variable to store the size of the file
        filesize = os.path.getsize("InputProjectFile.txt")
        temp = False

        # Check if the ID Number is repeated
        check_file = open("InputProjectFile.txt", "r")
        check_list = []

        for i in check_file:
            check_list.append(i.split(", "))

        check_file.close()


        print('Please fill in your project details')
        id_number = int(input('Enter the ID number of your project: '))
        for l in check_list:
            if str(id_number) == l[0]:
                temp = True
        if temp:
            print('ID Number is already been used.')
            self.prompt_key()
        else:
            title = str(input('Enter the title of your project: '))
            size = int(input('Enter the number of pages: '))
            priority_number = int(input('Enter the priority level of the project: '))
            print("Project Successfully Added!")
            self.prompt_key()


            # Store each user input inside the 'InputProjectFile.txt' text file.
            try:
                # Check if the file is empty to use first the 'w' for write mode then 'a' for append mode if not
                if filesize - 2 == 0:

                    write_file = open("InputProjectFile.txt", "w")
                    write_file.write(str(id_number) + ', ')
                    write_file.write(str(title) + ', ')
                    write_file.write(str(size) + ', ')
                    write_file.write(str(priority_number))
                    write_file.write('\n')
                    write_file.close()
                else:
                    write_file = open("InputProjectFile.txt", "a")
                    write_file.write(str(id_number) + ', ')
                    write_file.write(str(title) + ', ')
                    write_file.write(str(size) + ', ')
                    write_file.write(str(priority_number))
                    write_file.write('\n')
                    write_file.close()
            except IOError:
                print('File not found')


    def view_projects_submenu(self):

        """
        This method will print the user's desire to see inside the copy typing based on user's selected from the menu.
        """
        self.display_header("View Projects")

        print('\t[a] One Project')
        print('\t[b] Completed')
        print('\t[c] All Projects')
        choice = str(input('Enter your choice: '))
        if choice == 'a':
            self.clear_screen()
            self.one_project_submenu()
            self.prompt_key()

        elif choice == 'b':
            self.clear_screen()
            self.completed_projects_submenu()
            self.prompt_key()

        elif choice == 'c':
            self.clear_screen()
            self.all_projects_submenu()
            self.prompt_key()

        else:
            print('Invalid Choice')


    def one_project_submenu(self):

        """
        This method will display a single project copy typed based on the user's entered ID number.
        """

        self.display_header("View One Project")
        print("")

        try:
            key = int(input('Enter the ID number: '))
            one_file = open('InputProjectFile.txt', 'r')
            temp = False

            # This will store each line inside the text file into the list
            file_list = []
            for f in one_file:
                file_list.append(f.split(", "))

            # Search the entered ID number in the list.

            for l in file_list:
                if str(key) == l[0]:
                    temp = True
                    # Printing the project details
                    print("ID Number : Title                      : Size : Priority ")
                    print(l[0], " " * (8 - len(l[0])), ":",
                          l[1], " " * (25 - len(l[1])), ":",
                          l[2], " " * (3 - len(l[2])), ":",
                          l[3])

            if not temp:
                print('ID number not found.')

            one_file.close()

        except FileNotFoundError:
            print('File path not found')

    def completed_projects_submenu(self):

        """
        This method will display all the completed projects from the text file.
        """
        self.display_header("View Completed Projects")
        print()

        print('Completed Projects:')
        try:
            completed_projects = open('CompletedProjects.txt', 'r')

            # Store each line of project in a list.
            file_list = []
            for i in completed_projects:
                file_list.append(i.split(", "))

            # Calling the method to print the list in text-based table format.
            self.text_based_display_submenu(file_list)

            completed_projects.close()


        except FileNotFoundError:
            print('File path not found')

    def all_projects_submenu(self):

        """
        This method will display all the projects received.
        """

        self.display_header("View All Projects")
        print("")

        print('All Projects:')
        try:
            all_projects = open('InputProjectFile.txt', 'r')

            # This will store each line inside the text file into the list.
            file_list = []
            for f in all_projects:
                file_list.append(f.split(", "))

            # Printing each line of all the projects received
            self.text_based_display_submenu(file_list)

            all_projects.close()

        except FileNotFoundError:
            print('File path not found')

    def text_based_display_submenu(self, list_project):

        """
        This method will print a text base table format to display projects.
        """


        if list_project:
            print("ID Number : Title                      : Size : Priority ")
            for i in list_project:
                print(i[0], " " * (8 - len(i[0])), ":",
                      i[1], " " * (25 - len(i[1])), ":",
                      i[2], " " * (3 - len(i[2])), ":",
                      i[3], end="")
            print("")
        else:
            print('The queue is empty')
    def schedule_projects_submenu(self):
        """
            Submenu for the Schedule Projects.
            Prompts for user input.
        """
    
        self.display_header("Create Schedule")
        print("\t[a] Create Schedule")
        print("\t[b] View Updated Schedule")

        print("")
        
        choice = str(input("Enter your choice: "))
        print("")

        choice = choice.lower()

        if (choice == "a"):
            self.project_queue.retrieve_projects()
            self.project_queue.sort_project_queue()
            self.prompt_key()

        elif (choice == "b"):
            self.clear_screen()
            self.display_header("View Updated Schedule")
            if self.project_queue.schedule_exists():
                self.project_queue.print_projects()
                self.prompt_key()

            else:
                choice = input("No Existing Schedule. Do you want to create a schedule?(Y|N): ")
                choice = choice.lower()

                if choice == "y":
                    self.project_queue.retrieve_projects()
                    self.project_queue.sort_project_queue()
                    self.prompt_key()

                elif choice == "n":
                    print("No schedule created yet.")
                    self.prompt_key()
                
                else:
                    print("Invalid choice.")
                    self.prompt_key()

        else: 
            print("Invalid Choice")
            self.prompt_key()

    def get_project_submenu(self):
        self.display_header("Get a Project")
        
        if self.project_queue.schedule_exists():
            self.project_queue.completedproject()
            self.project_queue.print_projects()
        else:
            print("No projects to be removed.")
        
        self.prompt_key()

    def display_header(self, word):
        """
            Display a box typed header from given word.
            30 word limit.
        """

        center = 14 - (len(word) // 2)
        spaces = int(center) * " "
        remaining_spaces = int(28 - (len(spaces) + len(word))) * " "

        print("*" * 30)
        print(f"*{spaces}{word}{remaining_spaces}*")
        print("*" * 30)

    def prompt_key(self):
        input("Press enter key to continue...")
    
    def clear_screen(self): 
        """
            Clears the screen
        """
        # Windows
        if name == 'nt': 
            _ = system('cls') 

        # Unix
        else: 
            _ = system('clear') 

if __name__ == "__main__":
    project_queue = ProjectCollection()
    main_menu = Navigation(project_queue)
    main_menu.menu()
