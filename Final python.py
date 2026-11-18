"""
PYTHON BASICS FOR BEGINNERS
Pick a lesson (1-7). Each lesson has its own quiz and mini game!
Run it with:  python python_lessons.py
"""

import random

# ---------------------------------------------------------------
# LESSONS
# ---------------------------------------------------------------
LESSONS = {
    1: ("Introduction to Programming", '''
A programming language is how we give instructions to a computer.
Examples: Python, C/C++, PHP, Java, JavaScript, Ruby.

Python was created by Guido van Rossum in 1991. He wanted it to be
simple, readable, and easy to learn.

Python is:
  - high-level   (close to human language)
  - interpreted  (runs your code line by line)
  - general-purpose (can be used for almost anything)

Why learn Python?
  1. Easy to learn, great for beginners
  2. Code reads almost like English
  3. Used in AI, websites, automation, games, and more
  4. Huge community with lots of help online

Tools to start coding: PyCharm, VS Code, Jupyter Notebook.
'''),

    2: ("Python Basic Syntax", '''
Syntax = the grammar rules of Python.

1. Python is CASE-SENSITIVE
     name = "John"
     print(name)   # works
     print(Name)   # ERROR, 'Name' is not 'name'

2. INDENTATION matters
   Python uses spaces to show which code belongs together.
     if True:
         print("This line is indented, so it belongs to the if")

3. print() shows things on the screen
     print("Hello, World!")   # text needs quotes
     print(100)               # numbers do not

4. COMMENTS are notes for humans. Python ignores them.
     # this is a single-line comment
     """ this is a
         multi-line comment """

5. VARIABLES are named boxes that store data
   Naming rules:
     - start with a letter or underscore (_)
     - never start with a number
     - no spaces or symbols like # or @
     - age and AGE are two different variables
'''),

    3: ("Arithmetic Operators", '''
Operators are symbols that do math. An expression is a mix of
values, variables, and operators that gives a result.

   +    add                10 + 5   = 15
   -    subtract           10 - 5   = 5
   *    multiply           10 * 5   = 50
   /    divide             10 / 5   = 2.0   (always a decimal)
   //   floor divide       10 // 3  = 3     (drops the decimals)
   %    modulus            10 % 3   = 1     (the remainder)
   **   power              2 ** 3   = 8

Example: average of three grades
   average = (90 + 85 + 88) / 3     # 87.67

Python follows PEMDAS: brackets first, then powers, then
multiply/divide, then add/subtract.
'''),

    4: ("Basic Input and Output", '''
input() lets your program ask the user for something.

   name = input("Enter your name: ")

IMPORTANT: input() ALWAYS gives you text (a string), even if the
user types a number.

Showing results with print() and commas:
   print("Name:", name)

Need a number? Convert it:
   age   = int(input("Enter your age: "))      # whole number
   grade = float(input("Enter your grade: "))  # decimal number
'''),

    5: ("Conditional Statements", '''
Conditional statements let a program make decisions. It runs code
only when a condition is True or False.

RELATIONAL (COMPARISON) OPERATORS
They compare two values and always give True or False:
   ==   equal to
   !=   not equal to
   >    greater than
   <    less than
   >=   greater than or equal to
   <=   less than or equal to
Example: score = 85, then score >= 75 gives True

1) if STATEMENT
   Runs the indented block only if the condition is True.
   If it is False, the block is skipped.

   Syntax:
      if condition:
          statement(s)

   Example:
      age = 20
      if age >= 18:
          print("You are an adult.")

2) if-else STATEMENT
   Gives another block to run when the if condition is False.
   Only ONE block runs.

   Syntax:
      if condition:
          statement
      else:
          statement

   Example:
      score = 65
      if score >= 75:
          print("Passed")
      else:
          print("Failed")

3) if-elif-else STATEMENT
   Used for many conditions. Python checks from top to bottom,
   runs the FIRST True block, and skips the rest.

   Syntax:
      if condition1:
          statement
      elif condition2:
          statement
      else:
          statement

   Example (grading system):
      score = 88
      if score >= 90:
          print("Excellent")
      elif score >= 80:
          print("Very Good")
      elif score >= 75:
          print("Passed")
      else:
          print("Failed")
'''),

    6: ("Logical Operators", '''
Logical operators combine or flip True/False conditions. They are
often used with if, elif, and else.
Python has three: and, or, not.

and OPERATOR
   True only when ALL conditions are True. If any one is False,
   the whole result is False.
   Example: age >= 18 and age <= 60   (both must be True)
   Truth rule: True and True = True. Every other combination
   gives False.

or OPERATOR
   True if AT LEAST ONE condition is True. It is False only when
   every condition is False.
   Example: day == "Saturday" or day == "Sunday"
   Truth rule: if any side is True, the result is True.

not OPERATOR
   Reverses the result: True becomes False, False becomes True.
   Example: if not is_raining:
            runs when is_raining is False.

QUICK GUIDE
   and -> all true
   or  -> at least one true
   not -> flip the result
'''),

    7: ("Loops (Iteration)", '''
Iteration means repeating a set of instructions. Every repeat is
called an iteration. Loops save you from writing the same code
again and again.
Python has two main loops: the for loop and the while loop.

for LOOP
   Use it when you already know how many times to repeat. It runs
   once for each item in a sequence, like range().

   Syntax:
      for variable in sequence:
          indented code

   Example:
      for number in range(3):
          print("Welcome to Python!")

   range(start, stop, step)
      - the stop value is NOT included
      - you can count forward or backward
      range(1, 6)       gives 1 2 3 4 5
      range(5, 0, -1)   gives 5 4 3 2 1

while LOOP
   Repeats only while a condition stays True. It checks the
   condition BEFORE running the block.
   while True repeats forever, so use break to stop it.

   Example: keep asking for a name until the user types X.
      while True:
          name = input("Name (X to exit): ")
          if name.upper() == "X":
              break
          print("Hello,", name)

QUICK GUIDE
   iteration = repetition of code
   for       = fixed number of repeats
   while     = repeat based on a condition
'''),
}

