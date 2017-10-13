"""Console program designed to generate and ask random chem eng questions then check your answers for them."""
from random import sample, randrange, choice, random, shuffle
from time import sleep
import Static_Questions

def check_answer(desired, guessed, error_margin):
    return (desired < guessed + error_margin and desired > guessed - error_margin)

def get_user_input(wanted_type):
    """Abstract away the loop asking the user for input."""
    while True:
        user_input = input("Please enter your value: ")
        if user_input == "q" or user_input == "exit":
            raise SystemExit
        try:
            if wanted_type == bool:
                if user_input.strip() in {"true","t","True","T","yes"}: return True
                if user_input.strip() in {"false","f","False","F","no"}: return False
                raise ValueError  # If not true or false

            return wanted_type(user_input)  # Convert input to wanted_type
        except ValueError:
            print("Please enter a {}".format(wanted_type))

def temperatures():
    """Module1 unit conversions with temperatures."""
    global correct_temperature
    C = randrange(-2742, 4000, 1)/10
    K = C + 273.15
    F = C * 1.8 + 32
    R = F + 459.67
    all_temperatures = [(C," Celcuis"), (F," Fahrenheit"), (K," Kelvin"), (R," Ranken")]
    T1,T2 = tuple(sample(set(all_temperatures), 2))

    # Chance of being a interval question instead
    if choice([True, False]):
        if T1[1] is " Celcuis" or T1[1] is " Kelvin":
            T2 = (T1[0] * 1.8, choice([" A Fahrenheit Interval", " A Ranken Interval"]))
        else:
            T2 = (T1[0] / 1.8, choice([" A Celcuis Interval", " A Kelvin Interval"]))

    print("\nThis is a temperature question.\n")
    print("For an temperature of {:0.2f}{}\nPlease find its equivanlent value in{}".format(*T1,T2[1]))
    guess = get_user_input(float)

    if check_answer(T2[0], guess, 0.2):
        print("correct")
        correct_temperature += 1
    else:
        print("false the answer is {:0.2f}{}".format(*T2))

def pressure():
    """Module1 Pressure unit conversions."""
    global correct_pressure
    atmg = random()
    mmHgg = atmg * 760
    Kpag = atmg * 101.325
    barg = atmg * 1.01325
    psig = atmg * 14.696
    all_pressure = [(mmHgg," mmHg gage"),
                    (atmg," atm gage"),
                    (Kpag," Kpa gage"),
                    (psig," psi gage"),
                    (barg," bar gage"),
                    (mmHgg - 760," mmHg absolute"),
                    (atmg - 1," atm absolute"),
                    (Kpag - 101.325," Kpa absolute"),
                    (psig - 14.696," psi absolute"),
                    (barg - 1.01323," bar absolute")]
    P1,P2 = tuple(sample(set(all_pressure), 2))

    print("\nThis is a Pressure question.\n")
    print("For an Pressure of {:0.2f}{}\nPlease find its equivanlent value in{}".format(*P1,P2[1]))
    guess = get_user_input(float)

    if check_answer(P2[0], guess, 0.2):
        print("correct")
        correct_pressure += 1
    else:
        # TODO FIX decimal places?
        print("false the answer is {:0.2f}{}".format(*P2))


A = {"molar_mass":44.01, "name":"A"}
B = {"molar_mass":12.02, "name":"B"}
C = {"molar_mass":16.00, "name":"C"}
D = {"molar_mass":23.5, "name":"D"}
def fraction():
    """Module1 Mass and molar fractions."""
    substances = [A, B, C, D]
    units = {"lb mole":1, "lb":1, "kg":0.45359237, "kg mole":1}

    substance = choice(substances)
    print("\nThis is a mass and molar fractions question.\n")
    print("For a substance '{}' with a molar mass of '{}'\n".format(substance("name"), substance("molar_mass")))
    print("What is the ")
    pass

def flow_rate():
    """Module1 flow_rate."""
    print("\nThis is a flow rate question.\n")
    pass

def premade():
    """List of premade questions- if you get one right its removed from potential questions."""
    global all_questions

    choice(all_questions)
    temp = all_questions.pop(0)  # Treat scrambled list like a queue
    question,answer = temp
    print("\n\n{}".format(question))
    guess = get_user_input(type(answer))
    if guess is answer:
        print("Correct the answer is: {}".format(answer))
    else:
        print("Incorrect the answer is: {}, This question will be asked again.".format(answer))
        all_questions.append(temp)  # Add it back


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("This is the B-Tech Chem Eng study program.")
print("It should ask you as many random unit test questions to help you study for the first midterm")
print("At any time you can type 'q' or 'exit' to exit the program")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
# Main loop
all_questions = Static_Questions.get_all_questions()
shuffle(all_questions)
correct_temperature = 0
correct_pressure = 0

while True:
    # I know this is an ugly setup with a list of functions and global counters.
    # But honestly this looks nicer/I don't have to set up a load of if statements.
    types_of_questions = [temperatures(), pressure(), premade()]
    choice(types_of_questions)
    if all_questions is None:
        types_of_questions.remove(premade())
    if correct_temperature == 6:
        types_of_questions.remove(temperatures())
    if correct_pressure == 6:
        types_of_questions.remove(pressure())
