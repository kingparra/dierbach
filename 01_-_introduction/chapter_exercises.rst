*************************
 Chapter 1: Introduction
*************************



Chapter Exercises
=================


Section 1.1
-----------
1. Search online for two computing-related fields named “computational X” other
   than the ones listed in Figure 1-1.

    * Computational Toxicology and Computational Meteorology are two
      interdisciplinary job titles that caught my interest.


2. Search online for two areas of computer science other than those given in
   the chapter.

    * Computational complexity theory, which is the study of how computationally
      expensive it is to solve a problem, is one. Another area is cryptography,
      the study of how to share secrets in a confidential manner.


3. For the Man, Cabbage, Goat, Wolf problem:

    (a.) List all the invalid states for this problem, that is, in which the goat
         is left alone with the cabbage, or the wolf is left alone with the goat.

         The goat and cabbage are left unsupervised on the east shore.

         +---+---+---+---+
         | M | C | G | W |
         +===+===+===+===+
         | W | E | E | W |
         +---+---+---+---+

         The goat and the wolf are left unsupervised on the east shore.

         +---+---+---+---+
         | M | C | G | W |
         +===+===+===+===+
         | W | W | E | E |
         +---+---+---+---+

         The goat and cabbage are left unsupervised on the west shore.

         +---+---+---+---+
         | M | C | G | W |
         +===+===+===+===+
         | E | W | W | E |
         +---+---+---+---+

         The goat and the wolf are left unsupervised on the west shore.

         +---+---+---+---+
         | M | C | G | W |
         +===+===+===+===+
         | E | E | W | W |
         +---+---+---+---+

         The goat, cabbage, and wolf are left unsupervised on the east shore.

         +---+---+---+---+
         | M | C | G | W |
         +===+===+===+===+
         | W | E | E | E |
         +---+---+---+---+

         The goat, cabbage, and wolf are left unsupervised on the west shore.

         +---+---+---+---+
         | M | C | G | W |
         +===+===+===+===+
         | E | W | W | W |
         +---+---+---+---+

         To summarize, any state in which either the wolf and goat are left together
         unsupervised, or the cabbage and goat are left unsupervised is invalid.

    (b.) Give the shortest sequence of steps that solves the MCGW problem.

         (Note: This was copy pasted from `here <https://illuminations.nctm.org/BrainTeasers.
         aspx?id=4992>`_ since I did the state representation first and didn't want to
         re-type everything.)

         * The wolf does not eat cabbage, so the crossing can start with the goat.
         * The man leaves the goat and returns, puts the cabbage in the boat and takes it
           across. On the other bank, he leaves the cabbage but takes the goat.
         * He leaves the goat on the first bank and takes the wolf across. He leaves the
           cabbage with the wolf and rows back alone.
         * He takes the goat across.

    (c.) Give the sequence of state representations that correspond to your
         solution starting with (E,E,E,E) and ending with (W,W,W,W).

         +-----+---+---+---+---+
         |     | M | C | G | W |
         +=====+===+===+===+===+
         | *0* | E | E | E | E |
         +-----+---+---+---+---+
         | *1* | W | E | W | E |
         +-----+---+---+---+---+
         | *2* | E | E | W | E |
         +-----+---+---+---+---+
         | *3* | W | W | W | E |
         +-----+---+---+---+---+
         | *4* | E | W | E | E |
         +-----+---+---+---+---+
         | *5* | W | W | E | W |
         +-----+---+---+---+---+
         | *6* | E | W | E | W |
         +-----+---+---+---+---+
         | *7* | W | W | W | W |
         +-----+---+---+---+---+

    (d.) There is an alternate means of representing states. Rather than a sequence
         representation, a set representation can be used. In this representation,
         if an item is on the east side of the river, its symbol is in the set, and
         if on the west side, the symbol is not in the set as shown below,

         | ``{M,C,G,W}`` — all items on east side of river (start state)
         | ``{C,W}`` — cabbage and wolf on east side of river, man and goat on west side
         | ``{}`` — all items on the west side of the river (goal state)

         Give the sequence of states for your solution to the problem using this new
         state representation.

         * Here, enjoy::

             0 {M,C,G,W}
             1 {C,W}
             2 {M,C,W}
             3 {W}
             4 {M,G,W}
             5 {G}
             6 {M,G}
             7 {}

    (e.) How many shortest solutions are there for this problem?

         Good question. How can I figure that out? What are the relevant
         details? First off, what's a "solution", anyways? For our purposes,
         it's a series of representations of who's on each shore, or state,
         that must be recreated *in order*. So the relevant details are the
         state during each step, and the order in which the steps must be
         taken.

         Let's create a graph, and arrange each state in the order they must
         take to reach the goal state of W,W,W,W. Arrows that denote order can
         connect nodes, which are steps.

         So::

             +                                                                             +---+---+                         +---+---+
                                                                                           | E | W |                         | E | W |
                                                                                       +===+===+===+                     +===+===+===+
                                                                                       | M |   | x |                     | M |   | x |
                                                                                       +---+---+---+                     +---+---+---+
                                                                                 --->  | C |   | x |  ---------------->  | C |   | x |  ----\
                                                                                /      +---+---+---+                     +---+---+---+       \
                 +---+---+                +---+---+                +---+---+   /       | G |   | x |                     | G | x |   |        \      +---+---+                  +---+---+                  +---+---+
                 | E | W |                | E | W |                | E | W |  /        +---+---+---+                     +---+---+---+         >     | E | W |                  | E | W |                  | E | W |
             +===+===+===+            +===+===+===+            +===+===+===+ /         | W | x |   |                     | W |   | x |           +===+===+===+              +===+===+===+              +===+===+===+
             | M | x |   |            | M |   | x |            | M | x |   |           +---+---+---+                     +---+---+---+           | M |   | x |              | M | x |   |              | M |   | x |
             +---+---+---+            +---+---+---+            +---+---+---+                                                                     +---+---+---+              +---+---+---+              +---+---+---+
             | C | x |   | =========> | C | x |   | =========> | C | x |   |                                                                     | C |   | x |  =========>  | C |   | x |  =========>  | C |   | x |
             +---+---+---+            +---+---+---+            +---+---+---+                                                                     +---+---+---+              +---+---+---+              +---+---+---+
             | G | x |   |            | G |   | x |            | G |   | x |                                                                     | G | x |   |              | G | x |   |              | G |   | x |
             +---+---+---+            +---+---+---+            +---+---+---+                                                                     +---+---+---+              +---+---+---+              +---+---+---+
             | W | x |   |            | W | x |   |            | W | x |   |               +---+---+                         +---+---+           | W |   | x |              | W |   | x |              | W |   | x |
             +---+---+---+            +---+---+---+            +---+---+---+               | E | W |                         | E | W |           +---+---+---+              +---+---+---+              +---+---+---+
                                                                             \         +===+===+===+                     +===+===+===+          >
                                                                              \        | M |   | x |                     | M | x |   |         /
                                                                               \       +---+---+---+                     +---+---+---+        /
                                                                                \      | C | x |   |                     | C | x |   |       /
                                                                                 --->  +---+---+---+  ---------------->  +---+---+---+  ----/
                                                                                       | G |   | x |                     | G | x |   |
                                                                                       +---+---+---+                     +---+---+---+
                                                                                       | W |   | x |                     | W |   | x |
                                                                                       +---+---+---+                     +---+---+---+


         There are two solutions of the same length. (Note: Dijkstra, a
         preeminenet computer scientest, talks about this problem `here
         <http://www.cs.utexas.edu/users/EWD/videos/EWD4.mpg>`_. `local
         copy <./EWD4.mpg>`_)


