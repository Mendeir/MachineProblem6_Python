class Project:

    def __init__(self, id=0, title='', size=0, priority=0):
        self.__id = id
        self.__title = title
        self.__size = size
        self.__priority = priority

    def inputProject(self):
        print('Please fill in your project details')
        id_number = int(input('Enter the ID number of your project: '))
        title = str(input('Enter the title of your project: '))
        size = int(input('Enter the number of pages: '))
        priority_number = int(input('Enter the priority level of the project: '))

        self.__id = id_number
        self.__title = title
        self.__size = size
        self.__priority = priority_number

        write_file = open("InputProjectFile.txt","a")
        write_file.write(str(self.__id) + ', ')
        write_file.write(str(self.__title) + ', ')
        write_file.write(str(self.__size) + ', ')
        write_file.write(str(self.__priority))
        write_file.write('\n')
        write_file.close()

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_size(self):
        return self.__size

    def get_priority(self):
        return self.__priority


def menu():
    try:
        project = Project()
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
                project.inputProject()
            elif choice == 2:
                print()
            elif choice == 3:
                print()
            elif choice == 4:
                print()
            elif choice == 5:
                break
    except:
        print('Invalid Entry')


if __name__ == "__main__":
    menu()
