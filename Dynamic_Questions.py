"""Dynamic Questions."""
from random import sample, choice, random, shuffle, randint
import Static_Questions

def check_answer(desired, guessed, error_margin):
    """Simple check to see if the desiered value is within the guess."""
    return (desired < guessed + error_margin and desired > guessed - error_margin)

def get_user_input(wanted_type):
    """Abstract away the loop asking the user for input."""
    while True:
        user_input = input("Please enter your value: ")
        if user_input == "q" or user_input == "exit":
            raise SystemExit  # Nasty way to kill the program :p
        try:
            if wanted_type == bool:
                if user_input.strip() in {"true","t","True","T","yes"}: return True
                if user_input.strip() in {"false","f","False","F","no"}: return False
                raise ValueError  # If not true or false
            if wanted_type == str:
                answer = user_input.strip().upper()
                if answer in {"A","B","C","D","E"}: return answer
                if user_input.strip() in {"true","t","True","T","yes"}: return "T"
                if user_input.strip() in {"false","f","False","F","no"}: return "F"
                raise ValueError  # If not one of the possible errors

            return wanted_type(user_input)  # Convert input to wanted_type
        except ValueError:
            if wanted_type == bool:
                print("Please give either true or false as your answer.")
            elif wanted_type == str:
                print("Please give either A B C D or T/F as your answer.")
            elif wanted_type == float:
                print("Please provide your answer as a number to 2 decimal places.")
            elif wanted_type == int:
                print("Please provide your answer as a whole number.")
            else:
                print("Error function called inccorectly. Called with {}".format(wanted_type))
                raise ValueError

def temperatures():
    """Module1 unit conversions with temperatures."""
    global correct_temperature
    C = randint(-2742, 4000)/10
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

    print("\n\nThis is a temperature question.\n")
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

    print("\n\nThis is a Pressure question.\n")
    print("For an Pressure of {:0.2f}{}\nPlease find its equivanlent value in{}".format(*P1,P2[1]))
    guess = get_user_input(float)

    if check_answer(P2[0], guess, 0.2):
        print("correct")
        correct_pressure += 1
    else:
        print("false the answer is {:0.2f}{}".format(*P2))

def fraction():
    """Module1 Mass and molar fractions."""
    global correct_fraction
    S1,S2,S3 = {"molar_mass":1.008, "name":"A"},{"molar_mass":16.00, "name":"B"},{"molar_mass":44.01, "name":"C"}
    M1,M2,M3 = randint(1,50),randint(1,20),randint(1,20)  # Really really shitty but I'm lazy rn
    total_mass = S1["molar_mass"]*M1 + S2["molar_mass"]*M2 + S3["molar_mass"]*M3

    print("\n\nThis is a mass and molar fractions question.\n")
    print("\nFor a substance made out of '{}' with a molar mass of '{}'".format(S1["name"], S1["molar_mass"]))
    print("'{}' with a molar mass of '{}'".format(S2["name"], S2["molar_mass"]))
    print("and '{}' with a molar mass of '{}'".format(S3["name"], S3["molar_mass"]))

    # Chance at being molar or mass fraction
    if choice([True, False]):
        print("If there are {} moles of {} what is the mass fraction of a substance weighing {:0.2f}g ?\n".format(M1, S1["name"],total_mass))
        guess = get_user_input(float)
        answer = (M1*S1["molar_mass"])/(total_mass)*100
    else:
        print("If the mass of {} is {} and {} is {} what is the molar fraction of {} \nin a substance weighing {:0.2f}g ?\n".format(S1["name"], M1*S1["molar_mass"], S2["name"], M2*S2["molar_mass"], S3["name"], total_mass))
        guess = get_user_input(float)
        answer = M1/(M1+M2+M3)*100

    if check_answer(guess,answer,0.3):
        print("correct")
        correct_fraction += 1
    else:
        print("false the answer is {:0.2f}".format(answer))

