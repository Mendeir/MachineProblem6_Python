class Project:

    def __init__(self, id, title, size, priority):
        self.__id = id
        self.__title = title
        self.__size = size
        self.__priority = priority

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_size(self):
        return self.__size

    def get_priority(self):
        return self.__priority


class ProjectCollection:

    project_dictionary = {}

    def __init__ (self):
        pass

    def add_project(self, project_id, project_object):
        self.project_dictionary[project_id] = project_object

    def search_project(self, project_key):
        print(self.project_dictionary[project_key])


def input_project():

    print('Please fill in your project details')
    id_number = int(input('Enter the ID number of your project: '))
    title = str(input('Enter the title of your project: '))
    size = int(input('Enter the number of pages: '))
    priority_number = int(input('Enter the priority level of the project: '))

    project = Project(id_number, title, size, priority_number)
    project_collection = ProjectCollection()

    project_collection.add_project(project.get_id(), project)

    write_file = open("InputProjectFile.txt", "a")
    write_file.write(str(project.get_id()) + ', ')
    write_file.write(str(project.get_title()) + ', ')
    write_file.write(str(project.get_size()) + ', ')
    write_file.write(str(project.get_priority()))
    write_file.write('\n')
    write_file.close()


def view_table():
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


def menu():
    try:
        while True:
            print('Menu:')
            print('[1] Input Project Details')
            print('[2]. View Projects')
            print('\t [1] One Project')
            print('\t [2] Completed Projects')
            print('\t [3] All Projects')
            print('[3] Schedule Projects')
            print('\t [1] Create Schedule')
            print('\t [2] View Schedule')
            print('[4] Get a Project')
            print('[5] Exit')
            choice = int(input('Enter your choice: '))
            if choice == 1:
                input_project()
            elif choice == 2:
                view_table()
            elif choice == 3:
                print()
            elif choice == 4:
                print()
            elif choice == 5:
                break
    except ValueError:
        print('Invalid Entry')

if __name__ == "__main__":
    menu()
