"""Storage module to contain all the unchanging questions."""

# List of true or questions along with thire answer.
true_false_questions = [
 ("Is [Input Rate + Generation Rate == Output Rate + Consumption Rate + Accumulation Rate] a Integral Balance Question? T/F", False),
 ("An Integral Ballance Has units of the Ballanced quatity (Amount of input vs rate)? T/F", True),
 ("If there are zero degrees of freedom the question can easily be solved? T/F", True),
 ("Can a question with 2 degree of freedom be solved right away? T/F", False),
 ("Are more degrees of freedom good? They make you more free so you can do more stuff? T/F", False),
 ("Is this correct? An Integral Ballance Is typically applied to continuous processes while a Differential is applied to Batch processes? T/F", False),
 ("Henry's Law is Pa = Ya×P = Xa×Ha(T) is it valid when Xa is close to 1 T/F", False),
 ("Raults's Law is Pa = Ya×P = Xa×Pa*(T) is it valid when Xa is close to 1 T/F", True),
 ("A Closed System Means no mass crosses the system boundairy T/F", True),
 ("Heat is Positive if its transfered from the suroundings to the system T/F", True),
 ("Work is Positive if its transfered from the suroundings to the system T/F", False)
]

# List of multiple choice questions along with thire answer.
multiple_choice_questions = [
 ("""Which of the following are incorrect for a Differential Ballance Question.
 [A]♦ All units are divided per time.
 [B]♦ Provides what happens at every instance in time.
 [C]♦ Proves what happens Between two instances in time.
 [D]♦ Typically applied to continuous processes.
 ""","C"),
 ("""Which of the following is a Extensive Property
 [A]♦ Temperature
 [B]♦ Pressure
 [C]♦ Volume
 [D]♦ Age
 ""","C"),
 ("""Which of the following are incorrect?
 [A]♦ If a substance is total mass Generation is = Accumulation.
 [B]♦ If a system is in steady state Accumulation = 0
 [C]♦ If a substance is nonreactive Generation = Consumption = 0
 [D]♦ If a system is in steady state total mass is Input = Output.
 ""","A")
]

def get_all_questions():
    """Return all questions stored in this file."""
    return multiple_choice_questions + true_false_questions