# ---------------------------------------------------------------
# QUIZZES: one set per lesson
# Each question: (question, [(option, explanation), ...], index of correct option)
# Every option has its own explanation, shown after the player answers.
# ---------------------------------------------------------------
QUIZZES = {
    1: [
        ("Who created Python?",
         [("Guido van Rossum", "Yes! Guido, a Dutch software engineer, created Python in 1991."),
          ("Bill Gates", "No. Bill Gates co-founded Microsoft. He did not create Python."),
          ("Linus Torvalds", "No. Linus Torvalds created Linux, an operating system.")], 0),
        ("Which describes Python best?",
         [("High-level, interpreted, general-purpose", "Right! It is close to human language, runs line by line, and works for almost anything."),
          ("Low-level and only for websites", "No. Python is high-level and can do much more than websites."),
          ("A photo editing program", "No. Python is a programming language, not an app.")], 0),
        ("Which one is NOT a programming language?",
         [("PyCharm", "Correct! PyCharm is a tool (an editor) you use to WRITE code."),
          ("JavaScript", "No. JavaScript is a programming language."),
          ("Ruby", "No. Ruby is a programming language.")], 0),
        ("Why is Python great for beginners?",
         [("Its code is readable, almost like English", "Yes! Simple, readable syntax is the main reason."),
          ("It has no community or tutorials", "No. Python has a HUGE community with lots of help."),
          ("It can only run tiny programs", "No. Python is used for AI, web, automation, games, and more.")], 0),
    ],
    2: [
        ("name = \"John\", then you run print(Name). What happens?",
         [("An error, because Python is case-sensitive", "Correct! Name and name are different to Python."),
          ("It prints John", "No. Python does not treat Name and name as the same."),
          ("It prints Name", "No. Without quotes, Python looks for a variable called Name.")], 0),
        ("Which variable name is valid?",
         [("_score", "Yes! Names may start with a letter or an underscore."),
          ("2score", "No. A name can never start with a number."),
          ("my score", "No. Spaces are not allowed in variable names.")], 0),
        ("Which symbol starts a single-line comment?",
         [("#", "Right! Everything after # on that line is ignored by Python."),
          ("//", "No. // is used for comments in other languages, not Python."),
          ("<!--", "No. That is an HTML comment.")], 0),
        ("What does indentation do in Python?",
         [("Shows which lines belong together in a block", "Yes! For example, the code inside an if must be indented."),
          ("Makes the text look bold", "No. It has nothing to do with bold text."),
          ("Nothing, it is just decoration", "No. Wrong indentation can cause errors.")], 0),
    ],
    3: [
        ("What does 10 // 3 give?",
         [("3", "Correct! // is floor division. It drops the decimals."),
          ("3.33", "No. That would be 10 / 3. Floor division removes the decimals."),
          ("1", "No. That is the remainder, which is what % gives.")], 0),
        ("What does 10 % 3 give?",
         [("1", "Right! % gives the remainder. 3 goes into 10 three times, leaving 1."),
          ("3", "No. 3 is the result of 10 // 3."),
          ("0", "No. 0 would mean 3 divides 10 evenly.")], 0),
        ("What does 2 + 3 * 4 give?",
         [("14", "Correct! PEMDAS says multiply first: 3 * 4 = 12, then 2 + 12 = 14."),
          ("20", "No. That adds first, which breaks the order of operations."),
          ("24", "No. That is 2 * 3 * 4.")], 0),
        ("What does 10 / 5 give?",
         [("2.0", "Yes! The / operator always gives a decimal number."),
          ("2", "Close, but / always returns a decimal, so it is 2.0."),
          ("5", "No. 10 divided by 5 is 2.")], 0),
    ],
    4: [
        ("What type of data does input() always return?",
         [("Text (a string)", "Correct! Even if the user types a number, it arrives as text."),
          ("An integer", "No. You must convert it yourself using int()."),
          ("A decimal number", "No. You must convert it yourself using float().")], 0),
        ("Which line turns typed input into a whole number?",
         [("int(input(\"Age: \"))", "Yes! int() converts the text into an integer."),
          ("str(input(\"Age: \"))", "No. str() keeps it as text."),
          ("print(input(\"Age: \"))", "No. print() only displays things.")], 0),
        ("The user types 5. What does age = input() then print(age + age) show?",
         [("55", "Correct! age is TEXT, so + glues the two texts together."),
          ("10", "No. That only works if you convert it with int() first."),
          ("An error", "No. Adding text to text is allowed. It joins them.")], 0),
        ("name is \"Ana\". What does print(\"Name:\", name) show?",
         [("Name: Ana", "Right! The comma shows both and adds a space between them."),
          ("Name:Ana", "No. A comma in print() adds a space automatically."),
          ("name Ana", "No. The text in quotes is printed exactly as written.")], 0),
    ],
    5: [
        ("Which operator means \"not equal to\"?",
         [("!=", "Yes! != is true when the two values are different."),
          ("==", "No. == checks if two values are EQUAL."),
          ("=!", "No. That is not a Python operator.")], 0),
        ("score = 70. What does: if score >= 75: print(\"Passed\") else: print(\"Failed\") show?",
         [("Failed", "Correct! 70 >= 75 is False, so the else block runs."),
          ("Passed", "No. 70 is not greater than or equal to 75."),
          ("Nothing", "No. else runs whenever the if condition is False.")], 0),
        ("In an if-elif-else, two conditions are True. What runs?",
         [("Only the first True block", "Right! Python stops at the first True block and skips the rest."),
          ("Both True blocks", "No. Only one block ever runs."),
          ("Only the else block", "No. else runs only when every condition above it is False.")], 0),
        ("What does == do?",
         [("Compares two values (True or False)", "Yes! It asks 'are these equal?'"),
          ("Stores a value in a variable", "No. A single = stores a value."),
          ("Prints the two values", "No. print() is used to display things.")], 0),
    ],
    6: [
        ("What does True and False give?",
         [("False", "Correct! and needs EVERY condition to be True."),
          ("True", "No. One False makes the whole and False."),
          ("An error", "No. This is valid Python.")], 0),
        ("What does True or False give?",
         [("True", "Right! or only needs AT LEAST ONE True."),
          ("False", "No. or is False only when every side is False."),
          ("An error", "No. This is valid Python.")], 0),
        ("What does not True give?",
         [("False", "Yes! not flips the result."),
          ("True", "No. not reverses the value."),
          ("None", "No. It gives False.")], 0),
        ("age = 70. What does age >= 18 and age <= 60 give?",
         [("False", "Correct! 70 >= 18 is True, but 70 <= 60 is False, so and gives False."),
          ("True", "No. Both parts must be True for and, and the second one is False."),
          ("An error", "No. This is a valid expression.")], 0),
    ],
    7: [
        ("How many times does for i in range(3): run?",
         [("3 times", "Correct! range(3) gives 0, 1, 2. That is 3 repeats."),
          ("2 times", "No. It starts at 0, so there are three values."),
          ("4 times", "No. The stop value is not included.")], 0),
        ("What numbers does range(1, 4) give?",
         [("1, 2, 3", "Yes! It starts at 1 and stops BEFORE 4."),
          ("1, 2, 3, 4", "No. The stop value is excluded."),
          ("0, 1, 2, 3", "No. The start value here is 1, not 0.")], 0),
        ("Which is best when you don't know how many repeats you need?",
         [("A while loop", "Right! It repeats while a condition stays True."),
          ("for i in range(3)", "No. That always repeats exactly 3 times."),
          ("An if statement", "No. if runs the code once and never repeats.")], 0),
        ("What does break do inside a loop?",
         [("Stops the loop right away", "Yes! It is how you escape a while True loop."),
          ("Skips the whole program", "No. It only leaves the loop."),
          ("Restarts the loop", "No. It ends the loop instead.")], 0),
    ],
}