4. For a simple game that starts with five stones, in which each player can
   pick up either one or two stones, the person picking up the last stone being
   the loser,

   (a.) Give a state representation appropriate for this problem.

        * Stones are numbered 1 through 5.
        * Players are represented as P1, P2, etc...
        * During a turn, a stone in the sequence is replaced by the player name
          who picked it up.
        * Assuming we have two players...
        * Start state: ``{1, 2, 3, 4, 5}``.
        * An example end state: ``{P1, P1, P2, P2, P1}``.
        * Player one lost this round.

    (b.) Give the start state and goal state for this problem.

         * Start state:                                    ``{1, 2, 3, 4, 5}``
         * Goal state (assuming you're player one):        ``{P1, P2, P2, P1, P2}``

    (c.) Give a sequence of states in which the first player wins the game.

         * Sure::

             {1, 2, 3, 4, 5}
             {P1, P2, 3, 4, 5}
             {P1, P2, P1, P1, 5}
             {P1, P2, P1, P1, P2}


Section 1.2
-----------
5. Using the algorithm in Figure 1-8, show all steps for determining the day of
   the week for January 24, 2018.  (Note that 2018 is not a leap year.)

    * This is tedious::

        1. century_digits = 20
        2. year_digits = 18
        3. value = year_digits + floor(year_digits / 4)
           value = 18 + floor(18 / 4)
           value = 18 + floor(4.5)
           value = 18 + 4
           value = 22
        4. century_digits = century_digits + 2
           century_digits = 20 + 2
           century_digits = 22
        5. Since month is January and it's not a leap year
           value = value + 1
           value = 22 + 1
           value = 23
        6. value = (value + day) mod 7
           value = (23 + 24) mod 7
           value = 47 mod 7
           value = 5
        7. value is 5, so the day is Thursday.


6. Using the algorithm in Figure 1-8, determine the day of the week that you
   were born on.

    * My date of birth is April 30th, 1988. The day is Saturday.


7. Suppose that an algorithm was needed for determining the day of the week for
   dates that only occur within the years 2000–2099. Simplify the day of the
   week algorithm in Figure 1-8 as much as possible by making the appropriate
   changes.

    * TODO


8. As precisely as possible, give a series of steps (an algorithm) for doing
   long addition.

    * TODO

Section 1.3
-----------
9. What is the number of bits in 8 bytes, assuming the usual number of bits in
   a byte?

    * 8 bytes = 64 bits


10. Convert the following values in binary representation to base 10. Show all
    steps .

    (a.) 1010::
        2**1 + 2**3 = 10
        2 + 8 = 10

    (b.) 1011::
        2**0 + 2**1 + 2**3 = 11
        1 + 2 + 8 = 11

    (c.) 10000::
        2 ** 4 = 16
        16 = 16

    (d.) 1111::
        2**0 + 2**1 + 2**2 + 2**3 = 15
        1 + 2 + 4 + 8 = 15


11. Convert the following values into binary (base 2) representation. *Show all
    steps.*

    * No, that's a waste of time. Computer Science is about reducing tedium.
      It's sufficient to know that you multiply the digits by their respective
      place values. See "decimal_to_binary.py" for more. Here's the output::

        (a.)   5    = 101
        (b.)   7    = 111
        (c.)   16   = 10000
        (d.)   15   = 1111
        (e.)   32   = 100000
        (f.)   33   = 100001
        (g.)   64   = 1000000
        (h.)   63   = 111111
        (i.)   128  = 10000000
        (j.)   127  = 1111111


12. What is in common within each of the following groups of binary numbers?

    (a.) Values that end with a “0” digit (e.g., 1100).

        * They're even! The leftmost place value, 2**0, which evaluates to 1, is turned off.

    (b.) Values that end with a “1” digit (e.g., 1101).

        * They're odd!

    (c.) Values with a leftmost digit of “1,” followed by all “0s” (e.g., 1000).

        * I don't know. What do these binary numbers have in common?

    (d.) Values consisting only of all “1” digits (e.g., 1111).

        * The are the largest possible value given that many digits. They are also
          odd numbers.


13. Assuming that Moore’s Law continues to hold true, where n is the number of
    transistors that can currently be placed on an integrated circuit (chip),
    and k*n is the number that can be placed on a chip in eight years, what is
    the value of k?

    * From https://en.wikipedia.org/wiki/Transistor_count: As of 2016, the largest
      transistor count in a commercially available single-chip processor is over
      7.2 billion—the Intel Broadwell-EP Xeon. (OK, it's 2017, but I couldn't find
      anything more recent.)
    * ``n = 7.2 * 10 ** 9``
    * ``k = 8``
    * ``n * k``
    * The projected number of transistors that will be able to fit on a CPU in
      eight years is 57,600,000,000.


Section 1.4
-----------
14. Give two specific examples of an application program besides those
    mentioned in the chapter.

    * Vim and photoshop spring to mind.


15. For each of the following statements in English, indicate whether the
    statement contains a syntax error, a logic (semantic) error, or is a valid
    statement.

        +------------------------------+---------------------+
        | Statement                    | Error               |
    +===+==============================+=====================+
    | a | Which way did he go?         | VALID               |
    +---+------------------------------+---------------------+
    | b | I think he went over their.  | SYNTAX              |
    +---+------------------------------+---------------------+
    | c | I didn’t see him go nowhere. | SYNTAX and SEMANTIC |
    +---+------------------------------+---------------------+


16. For each of the following arithmetic expressions for adding up the integers
    1 to 5, indicate whether the expression contains a syntax error, a semantic
    error, or is a valid expression.

        +---------------------+--------+
        | Statement           | Error  |
    +===+=====================+========|
    | a | 1 + 2 ++ 3 + 4 + 5  | SYNTAX |
    +---+---------------------+--------+
    | b | 1 + 2 + 4 + 5       | VALID  |
    +---+---------------------+--------+
    | c | 1 + 2 + 3 + 4 + 5   | VALID  |
    +---+---------------------+--------+
    | d | 5 + 4 + 3 + 2 + 1   | VALID  |
    +---+---------------------+--------+


17. Give one benefit of the use of a compiler, and one benefit of the use of an
    interpreter.

    * A compiler creates object code which can be executed quickly by the cpu.
      Much faster than an interpreter. An interpreter allows faster
      troubleshooting, since you can observe the effects of changes to source
      code without recompiling. You can also run in interactive mode, which
      allows for experimental interaction.
    * Compilers also introduce the opportunity for checks to be performed
      staticlly, before runtime.


Section 1.5
-----------
18. Use the Python Interactive Shell to calculate the number of routes that can
    be taken for the Traveling Salesman problem for

    (a.) 6  cities = 720 possible routes
    (b.) 12 cities = 479001600 possible routes
    (c.) 18 cities = 6402373705728000 possible routes
    (d.) 36 cities = 371993326789901217467999448150835200000000 possible routes


19. Enter the following statement into the interactive shell::

        print('What is your favorite color?')

    Record the output. Now enter the following statement exactly as given::

        printt('What is your favorite color?')

    Record the output. Is this a syntax error or a logic error?

    * It's a syntax error, specifically a NameError. Here's the output::

        Traceback (most recent call last):
        File "<input>", line 1, in <module>
        printt('What is your favorite color?')
        NameError: name 'printt' is not defined


20. For the Traveling Salesman problem,

    (a.) Update the list representation of the distances between cities in the table
        in Figure 1-23 to add the city of Seattle. The distances between Seattle and
        each of the other cities is given below.

        * Atlanta to Seattle:         2641 miles
        * Boston to Seattle:          3032 miles
        * Chicago to Seattle:         2043 miles
        * LA to Seattle:              1208 miles
        * NYC to Seattle:             2832 miles
        * San Francisco to Seattle:    808 miles

        * TODO

    (b.) Determine a reasonably short route of travel for visiting each city once
        and only once, starting in Atlanta and ending in San Francisco.

        * TODO


Section 1.6
-----------
21. Which of the following capabilities does an integrated development environment (IDE) provide?

    (a.) Creating and modifying programs
    (b.) Executing programs
    (c.) Debugging programs
    (*d.*) All of the above


22. The Python shell is a window in which Python instructions are immediately executed. (*TRUE*/FALSE)


23. Suppose that the math module of the Python Standard Library were imported.
    What would be the proper syntax for calling a function in the math module
    named sqrt to calculate the square root of four?

    * The proper syntax for calling the sqrt function of the math module would
      be ``math.sqrt()``.


24. What is the value of variable n after the following instructions are executed?

    ::
        j = 5
        k = 10
        n = j * k

    * The value of n would be 50.


25. Which of the following is a proper arithmetic expression in Python?

    (a.)   ``10(15 + 6)``
    (b.)   ``(10 * 2)(4 + 8)``
    (*c.*) ``5 * (6 - 2)``


26. Exactly what is output by the following if the user enters 24 in response
    to the input prompt::

        age = input('How old are you?: ')
        print('You are', age, 'years old')

    * It would be: "You are 24 years old".

