# -----------------------------------------+
# Brendan Smith                            |
# -----------------------------------------|
# Program that helps me learn python and   |
# how to play the saxophone                |
# -----------------------------------------+

# the possible musical notes
POSSIBLE_NOTES = ['A','a', 'A#', 'a#', 'B', 'b', 'C', 'c', 'C#', 'c#', 'D',
                  'd','D#','d#', 'E','e', 'F','f', 'F#','f#','G','g', 'G#', 'g#']

#Simple Fingering Chart
simple_fingering_chart = ['B = 1\n',
                          "A = 2\n"
                          "G = 3\n"
                          "F = 4\n"
                          "E = 5\n"
                          "D = 6\n"]

#makes musical staff
make_staff = ["____________________________________________________________________\n",
              "____________________________________________________________________\n",
              "____________________________________________________________________\n",
              "____________________________________________________________________\n",
              "___________________________________________________________________\n"]

print(POSSIBLE_NOTES)
print(simple_fingering_chart)
print(make_staff)

q1 = input("what size reid should you have when starting off?")
if(q1 == 2 | 2.5 | 3):
    print("correct sir")
q2 = input("true or false: its good to soak your reid in amber listerine")
if (q2 == "true"):
    print("yes!")
else:
    ("no sir")

q3 = input("what is the fingering chart")
if(q3 == "BAGFED"):
    print("gold star***")