def flow_rate():
    """Module1 flow_rate."""
    print("\n\nThis is a flow rate question.\n")
    pass

def solve_mass_ballance(equation_type, d):
    """All posible equations for: input + generation = output + consumption + accumulation."""
    temp_out = ""
    t,r,p = equation_type
    for key,value in d.items():
        if value is None:
            print("Find the {}{} of {} when,\n".format(key, t, p))
        elif value != 0:  # Skip empty values
            temp_out += "{}{} is {} g{}\n".format(key, t, value, r)
    print(temp_out)

    if d["input"] is None:
        return d["output"] + d["consumption"] + d["accumulation"] - d["generation"]
    elif d["generation"] is None:
        return d["output"] + d["consumption"] + d["accumulation"] - d["input"]
    elif d["output"] is None:
        return d["input"] + d["generation"] - d["consumption"] - d["accumulation"]
    elif d["consumption"] is None:
        return d["input"] + d["generation"] - d["output"] - d["accumulation"]
    elif d["accumulation"] is None:
        return d["input"] + d["generation"] - d["consumption"] - d["output"]

def simple_mass_ballance():
    """Mass ballance with one equation and one unknown."""
    global correct_simple_mass
    print("\n\nThis is a simple system ballance question.\n")

    all_variables = {"input":randint(0,10), "output":randint(0,10), "generation":0, "consumption":0, "accumulation":0}
    K1,K2,K3 = tuple(sample(set(all_variables.keys()), 3))
    all_variables[K1] = randint(1,450)
    all_variables[K2] = randint(1,450)
    all_variables[K3] = None  # The variable to be found
    equation_type = choice([("","",choice(["Steel","Chemical A"])), ("rate","/s", choice(["Sewage","Pepsi","Chemical A flow", "Glue", "Glowing Substance", "H2SO4"]))])

    answer = solve_mass_ballance(equation_type, all_variables)
    guess = get_user_input(float)

    if check_answer(guess,answer,0.3):
        print("correct")
        correct_simple_mass += 1
    else:
        print("false the {}{} is {} g{}".format(K3,equation_type[0], answer,equation_type[1]))

def complex_mass_ballance():
    """Mass ballance with two or more equations."""
    global correct_complex_mass
    print("\n\nThis is a complex system ballance question.\n")

    all_variables = {"input":randint(0,10), "output":randint(0,10), "generation":0, "consumption":0, "accumulation":0}
    K1,K2,K3 = tuple(sample(set(all_variables.keys()), 3))
    all_variables[K1] = randint(1,450)
    all_variables[K2] = randint(1,450)
    all_variables[K3] = None  # The variable to be found
    equation_type = choice([("","",choice(["Steel","Chemical A"])), ("rate","/s", choice(["Sewage","Pepsi","Chemical A flow"]))])

    answer = solve_mass_ballance(equation_type, all_variables)
    guess = get_user_input(float)

    if check_answer(guess,answer,0.3):
        print("correct")
        correct_complex_mass += 1
    else:
        print("false the {}{} is {} g{}".format(K3,equation_type[0], answer,equation_type[1]))

def premade():
    """List of premade questions- if you get one right its removed from potential questions."""
    global all_questions

    choice(all_questions)
    temp = all_questions.pop(0)  # Treat scrambled list like a queue
    question,answer = temp
    print("\n\n{}".format(question))
    guess = get_user_input(str)

    if guess == "T": guess = True
    if guess == "F": guess = False

    if guess == answer:
        print("Correct the answer is: {}".format(answer))
    else:
        print("Incorrect the answer is: {}, This question will be asked again.".format(answer))
        all_questions.append(temp)  # Add it back


all_questions = Static_Questions.get_all_questions()
shuffle(all_questions)
correct_temperature = 0
correct_pressure = 0
correct_fraction = 0
correct_simple_mass = 0
correct_complex_mass = 0
