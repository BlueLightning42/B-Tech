from random import sample, randrange, choice, random

def check_answer(desired, guessed, error_margin):
    return (desired < guessed + error_margin and desired > guessed - error_margin)

def get_user_input(wanted_type):
    while True:
        user_input = input("Please enter your value: ")
        if user_input == "q" or user_input == "exit":
            raise SystemExit
        try:
            return wanted_type(user_input)
        except ValueError:
            print("Please enter a {}".format(wanted_type))

def temperatures():
    """Module1 unit conversions with temperatures"""
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
    else:
        print("false the answer is {:0.2f}{}".format(*T2))

def pressure():
    """Module1 Pressure unit conversions"""
    atmg = random()
    mmHgg = atmg * 760
    Kpag = atmg * 101.325
    barg = atmg * 1.01325
    psig = atmg * 14.696
    all_pressures = [(mmHgg," mmHg gage"), (atmg," atm gage"), (Kpag," Kpa gage"), (psig," psi gage"), (barg," bar gage"), (mmHgg-760," mmHg absolute"), (atmg-1," atm absolute"), (Kpag-101.325," Kpa absolute"), (psig-14.696," psi absolute"), (barg -1.01323," bar absolute")]
    P1,P2 = tuple(sample(set(all_pressures), 2))

    print("\nThis is a Pressure question.\n")
    print("For an Pressure of {:0.2f}{}\nPlease find its equivanlent value in{}".format(*P1,P2[1]))
    guess = get_user_input(float)

    if check_answer(P2[0], guess, 0.2):
        print("correct")
    else:
        # TODO FIX decimal places?
        print("false the answer is {:0.2f}{}".format(*P2))


def fraction():
    """Module1 Mass and molar fractions"""
    print("\nThis is a mass and molar fractions question.\n")

    pass

def flow_rate():
    """Module1 flow_rate"""
    print("\nThis is a flow rate question.\n")
    pass


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("This is the B-Tech Chem Eng study program.")
print("It should ask you as many random unit test questions to help you study for the first midterm")
print("At any time you can type 'q' or 'exit' to exit the program")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
# Main loop
while True:
    choice([temperatures(), fraction(), flow_rate(), pressure()])
