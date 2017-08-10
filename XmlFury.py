################################################
### @author Muhammad Farris Iqbal Bin Khalid ###
###      @email farriskhalid@gmail.com       ###
###    @website https://farriskhalid.com     ###
###             @version 1.0                 ###
################################################

class XmlFury:
    def __init__(self, filename):
        self.storage = []
        self.filename = filename
        self.storeValuesInArray()

    # opens the file and stores all of the content inside of an storage array
    def storeValuesInArray(self):
        file = open(self.filename, "r")
        elementValues = ""

        # separates all items in the file into an array of all the things from the file
        for line in file.read():
            if line == ">":
                self.storage.append(elementValues)
                elementValues = ""
            else:
                elementValues += line
        file.close()

    # this function outputs a "skeletal" version of the filename being opened
    # if the filename has attributes inside xml elements, then they will be removed
    # Only the xml elements will remain and be written to a new file without attributes or
    # content inside of element blocks
    def buildSkeleton(self, outputfilename):

        allElements = list(self.storage)
        openingElements = []
        closingElements = []

        # this loop parses everything inside allElements array to determine the
        # opening and closing element tags
        while len(allElements) > 0:
            temp = allElements.pop(0)
            temp = temp.replace('\n', '')

            # opening bracket indicating beginning of an element
            # populate the openingElements array
            if temp[0] == "<":
                removeAttributes = temp.rsplit(' ', 1)[0]
                if removeAttributes[1] == "/":
                    closingElements.append(removeAttributes[2:])
                else:
                    openingElements.append(removeAttributes[1:])


            # closing bracket condition to indicate ending of an element
            # populate closingElements array
            elif temp[0] != "<":
                generic = ""
                for letter in temp:
                    if letter == "/":
                        generic = ""
                    else:
                        generic += letter
                closingElements.append(generic)

        newFile = open(outputfilename, 'w')

        # the rebuild loop,the core of this function, where openingElements and closingElements come together
        # to produce a skeletal version of the file (the original file)
        for element in openingElements:
            if element == closingElements[0]:
                removal = closingElements.pop(0)
                newFile.write("<" + removal + ">" + "</" + removal + ">")
            else:
                newFile.write("<" + element + ">")

        # write the closing root element to file, free up system resources
        newFile.write("<" + closingElements.pop() + ">")
        newFile.close()

    # this function checks the path in the form of "root/subelement1/subelement2"
    # to see if the elements and their hierarchy already exist in original file
    def checkPath(self, path):
        data = list(self.storage)
        path = path.split('/')

        while len(path) > 0:
            temp = data.pop(0)
            temp = temp.replace('\n', '')

            # compare data array to path array
            if temp[0] == "<":
                removeAttributes = temp.rsplit(' ', 1)[0]
                # skip closing element tags
                if removeAttributes[1] == "/":
                    continue
                else:
                    # if the hierarchy of elements in file does not
                    # match hierarchy requested to be checked, return False
                    # if this condition never hits, return True after loop ends
                    if path.pop(0) != removeAttributes[1:]:
                        return False
        return True

# XmlFury("test.xml").buildSkeleton("testfile2.xml")

