from pyscript import display, document


class classmates:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):  #creating a method
        display('Hello!', target='output')


classmate1 = classmates("Alice", "A", "Math")
classmate2 = classmates("Bob", "B", "Science")
classmate3 = classmates("Charlie", "C", "English")
classmate4 = classmates("David", "D", "History")
classmate5 = classmates("Eve", "E", "Art")

def add_classmate(e):
    input1 = document.getElementById("input1")
    input2 = document.getElementById("input2")
    input3 = document.getElementById("input3")
    
    name = input1.value
    section = input2.value
    subject = input3.value

    if name and section and subject:
        new_person = {
            "name": name,
            "section": section,
            "subject": subject
        }
        classmates.append(new_person)
        
        input1.value = ""
        input2.value = ""
        input3.value = ""
        
        display(f"{name} is now added!", target="listOutput", append=False)

def show_list(e):
    output_div = document.getElementById("listOutput")
    output_div.innerHTML = "<h3>📋 Classmate List</h3>"
    
    for i, person in enumerate(classmates, 1):
        formatted_entry = f"{i}) {person['name']}, {person['section']}, {person['subject']}"
        display(formatted_entry, target="listOutput", append=True)