class Person:
    def __init__(self, fn, ln, intersts = [], role='student'): #constructor
        self.first_name = fn
        self.last_name = ln
        self.intersts = intersts
        self.role = role

    # a build in function in python we are overriding and customizing
    def __repr__(self):
        return f"first name: {self.first_name}, last name: {self.last_name}, role: {self.role}"

class Lecture:
    def __init__(self, lecturer, topic, start_time, location, atendees=[]):
        self.lecturer = lecturer
        self.topic = topic
        self.start_time = start_time
        self.location = location
        self.atendees = atendees
    
    def __repr__(self):
        return f"lecture is about {self.topic} by {self.lecturer} starting at {self.start_time} at {self.location}"
    
nadia = Person("Nadia", "N") #instance of Person class

# print(nadia)

this_lecture = Lecture(nadia, "python oop", "10:30 ish", "fish bowl",
    [
        Person("Matthew", "Merrill", ["coding","baseball","reading"]),
        Person("Jimmy","Lam", ["coding","soccer","coffee","food"]),
        Person("Henry","Le", ["ping pong","energy drinks","martial arts"])
    ]
)

for people in this_lecture.atendees:
    # print(people)
    # print(people.first_name)
    # print(people.first_name, people.last_name)
    if people.first_name=="Jimmy":
        for intrest in people.intersts:
            if intrest=="soccer":
                print("Jimmy loves soccer")

for i in range(len(this_lecture.atendees)):
    if i==1:
        print(this_lecture.atendees[i])