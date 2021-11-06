import os

class ProjectCollection:

    project_queue = []

    def __init__ (self):
        pass

    def retrieve_projects(self):
        project_file = open("InputProjectFile.txt", "r")
        
        self.project_queue.clear()

        for file_line in project_file:
            id,title,size,priority = file_line.split(", ")
            
            self.project_queue.append([id, title, size, priority])

        project_file.close()
    
    def sort_project_queue(self):
        self.project_queue = sorted(self.project_queue, key = lambda attribute: (attribute[3], attribute[2]))

    def print_projects(self):
        for projects in self.project_queue:
            print(projects)

    def schedule_exists(self):
        if not self.project_queue:
            return False
        else:
            return True

    def search_project(self, project_key):
        print(self.project_dictionary[project_key])

class Navigation:

    def __init__ (self, given_project_queue):
        self.project_queue = given_project_queue
    
    def menu(self):
        project_list = ProjectCollection()

        try:
            while True:
                print('Menu:')
                print('[1] Input Project Details')
                print('[2]. View Projects')
                print('[3] Schedule Projects')
                print('[4] Get a Project')
                print('[5] Exit')

                choice = int(input('Enter your choice: '))
                if choice == 1:
                    self.input_project()
                
                elif choice == 2:
                    self.view_table()
                
                elif choice == 3:
                    self.schedule_projects_submenu()
                    
                elif choice == 4:
                    pass
                
                elif choice == 5:
                    break
        
        except ValueError:
            print('Invalid Entry')

    def input_project(self):

        print('Please fill in your project details')
        id_number = int(input('Enter the ID number of your project: '))
        title = str(input('Enter the title of your project: '))
        size = int(input('Enter the number of pages: '))
        priority_number = int(input('Enter the priority level of the project: '))

        write_file = open("InputProjectFile.txt", "a")
        write_file.write(str(project.get_id()) + ', ')
        write_file.write(str(project.get_title()) + ', ')
        write_file.write(str(project.get_size()) + ', ')
        write_file.write(str(project.get_priority()))
        write_file.write('\n')
        write_file.close()

    def view_table(self):
        project_collection = ProjectCollection()
        print('[a] One Project')
        print('[b] Completed')
        print('[c] All Projects')
        choice = str(input('Enter your choice: '))
        if choice == 'a':
            key = int(input('Enter the ID number: '))
            project_collection.search_project(key)
        elif choice == 'b':
            print('b')
        elif choice == 'c':
            print('c')

    def schedule_projects_submenu(self):
        print("\t[a] Create Schedule")
        print("\t[b] View Updated Schedule")

        choice = str(input("Enter your choice: "))

        if (choice == "a"):
            self.project_queue.retrieve_projects()
            self.project_queue.sort_project_queue()

        elif (choice == "b"):
            if self.project_queue.schedule_exists():
                self.project_queue.print_projects()
            else:
                choice = input("No Existing Schedule. Do you want to create a schedule?(Y|N): ")
                if choice == "Y":
                    self.project_queue.retrieve_projects()
                    self.project_queue.sort_project_queue()

        else: 
            print("Invalid Choice")


if __name__ == "__main__":
    project_queue = ProjectCollection()
    main_menu = Navigation(project_queue)
    main_menu.menu()
