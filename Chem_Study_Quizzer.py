"""Console program designed to generate and ask random chem eng questions then check your answers for them."""
from Dynamic_Questions import temperatures, pressure, fraction, premade, simple_mass_ballance
import Dynamic_Questions as q
from random import choice

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("This is the B-Tech Chem Eng study program.")
print("It should ask you as many random unit test questions to help you study for the first midterm")
print("At any time you can type 'q' or 'exit' to exit the program")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

while True:
    # I know this is an ugly setup with a list of functions and global counters.
    # But honestly this looks nicer/I don't have to set up a load of if statements.
    # Was thinking of having a list of tuples with (func,counter) then returning the counter each time etc...
    # counter = func(counter) but that seems ugly just to maintain the correct OOP...
    # and again I want to randomly chose each function so this seems the best.
    types_of_questions = [simple_mass_ballance,premade,pressure,temperatures,fraction]
    choice(types_of_questions)()  # Randomly calls one of the functions
    if not q.all_questions:
        types_of_questions.remove(premade)
    elif q.correct_temperature >= 4:
        types_of_questions.remove(temperatures)
    elif q.correct_pressure >= 4:
        types_of_questions.remove(pressure)
    elif q.correct_fraction >= 2:
        types_of_questions.remove(fraction)
    elif q.correct_simple_mass >= 4:
        types_of_questions.remove(simple_mass_ballance)

    if not types_of_questions:
        print("\n  - You have finished all the questions!")
        print("  - You are ready for the midterm...")
        break  # End program
    else:
        input("\n- Hit enter to get your next question. -\n")
