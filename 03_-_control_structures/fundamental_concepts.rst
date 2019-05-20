*******************************
 Chapter 3: Control Structures
*******************************



Fundamental Concepts
====================


3.1 What Is a Control Structure?
--------------------------------
* **Control flow** is the order that instructions in are executed in a program.
* A **control statement** is a statement that determines the control flow of a set
  of instructions.
* A **control structure** is a set of instructions and the control statements
  controlling their execution.
* Three fundamental forms of control in programming are sequential, selection,
  and iterative control.

  * **Sequential control** is an implicit form of control in which instructions
    are executed in the order they're written.
  * **Selection control** is provided by a control statement that selectively
    executes instructions based on a condition.
  * **Iterative control** is provided by a control statement that repeatedly
    executes instructions based on a condition.


3.2 Boolean Expressions (Conditions)
------------------------------------
* The Boolean data type contains two Boolean values, denoted as ``True`` and
  ``False`` in Python.
* A Boolean expression is an expression that evaluates to a Boolean value.


3.2.1 Relational Operators
--------------------------
* The relational operators ``==``, ``!=``, ``<``, ``>``, ``<=``, ``>=`` can be
  applied to any set of values that has an ordering.
* Strings are compared based on the lexicographical ordering of their member
  characters, which is derived from each characters respective Unicode code
  point.


3.2.2 Membership Operators
--------------------------
* Python provides membership operators ``in`` and ``not in`` for determining if
  a specific value is in (or not in) a given list of values (or any collection,
  really).


3.2.3 Boolean Operators
-----------------------
* Boolean operators in Python are denoted by ``and``, ``or``, and ``not``.


3.2.4 Operator Precedence and Boolean Expressions
-------------------------------------------------
* Arithmetic operators are performed before relational operators, which are
  performed before boolean operators.


3.2.5 Short-Circuit (Lazy) Evaluation
-------------------------------------
* In short-circuit (lazy) evaluation, the second operand of Boolean operators
  ``and`` and ``or`` is not evaluated if the value of the Boolean expression
  can be determined from the first operand alone.


3.2.6 Logically Equivalent Boolean Expressions
----------------------------------------------
* There are logically equivalent Boolean expressions of different form.
* ``De Morgan's Laws <https://brilliant.org/wiki/de-morgans-laws/>``_:
  * Not (A and B) is the same as Not A or Not B.
  * Not (A or B) is the same as Not A and Not B.

Self-Test Questions
^^^^^^^^^^^^^^^^^^^
1. Three forms of control in programming are sequential, selection and
   ``__iterative__`` control.

2. Which of the following expressions evaluate to True?

    **a.**  ``10 >= 8 ``
    **b.**  ``8 <= 10 ``
    c.      ``10 == 8 ``
    **d.**  ``10 != 8``
    e.      ``'8' < '10'``

3. Which of the following Boolean expressions evaluate to True?

    **a.**  ``'Dave' < 'Ed' ``
    b.      ``'dave' < 'Ed' ``
    c.      ``'Dave' < 'Dale'``

4. What is the value of variable num after the following is executed?

   ::

        num = 10
        num = num + 5
        num == 20
        num = num + 1

    * ``num`` would point to 16.

5. What does the following expression evaluate to for name equal to 'Ann'?

   ::

       name in ('Jacob', 'MaryAnn', 'Thomas')

    * ``False``.

6. Evaluate the following Boolean expressions using the operator precedence
   rules of Python.

    a. ``10 >= 8 and 5 != 3 ``              ==> True
    b. ``10 >= 8 and 5 == 3 or 14 < 5``     ==> False

7. Which one of the following Boolean expressions is not logically equivalent
   to the other two?

    a.      ``not(num < 0 or num > 10)``
    **b.**  ``num > 0 and num < 10``
    c.      ``num >= 0 and num <= 10``


3.3 Selection Control
---------------------
* A selection control statement is a control statement providing selective
  execution of instructions.


3.3.1 ``if`` Statement
----------------------
* An ``if`` statement is a selection control statement based on the value of a
  given Boolean expression.
* Statements that contain other statements are referred to as a compound
  statement.


3.3.2 Indentation in Python
---------------------------
* A header in  Python starts with a keyword and ends with a colon. The group of
  statements following a header is called a suite. A header and its associated
  suite together are referred to as a clause.


3.3.3 Multi-Way Selection
-------------------------
* ``if`` statements may contain any number of ``elif`` headers, providing for
  multi-way selection.


3.3.4 Let's Apply It -- Number of Days in Month Program
-------------------------------------------------------
* Logic to determine if a year is a leap year: ``year % 4 == 0 and year % 100 != 0 or year % 400 == 0``.

Self-Test Questions
^^^^^^^^^^^^^^^^^^^
1. All ``if`` statements must contain either an ``else`` or ``elif`` header.

   TRUE/**FALSE**

2. A compound statement is,

   a.      A statement that spans more than one line.
   **b.**  A statement that contains other statements.
   c.      A statement the contains at least one arithmetic expressions.

3. Which of the following statements are true regarding headers in Python?
   **a.**  Headers begin with a keyword and end with a colon.
   b.      Headers always occur in pairs.
   **c.**  All headers of the same compound statement must be indented the same
           amount.

4. Which of the following statements is true?
   a.      Statements within a suite can be indented a different amount.
   b.      Statements within a suite can be indented a different amount as long as
           all headers in the statement that it occurs in are indented the same
           amount.
   **c.**  All headers must be indented the same amount as all others headers
           in the same statement, and all statements in a given suite must be
           indented the same amount.

5. The ``elif`` header allows for,
   a.      Multi-way selection that cannot be accomplished otherwise.
   **b.**  Multi-way selection as a single if statement.
   c.      The use of a "catch-all" case in multi-way selection.


3.4 Iterative Control
---------------------
* An iterative control statement is a control statement that allows for the
  repeated execution of a set of statements.


3.4.1 While Statement
---------------------
* A ``while`` statement is an iterative control statement the repeatedly executes
  a set of statements based on a Boolean expression. As long as the boolean
  expression evaluates to True, the statements are executed.


3.4.2 Input Error Checking
--------------------------
* The ``while`` statement is well suited for input error checking.


3.4.3 Infinite Loops
--------------------
* An infinite loop is an iterative control structure that never terminates (or
  eventually terminates with a system error).


3.4.4 Definite vs Indefinite Loops
----------------------------------
* A definite loop is a loop where the number of iterations is known beforehand.
  Indefinite loops may iterate any number of times, or not at all.


3.4.5 Boolean Flags and Indefinite Loops
----------------------------------------
* A single Boolean variable used as the condition of a given control statement
  is called a Boolean flag.


3.4.6 Let's Apply It - Coin Change Exercise Program
---------------------------------------------------
* Got it.

Self-Test Questions
^^^^^^^^^^^^^^^^^^^
1. A while loop continues to iterate until its condition becomes false.
   **TRUE**/FALSE
2. A while loop executes zero or more times.
   **TRUE**/FALSE
3. All iteration can be achieved by a while loop.
   **TRUE**/FALSE
4. An infinite loop is an iterative control structures that,
    a. Loops forever and must be forced to terminate
    b. Loops until the program terminates with a system error
    **c**. Both of the above
5. The terms definite loop and indefinite loop are used to indicate whether,
    a. A given loop executes at least once
    **b**. The number of times that a loop is executed can be determined before the loop is executed.
    c. Both of the above
6. A Boolean flag is,
    a. A variable
    b. Has the value ``True`` or ``False``
    c. Is used as a condition for control statements
    **d**. All of the above


