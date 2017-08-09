################################################
### @author Muhammad Farris Iqbal Bin Khalid ###
###      @email farriskhalid@gmail.com       ###
###    @website https://farriskhalid.com     ###
###             @version 1.0                 ###
################################################

class XmlFury():
    def __init__(self):
        self.menu = "Menu: \n" \
              "1 - create empty elements/single element from a path \n" \
              "2 - import csv file of id's that were mapped to write to mapping document of project manager\n" \
              "3 - create summary of mapped items for JIRA\n" \
              "Other number - quit"
        self.paths = []
        self.active = True

        while self.active:
            print(self.menu)
            choice = int(input("Enter Number: "))
            if choice == 1:
                self.CreateEmptyPath()
            elif choice == 2:
                self.completedIDs(input("id csv filename: \n"), input("mapping document filename: "))
            else:
                break

    def CreateEmptyPath(self):
        pass

    def completedIDs(self, idFile, mappingDocument):
        pass


XmlFury()