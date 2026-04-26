from pyscript import *


class Classmate: # class

        def __init__(self, name, section, favorite_subject):
            self.name = name # att
            self.section = section # att
            self.favorite_subject = favorite_subject # att
            

        def introduce(self): # method
                display(f'Hi I am {self.name} from  {self.section}. My favorite subject is {self.favorite_subject}.', target = 'output') # introduction text

# 5 pre-made classmates
# "|" to indicate what part of the string the program will have to apply the split function (.split)
classMate1 = Classmate('Malou|', 'Ruby|', 'Math')
classMate2 = Classmate('Margo|', 'Sapphire|', 'Science')
classMate3 = Classmate('Andrew|', 'Topaz|', 'Math')
classMate4 = Classmate('Adam|', 'Emerald|', 'Social Studies')
classMate5 = Classmate('Evie|', 'Ruby|', 'English')

# list to store all classmates
studentList = [classMate1.name + classMate1.section + classMate1.favorite_subject, classMate2.name + classMate2.section + classMate2.favorite_subject, classMate3.name + classMate3.section + classMate3.favorite_subject, classMate4.name + classMate4.section + classMate4.favorite_subject, classMate5.name + classMate5.section + classMate5.favorite_subject]

newMateInfo = ""

display('To Add New Classmate in the list: Input values to input fields then click Add Classmate button.', target = 'output', append = False)
display('To View complete list of Classmates: Click Show List button.', target = 'output', append = True)

def checkValue (value, dataList): # checking the value
    if (value in dataList):
        return True
    else: 
        return False

def addMate(event = None):
    if event:
        event.preventDefault() # to ensure that this area of the code will not be triggered by anything else but the user clicking the "Add Classmate" button
        pangalan = document.getElementById("inputClassmatee").value 
        
        if pangalan == "" or pangalan == " ": # checks if the user inputted anything in the classmate's name text box
            display('Please enter name of classmate', target = 'output', append = False) # "append = False" prevents the pre-made list of classmates from doubling/piling up in the output div 
        else:
            seksyon = document.getElementById("inputSection").value 
            paksa = document.getElementById("inputSubject").value
            newMateInfo = pangalan + "|" + seksyon + "|" + paksa # concatenates the newly added user inputs together
            
            if checkValue(newMateInfo, studentList) == True: # checks if the classmate entered by the user already exists in the list
                display('Classmate already exists in the list. Please enter a new classmate.', target = 'output', append = False)
            else:
                studentList.append(newMateInfo) # adds the newly added classmate into the studentList list
                display("New classmate added in the list. Click the Show List button to see complete list of classmates.", target = 'output', append = False)


def showList(event = None):
    if event:
        event.preventDefault()
        display("", target = 'output', append = False)
        for el in studentList:
            studName, studSection, studFaveSubj = el.split("|") # el.split is necessary for the program to know when to cut the input and put it in the proper variables so that it will be displayed properly
            newClassmates = Classmate(studName, studSection, studFaveSubj)        
            newClassmates.introduce()

