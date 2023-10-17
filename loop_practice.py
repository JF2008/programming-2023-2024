# Loop practice
# 10/10/2023
# Jonathan Feng

import random

groceries = ["hot wheels", "lego", "ice cream", "video games"]

for item in groceries:
    print(f"* {item}")
    print("  ---")


stars = ["*", "**", "***", "****", "*****"]

for row in stars:
    print(row)

#Happy new year exercise bot

import time

for i in range(10):
    print(10 - i)
    time.sleep(1)
print("happy new year!")


names = ['Anthony Maldonado', 'Randy Love', 'Christopher Valdez', 'Rodney Odom', 'Kimberly Ramos', 'Lisa Ray', 'Kevin Terry', 'Gregory Romero', 'Debbie Harris', 'Edwin Hall', 'Mark Myers', 'Lisa Long', 'Stephanie Watson', 'Katherine Fields', 'Kathryn Olson', 'Maurice Baxter', 'Russell Caldwell', 'Heather Griffin', 'Kara Lane', 'Mark Tucker', 'Kathryn Rodriguez', 'Rachael Daniels', 'Debra Whitaker', 'Angela Neal', 'Michelle Hall', 'Jessica Olson', 'Lynn Jensen', 'Marc Ray', 'Valerie Harris', 'Tina Webb', 'Donna Green', 'Derek Mcgee', 'Tammy Hall DVM', 'Christopher Johnston', 'Eric Smith', 'Matthew Lopez', 'Mary Smith', 'Dr. Heather Ramos MD', 'Eric Johnson', 'Dylan Alvarado', 'Aaron Huff', 'Robin James', 'Sandra Stevens', 'Scott Thomas', 'Philip Nelson', 'Marcus Martin', 'Mary Alexander', 'Jason James', 'Samantha Burch', 'Jessica Martinez', 'Jose Wright', 'Zachary Pineda', 'William Ramos', 'Shelby Hughes', 'Melanie Moore', 'Kimberly Fowler', 'Jordan Jones', 'Brenda Anderson', 'Russell Coleman', 'Jeremy Snow', 'Billy Wu', 'Jesse Rodriguez', 'Andrew Shea', 'Jason Castillo', 'Donald Abbott', 'Richard Cervantes Jr.', 'Jeffrey Powell', 'Angel Fernandez', 'Michelle Donovan', 'Mr. Michael Wagner DDS', 'Kimberly Gonzalez', 'Thomas Smith', 'Nichole Barnes', 'Shelly Clark', 'Ashley Ortiz', 'Jessica Lam', 'Kimberly Ray MD', 'Mason Kennedy', 'Whitney Harrington', 'Nicole Tran', 'Robert Montgomery', 'Ryan Gardner', 'Kimberly Silva', 'Stephanie Rivera', 'William Santos', 'Ashley Mcclain', 'Sophia Williams', 'Kevin Herring', 'Tyrone Leonard', 'Carolyn Jones', 'Stephanie Willis', 'Jon Lang', 'Tammy Porter', 'Robert Garcia', 'Casey Brown', 'Benjamin Aguilar', 'Nancy Norman', 'Aaron Peters', 'Blake Graham', 'Noah Harper DDS', 'Dwayne Ortiz', 'Melissa Padilla', 'Rebecca Jones', 'Michael Wood', 'Daniel Bean', 'Alexander Kaufman', 'Michael Higgins', 'Richard Bailey', 'Jay Cisneros', 'Lisa Acevedo', 'Sarah Hernandez', 'Bryan Jones', 'Mark Kennedy', 'Robert Caldwell', 'Larry Wolf', 'Robert Adkins', 'Wanda Doyle', 'Thomas Brown', 'Kevin Key', 'Stacey Fisher', 'Amber Hart', 'Paul Russell', 'Jacqueline David', 'Shannon Parker', 'Lisa Sanchez', 'Jennifer Atkins', 'Jason Woods', 'Richard Garcia', 'Luis Williams', 'Marco Weaver', 'Amy Hayes', 'Elizabeth Doyle DDS', 'Nicole Smith', 'Karen Thomas', 'Randy Reese', 'Deanna Rodriguez', 'Christian Conway', 'Craig Doyle', 'Dennis Oneill', 'Diane Jordan', 'Patrick Holder', 'Christina Thompson', 'Deanna Lee', 'Kathleen Davis', 'Brian Cox', 'Kristen Thomas', 'Samantha Smith', 'William Moss', 'Matthew Flowers', 'Megan Powell', 'Richard Williamson', 'Cindy Glenn', 'John Taylor', 'Nathaniel Lee', 'Sara Glover', 'James Jackson II', 'Carlos Henderson', 'Edward Holder', 'Whitney Hansen', 'Matthew Jacobs', 'Raymond Rodriguez', 'Christy Kennedy', 'Lisa Johnson', 'Mark Harris', 'Stephen Bowers', 'Derrick Brown', 'Stephen Schroeder', 'Martin Lawrence', 'Brian Reed', 'Trevor Booker', 'Ruben Johnson', 'Jeffrey Griffith', 'William Townsend', 'Cynthia Park', 'Carla Yang', 'Oscar Hartman', 'Shawn Hendricks', 'Timothy Oconnor', 'Gina Robertson', 'Jennifer Rodriguez', 'Jared Harris', 'Austin Austin', 'Nathan Golden', 'Samantha Flores', 'Alexis Jones', 'Susan Rice', 'Randall Holmes', 'Connie Johnson', 'Carol Young', 'Brandon Norris', 'Timothy Lester', 'Dustin Mccarthy', 'Tammy Brock', 'Heather Cummings', 'John Moreno', 'Dawn Berry', 'Jeffrey Montes', 'Joshua Smith', 'Alexa Barber', 'Mark Lewis']

target = ""
for item in names:
    if item == target:
        print(f"Hey we found {target}!")
        break
else:
    print("item not found")


for i in range(1, 100, 2): #start, stop, count by x number
    print(i)

#print all even numbers between 1200 and 1500
for i in range(1200, 1501, 2):
    print(i)
#print all odd numbers between -150 and 0
for i in range(-149, 0, 2):
    print(i)

#This is example of Boolean Statement
print("\n")

Value = random.randint(1,2)
Boolean = False

if Value == 1:
    Boolean = True
if Value == 2:
    Boolean = False

print("Boolean statement is: ")
print(Boolean)