# ---------------------------------------------------------------
# MINI GAMES: one per lesson
# GAMES[n] = (game title, instructions, prompt for the player, items)
# item = (what to show, correct answer, hint, explanation)
# ---------------------------------------------------------------
GAMES = {
    1: ("True or False Rush",
        "Read each statement and type true or false.",
        "true or false: ",
        [("Python was created in 1991.", "true", "Think of Guido van Rossum.", "Python was created in 1991 by Guido van Rossum."),
         ("Python is a low-level language.", "false", "Is it close to human language?", "Python is HIGH-level, close to human language."),
         ("Python code is usually hard to read.", "false", "Remember why beginners like it.", "Python is designed to be readable, almost like English."),
         ("Python can be used for AI, web, and games.", "true", "It is very versatile.", "Python is versatile: AI, web, automation, games, and more.")]),

    2: ("Valid or Invalid?",
        "Is each variable name allowed in Python? Type valid or invalid.",
        "valid or invalid: ",
        [("my_age", "valid", "Letters and underscores are fine.", "Letters and underscores are allowed."),
         ("2nd_place", "invalid", "Check the first character.", "A name cannot start with a number."),
         ("first name", "invalid", "Look for a space.", "Spaces are not allowed. Use first_name instead."),
         ("_total", "valid", "Names may start with an underscore.", "Starting with an underscore is allowed."),
         ("email@home", "invalid", "Look for a special symbol.", "Special characters like @ and # are not allowed.")]),

    3: ("Math Detective",
        "Type exactly what each line prints.",
        "It prints: ",
        [("print(10 // 4)", "2", "// drops the decimals.", "10 divided by 4 is 2.5, and // drops the .5, leaving 2."),
         ("print(17 % 5)", "2", "% is the remainder.", "5 goes into 17 three times (15), leaving 2."),
         ("print(3 ** 2)", "9", "** means power.", "3 ** 2 means 3 x 3 = 9."),
         ("print((2 + 3) * 4)", "20", "Brackets come first.", "Brackets first: 2 + 3 = 5, then 5 * 4 = 20."),
         ("print(7 / 2)", "3.5", "/ gives a decimal.", "7 divided by 2 is 3.5.")]),

    4: ("Input Detective",
        "Read the code (and what the user types), then type exactly what it prints.",
        "It prints: ",
        [("name = input(\"Name: \")    # user types: Ana\nprint(\"Hello,\", name)", "Hello, Ana", "The comma adds a space.", "name holds Ana, and the comma adds a space after Hello,"),
         ("age = input(\"Age: \")      # user types: 5\nprint(age + age)", "55", "input() gives TEXT.", "5 is text here, so + glues them together: 55."),
         ("age = int(input(\"Age: \")) # user types: 5\nprint(age + 1)", "6", "int() makes it a number.", "int() turned the text into a number, so 5 + 1 = 6."),
         ("print(\"Age:\", 20)", "Age: 20", "Comma adds a space.", "The comma prints both values with a space between.")]),

    5: ("Decision Detective",
        "Type exactly what each program prints.",
        "It prints: ",
        [("score = 82\nif score >= 75:\n    print(\"Passed\")\nelse:\n    print(\"Failed\")", "Passed", "Is 82 >= 75?", "82 >= 75 is True, so the if block runs."),
         ("age = 15\nif age >= 18:\n    print(\"Adult\")\nelse:\n    print(\"Minor\")", "Minor", "Is 15 >= 18?", "15 >= 18 is False, so the else block runs."),
         ("x = 5\nif x == 5:\n    print(\"Five\")\nelif x > 3:\n    print(\"Big\")\nelse:\n    print(\"Small\")", "Five", "Only the FIRST True block runs.", "x == 5 is True, so Python runs it and skips the elif."),
         ("print(5 != 5)", "False", "5 is equal to 5.", "5 != 5 asks 'are they different?' and the answer is False.")]),

    6: ("Logic Detective",
        "Type True or False for what each line prints.",
        "It prints: ",
        [("print(True and True)", "True", "and needs all True.", "Both sides are True, so the result is True."),
         ("print(False or False)", "False", "or needs at least one True.", "Neither side is True, so the result is False."),
         ("print(not False)", "True", "not flips it.", "not flips False into True."),
         ("day = \"Monday\"\nprint(day == \"Saturday\" or day == \"Sunday\")", "False", "Is Monday a weekend day?", "Both tests are False, so or gives False."),
         ("print(5 > 3 and 2 > 10)", "False", "Check each side.", "5 > 3 is True but 2 > 10 is False, so and gives False.")]),

    7: ("Loop Detective",
        "Type what each program prints, with spaces between the numbers (example: 1 2 3).",
        "It prints: ",
        [("for i in range(3):\n    print(i)", "0 1 2", "range(3) starts at 0.", "range(3) gives 0, 1, 2."),
         ("for i in range(1, 4):\n    print(i)", "1 2 3", "Stop value is excluded.", "It starts at 1 and stops before 4."),
         ("for i in range(5, 0, -1):\n    print(i)", "5 4 3 2 1", "The step is -1, so it counts down.", "It counts down from 5 and stops before 0."),
         ("i = 0\nwhile i < 3:\n    print(i)\n    i = i + 1", "0 1 2", "Stops when i reaches 3.", "The loop runs while i < 3, adding 1 each time."),
         ("for i in range(5):\n    if i == 2:\n        break\n    print(i)", "0 1", "break stops the loop.", "When i becomes 2, break ends the loop before printing.")]),
}


