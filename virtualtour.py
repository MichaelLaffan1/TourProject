#Marist Virtual Tour

#Location Class
class Location:
    def __init__(self, name, description, details):
        self.name = name
        self.description = description
        self.details = details

#Locations List
locs = [Location("Murray Student Center", '''Our first location here is the Murray Student Center. This location   
serves as the center point of the college. It brings together all
the members of Marist College. It provides various student services
and serves as a place where students can meet and organize events.
Some of these services include dining services, student lounge,
the campus post office, and the campus bookstore.''', '''The dorms that are adjacent to the Student Center are Champangat Hall
and Midrise Hall. Champagnat is a freshman residence consisting of nine floors and has
rooms consisting of doubles. Midrise hall is a suite style residence hall and houses
freshman, sophomore and transfer students.'''), Location("Donnelly Hall", '''Our next location here is Donnelly Hall. This location mainly houses
our technology services and other offices that are available to
our students here on campus. Some of these services include
Financial services, the Help Desk, Advising and Academic Services
and the Computer Lab.''', '''The other services we have available here are the Accomodations
and Accessibility, the Registrar office, Safety and Security, ResNet, and
Business and Financial Affairs.'''), Location("Hancock Center", '''Our next location here is the Hancock Center. This location is
for our School of Computer Science and Mathematics. However, it also
houses our Study Abroad offices, which manages our programs for students
who want to go and study in another country, such as our campus in
Florence, Italy. It also houses our Investment Center and Trading Room
and our Center for Teaching Excellence.''', '''Our Study Abroad locations include Japan, Italy, Greece, France,
Australia, Spain, and China.'''), Location("McCann Center", '''Our next location here is the McCann Center. This location is mostly
known to be our sports center here on campus. It houses our Athletic
Department, our fitness center, our Center for Sports Medicine, and
other sports services. It also houses our Admissions Visitor Center
for people who come to visit our campus.''', '''The primary sports that are available here at Marist are
basketball, soccer, volleyball, flag football, and softball.'''), Location("Cannavino Library", '''Our next location here is the Cannavino Library. This location serves
as our main library here on campus. It also serves as a place where
students can catch up on their work and study without any distractions.
It also houses our Center for Career Services, Center for Multicultural
Affairs, and our Digital Education services.''', '''The library has a tool called Fox Hunt that allows you to
look for any book that is available in the library. It also allows you to
access any workshop that gives you information about other services we have
here on campus such as counseling.'''), Location("Chapel", '''Our next location here is the Chapel. The Chapel serves as an
Inter-Faith Prayer room, where anyone can come in for quiet
prayer from 7 am to 10 pm. It also provides Mass services
Monday through Thursday at 12:15 pm and on Sundays at both
12 pm and 6:30 pm.''', '''The Chapel hosts spirit groups for men, women, and different
faiths. Some of the topics discussed in these spirit groups are personal
identity, transitions into college, and sprituality.'''), Location("McCormick Hall", '''Our next location here is McCormick Hall. This location serves as a
residence hall for our upperclassmen. Unlike the freshman residence
halls we have here on campus, residents of this hall are responsible
for their own cooking and cleaning of their apartment. This location
also serves as one of our dining locations here on campus, also
known as North End Dining.''', '''Some of our food options that are available at North End
Dining are cheese quesadillas, cheeseburgers, crispy chicken sandwich,
and cheese and pepperoni pizza.'''), Location("Steel Plant Studios and Gallery", '''Our next location is the Steel Plant Studios and Gallery, commonly
known as the Steel Plant. This building mainly houses our fashion
and design programs that we have available here on campus. It also
houses our Art Gallery and our Digital Media and Fine Arts programs
here as well.''', '''The Art Gallery is a 3200 square foot art exhibition space
and retains the industrial look of the former steel plant. It focuses on
contemporary regional artists working in fine arts media.'''), Location("Science and Allied Health Building", '''Our next location here is the Science and Allied Health Building.
This building mainly houses our science and medical field programs.
It also houses our School of Science and our labratories such as the
Cognitive Computing Lab and Gross Anatomy Lab. Anyone interested in
the medical field will likely take most of their classes here.''', '''Our Physician Assistant program is a 24 month, full time program
designed to prepare our students for clinical practice. Students learn how to
care in a variety of settings such as in the operating and emergency room.'''), Location("Dyson Center", '''Our last location that I will be showing you here at Marist College
is the Dyson Center. This building houses our School of Management
and School of Social and Behavioral Sciences. It also houses our
Teacher Education Program for any students that wish to pursue a
career in teaching and it also has a coffee shop.''', '''Some of our programs of study for our education majors is the
Adolescence Education program, Special Education program, and M.A.s in Education
Psychology and Initial Teaching Certification.''')]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

location = 0
count = 0
commands = "Here are a list of valid commands: 'help', 'map', 'details', 'quit', or an integer that corresponds to a valid location."

#Intro Function
def intro():
    print("Marist Virtual Tour")
    print("Hello everyone! Welcome to Marist College. I'll be your tour guide as I show you some of our locations here on campus. Enjoy the tour.")
    print()
    print(commands)
    print()

#Closing Function   
def closing():
    print('''Thank you everyone for visiting Marist College. I hope you enjoyed
the tour and consider applying to Marist College. Goodbye!''')

#Continue Function
def prompt():
    c = "Press enter to continue: "
    print(input(c))
    
#Visit Function
def visit():
    global count
    count = count + 1

#Move Function
def move():
    global location
    global count 
    print()
    print(locs[location].name)
    print()
    print("You have visited", count, "locations.")
    print()
    print(locs[location].description)
    print()

#Command Function
def command():
    while True:
        n = input("Enter a command: ").lower()
        n.strip()
        if len(n) > 0:
            return n

#Help Command Function
def showHelp():
    print(commands)

#Map Command Function
def showMap():
    print(numbers)
    for i in range(len(locs)):
        print(locs[i].name)

#Details Command Function
def showDetails():
    print(locs[location].details)

#Quit Command Function
def quitTour():
    q = input("Press Q to end the tour. Otherwise, it will restart: ").upper()
    if q == 'Q':
        closing()
        quit()
    else:
        location = 0
        count = 0


log = {
    'help': showHelp,
    'map': showMap,
    'details': showDetails,
    'quit': quitTour
    }

#Main Function 
def main():
    global location
    global count
    
    #Title and Introduction
    intro()
    prompt()
    
    #Loop
    while True:
        cmd = command()
        if cmd.isdigit():
            location = int(cmd) - 1
            visit()
            move()
        else:
            try:
               action = log[cmd]
               action()
            except:
                print("Invalid command.")


main()
