from pyscript import display, document


classmates = [
    {"name": "Jennifer", "section": "Sapphire", "subject": "PE"},
    {"name": "Cheska", "section": "Sapphire", "subject": "English"},
    {"name": "Sofie", "section": "Sapphire", "subject": "Math"},
    {"name": "Michaela", "section": "Sapphire", "subject": "SS"},
    {"name": "Neriza", "section": "Sapphire", "subject": "CAT"},
]

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
        
        display(f"{name} is now added.", target="list", append=False)

def show_list(e):
    output = document.getElementById("list")
    output.innerHTML = "<h2>Classmate List</h2>"
    
    for i, person in enumerate(classmates, 1):
        formatted_entry = f"{i}) {person['name']}, {person['section']}, {person['subject']}"
        display(formatted_entry, target="list", append=True)