# ---------------------------------------------------------------
# FUNCTIONS
# ---------------------------------------------------------------
def pause():
    input("\nPress Enter to continue...")


def read_lesson(number):
    title, content = LESSONS[number]
    print(f"\n----- LESSON {number}: {title.upper()} -----")
    print(content)
    pause()


def run_quiz(questions, title):
    print(f"\n----- {title.upper()} -----")
    print("Type the number of your answer.\n")
    questions = random.sample(questions, len(questions))
    score = 0

    for number, (question, options, correct) in enumerate(questions, 1):
        correct_text = options[correct][0]
        shuffled = random.sample(options, len(options))

        print(f"Q{number}. {question}")
        for i, (text, _) in enumerate(shuffled, 1):
            print(f"   {i}. {text}")

        valid = [str(i) for i in range(1, len(shuffled) + 1)]
        answer = input("Your answer: ").strip()
        while answer not in valid:
            answer = input(f"Please type a number from 1 to {len(shuffled)}: ").strip()

        picked_text, picked_explanation = shuffled[int(answer) - 1]
        if picked_text == correct_text:
            print(f"  Correct! +1 point\n  {picked_explanation}\n")
            score += 1
        else:
            print(f"  Not quite.\n  Why not? {picked_explanation}")
            correct_explanation = dict(options)[correct_text]
            print(f"  The right answer is: {correct_text}\n  {correct_explanation}\n")

    total = len(questions)
    print(f"Score: {score}/{total}")
    if score == total:
        print("Perfect! You are a Python star!")
    elif score >= total * 0.7:
        print("Great job! Almost perfect.")
    else:
        print("Keep going! Read the lesson again and retry.")
    pause()


def run_game(number):
    name, instructions, prompt, items = GAMES[number]
    print(f"\n----- MINI GAME: {name.upper()} -----")
    print(instructions)
    print("You have 3 lives. Type 'hint' for a free clue.\n")

    items = random.sample(items, len(items))
    lives = 3
    points = 0

    for case, (shown, expected, hint, explanation) in enumerate(items, 1):
        print(f"Case {case}    Lives: {'<3 ' * lives}")
        print("-" * 32)
        print(shown)
        print("-" * 32)

        while True:
            guess = input(prompt).strip()
            if guess.lower() == "hint":
                print(f"Hint: {hint}")
                continue
            break

        if " ".join(guess.split()).lower() == expected.lower():
            print(f"Correct! +10 points\n  {explanation}\n")
            points += 10
        else:
            lives -= 1
            print(f"Wrong! The answer is: {expected}\n  {explanation}\n")
            if lives == 0:
                print("Game over, you ran out of lives!")
                break

    print(f"Total points: {points}")
    if lives > 0:
        print("You finished the game. Nice work!")
    pause()


def lesson_menu(number):
    title = LESSONS[number][0]
    while True:
        print("\n" + "=" * 36)
        print(f"  LESSON {number}: {title}")
        print("=" * 36)
        print("  1. Read the lesson")
        print("  2. Take the quiz")
        print(f"  3. Play the mini game ({GAMES[number][0]})")
        print("  0. Back to lesson list")

        choice = input("\nChoose (0-3): ").strip()
        if choice == "1":
            read_lesson(number)
        elif choice == "2":
            run_quiz(QUIZZES[number], f"Lesson {number} Quiz")
        elif choice == "3":
            run_game(number)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please type 0, 1, 2, or 3.")


def final_challenge():
    everything = [q for questions in QUIZZES.values() for q in questions]
    run_quiz(random.sample(everything, 10), "Final Challenge (all lessons)")


def main():
    print("Welcome! Let's learn Python together.")
    while True:
        print("\n" + "=" * 36)
        print("      PYTHON BASICS FOR BEGINNERS")
        print("=" * 36)
        for number, (title, _) in LESSONS.items():
            print(f"  {number}. Lesson {number}: {title}")
        print("  8. Final Challenge (mixed quiz)")
        print("  0. Exit")

        choice = input("\nChoose a lesson (1-7), 8, or 0: ").strip()
        if choice == "0":
            print("Goodbye! Keep practicing!")
            break
        elif choice.isdigit() and int(choice) in LESSONS:
            lesson_menu(int(choice))
        elif choice == "8":
            final_challenge()
        else:
            print("Invalid choice. Please type a number from 0 to 8.")


if __name__ == "__main__":
    main()