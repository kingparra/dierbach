*********************************
 Chapter 2: Data and Expressions
*********************************



Fundamental Concepts
====================
* In the docs: https://docs.python.org/3/reference/expressions.html ..this
  covers most of the chapters content in regards to pythons implementation in
  painstaking detail. The organization of topics are strikingly similar.


2.1 Literals
------------


2.1.1 What Is a Literal?
------------------------
* A literal is a value that is represented literally in source code. In
  contrast to a variable name, function name, macro, or other identifier, it
  stands only for itself.


2.1.2 Numeric Literals
----------------------
* Valid characters include ``+``, ``-``, ``0`` through ``9``, ``.`` (for
  decimal numbers), and ``e`` (for scientific notation.)
* Commas are never used in numeric literals. In python 3.6 and later, however,
  you can use underscores as a thousands separator.
* Tangentially, a prefix of ``0b`` can be used for binary, ``0c`` for octal,
  and ``0x`` for hexadecimal, representations of integer numeric literals.

Limits of Range in Floating-Point Representation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Floating point values have both a limited range and precision, between
  10**-308 to 10**308, with 16 to 17 digits of precision. This is codified by
  the double-precision standard format, IEEE 754.
* Arithmetic overflow occurs when a calculated result is too large in magnitude
  to be represented. On the repl, it looks like ``inf``.
* Arithmetic underflow occurs when a calculated result is too small in
  magnitude to be represented. On the repl, it looks like ``0.0``.

Limits of Precision in Floating-Point Representation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Since any floating-point representation has only a finite number of digits,
  what is stored for many floating-point values is only an approximation of the
  true value.
* Loss of accuracy is common when using floats to represent very large or very
  small numbers, and can be hard to debug.
* Therefore, it's not a good idea to store irrational numbers or fractions as
  floating point numbers.

Built-in ``format`` Function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* The built-in ``format()`` function can be used to produce a numeric string of
  a given floating-point value rounded to a specific number of decimal places.


2.1.3 String Literals
---------------------
* A string literal, or string, is a sequence of characters surrounded by a pair of
  matching single or double (and sometimes triple) quotes in Python.

The Representation of Character Values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Unicode is capable of representing over 4 billion different characters,
  enough to represent the alphabets of all languages past and present(?).
* Python's default character encoding uses UTF-8, an eight bit encoding that's
  part of the Unicode standard.
* The ``ord()`` function can be used to display the unicode encoding of a
  character. ``chr()`` can convert an ASCII encoding number to a character.


2.1.4 Control Characters
------------------------
* Control characters are nonprinting characters used to control the display of
  output (amongst other things). An escape sequence is a string of one or more
  characters used to denote control characters.
* Strings interpret escape sequences by default.
* You can use a raw string eg, ``r'\r is not a newline but backslash r'`` to
  store character sequences literally, preventing interpretation of escape
  sequences. This is useful for storing regular expressions.


2.1.5 String Formatting
-----------------------
* The built-in ``format()`` function can be used to control how strings are
  displayed.


2.1.6 Implicit and Explicit Line Joining
----------------------------------------
* Sometimes a line may be too long to fit in the recommended maximum line
  length of 79 characters. Here are some ways to deal with that.

Implicit Line Joining
^^^^^^^^^^^^^^^^^^^^^
* Matching parentheses, square brackets, and curly braces can be used to span a
  logical program line on more than one physical line.
* Adjacent string literals in the same print statement are automatically
  concatenated. e.g.::

    >>> print('This is all'
    ... ' one line.')
    OUT: This is all one line.

Explicit Line Joining
^^^^^^^^^^^^^^^^^^^^^
* Program lines may be explicitly joined by use of the backslash (\).


2.1.7 Let's Apply it - Hello World Unicode Encoding
---------------------------------------------------
* There is a small program in this subsection that displays the unicode code
  points for the string 'Hello world!'.

Self-Test Questions
^^^^^^^^^^^^^^^^^^^
1. Indicate which of the following are valid numeric literals in Python.

    **a.**   ``1024``
    b.       ``1,024``
    **c.**   ``1024.0``
    **d.**   ``0.25``
    **e.**   ``.45``
    f.       ``0.25+10``

2. Indicate which of the following exceed the range and/or precision of
   floating-point values that can be represented in Python.

    a.       ``1.89345348392e+301``
    b.       ``1.62123432632322e+300``
    **c.**   ``2.0424e+320``
    d.       ``1.323232435342327896452e-140``

3. Which of the following would result in either overflow or underflow for the
   floating-point representation scheme mentioned in the chapter.

    a.       ``6.25e+240 * 1.24e+10``
    **b.**   ``2.24e+240 * 1.45e+300``
    c.       ``6.25e+240 / 1.24e-10``
    **d.**   ``2.24e2240 / 1.45e-300``

4. Exactly what is output by print(format(24.893952, '.3f'))

    **a.**   ``24.894``
    b.       ``24.893``
    c.       ``2.48e1``

5. Which of the following are valid string literals in Python.

    **a.**   ``"Hello"``
    **b.**   ``'hello'``
    c.       ``"Hello'``
    **d.**   ``'Hello there'``
    **e.**   ``''``

6. Which of the following results of the ``ord()`` and ``chr()`` functions are
   correct?

    **a.**  ``ord('1')`` ➝ ``49``
    b.      ``chr(68)`` ➝ ``'d'``
    **c.**  ``chr(99)`` ➝ ``'c'``

7. How many lines of screen output is displayed by the following
   expression, ``print('apple\nbanana\ncherry\npeach')``?

    a.       ``1``
    b.       ``2``
    c.       ``3``
    **d.**   ``4``


2.2 Variables and Identifiers
-----------------------------


2.2.1 What is a Variable?
-------------------------
* **tl;dr; variables are names for sorage locations that contain values**
* They can be thought of as having three parts:

    * a name, or identifier
    * a reference to a (memory) location
    * a value that lives at that referenced location (as an object)

* Variables are created with the assigment operator, ``=``.
* When varialbes are assigned, like this ``x = [1, 2, 3, 4, getnum()]``, the
  right side is evaluated first and then then resulting value is is assigned to
  the name on the left.
* You can reassign variables.
* Becuase the value assigned to a name can change, the order of variable
  assignments matters.

..  * This means the assignment operator, ``=``, is very differnt from ``=`` in
      math, where you can swap either side of the equality with each other for all
      occurances.
    * Instead, you can only swap either side for every subsequent occurance, at
      least until it's reassigned.
    * And you've assigned a variable name to a subroutine call that returns a
      different value every time, you can't ever reliably substitute the
      *definition* of a variable with the variable name again, only with the
      particular instance of the returned value.
    * Since variables are changable associations, the ``<-`` symbol would probably have
      been a better choice than ``=`` for assignment.
    * Some languages don't allow reassignment; ``=`` works mathematically.

.. * Variables don't have types, but the objects they refrence do. So you can
     reassign them to values of other types. Oh, and no static type checking.

* You can get the reference id of a variables value with the ``id()`` function.
* The value that a variable references, when considered by itself, is known as
  the derefrenced value.
* If you assign one variable to another, and the value is *mutable*, changes to
  one will affect the other. They'll reference the same object, after all.
* This can be confusing...
* If it's immutable, no problem, python will create a new value.


2.2.2 Variable Assignment and Keyboard Input
--------------------------------------------
* All input returned by the ``input()`` function is of the string data type.
* Built in functions ``int()`` and ``float()`` can be used to convert the string
  to a numeric type.


2.2.3 What Is an Identifier?
----------------------------
* An identifier is a sequence of one or more characters used to name a given
  program element. In Python, an identifier may contain letters and digits, but
  cannot begin with a digit. The special underscore character can also be used.
* More `here <https://docs.python.org/3/reference/lexical_analysis.html>`_.


2.2.4 Keywords and Other Predefined Identifiers in Python
---------------------------------------------------------
* How to check whether an identifier is a python keyword::

    'exit' in dir(__builtins__)
    OUT: True

* A keyword is an identifier that has predefined meaning in a programming
  language and therefore cannot be used as a regular identifier. Doing so will
  result in a syntax error.
* The ``_`` variable represents the result of the last evaluation made in the
  repl.


2.2.5 Let's Apply It - Restaurant Tab Calculation
-------------------------------------------------

Self-Test Questions
^^^^^^^^^^^^^^^^^^^
1. Which of the following are valid assignment statements, in which only
   variable k has already been assigned a value?

    **a.**   ``n = k + 1``
    b.       ``n = n + 1``
    c.       ``n + k = 10``
    d.       ``n + 1 = 1``

2. What is the value of variable ``num`` after the following assignment statements
   are executed?

    ::
        num = 0
        num = num + 1
        num = num + 5

* The value of ``num`` is 6.

3. Do variables ``num`` and ``k`` reference the same memory location after the
   following instructions are executed? (YES/**NO**)

    ::
        num = 10
        k = num
        num = num + 1

4. Which of the following are valid identifiers in Python?

    **a.**   ``errors``
    **b.**   ``error_count``
    c.       ``error-count``

5. Which of the following are keywords in Python?

    **a.**   ``and``
    b.       ``As``
    **c.**   ``while``
    d.       ``until``
    e.       ``NOT``

6. Which one of the following is correct for reading and storing an integer
   value from the user?

    a.       ``n = int_input('Enter: ')``
    **b.**   ``n = int(input('Enter: '))``


2.3 Operators
-------------


2.3.1 What Is an Operator?
--------------------------
* An operator is a symbol that represents an operation that may be performed on
  one or more operands. Operators that take on operand are called unary
  operators. Operators that take two operands are called binary operators.


2.3.2 Arithmetic Operators
--------------------------
* The division operator, ``/``, produces “true division” regardless of its
  operand types.
* The truncating division operator, ``//``, produces either an
  integer or float truncated result based on the type of operands applied to.
* The modulus operator, ``%``, gives the remainder of the division of its
  operands.


2.3.3 Let's Apply It - Your Place in the Universe
-------------------------------------------------
* Ok, I understand the example program.

Self-Test Questions
^^^^^^^^^^^^^^^^^^^
1. Give the results for each of the following.

    a. ``-2 * 3``::

        OUT: -6

    b. ``15 % 4``::

        OUT: 3

    c. ``3 ** 2``::

        OUT: 9

2. Give the exact results of each of the following division operations.

    a. ``5 / 4``::

        OUT: 1.25

    b. ``5 // 4``::

        OUT: 1

    c. ``5.0 // 4``::

        OUT: 1.0

3. Which of the expressions in question 2 is an example of integer division?

    * Answer b is an example of integer division.

4. Do any two of the expressions in question 2 evaluate to the exact same
   result? (YES/**NO**)

5. How many operands are there in the following arithmetic expression?

    ::

        2 * 24 + 60 - 10

    **a.**   ``4``
    b.       ``3``
    c.       ``7``

6. How many binary operators are there in the following arithmetic expression?

    ::

        -10 + 24 / (16 + 12)

    a.       ``2``
    **b.**   ``3``
    c.       ``4``


2.4 Expressions and Data Types
------------------------------


2.4.1 What Is an Expression?
----------------------------
* An expression is a combination of symbols (or a single symbol) that evaluates
  to a value.  A subexpression is any expression which is part of a larger
  expression.
* Expressions which evaluate to a numeric type are called arithmetic expressions.
* There are other ways of representing expressions called prefix and postfix
  notation, in which operators are placed before and after their operands,
  respectively.


2.4.2 Operator Precedence
-------------------------
* Operator precedence is the relative order that operators are applied in the
  evaluation of expressions, defined by a given operator precedence table.

    In order of precedence:

    +-------------------------------+--------------------------+
    |  Operator                     |           Associativity  |
    +===============================+==========================+
    |  ``**`` (exponentiation)      |           right-to-left  |
    +-------------------------------+--------------------------+
    |  ``-``  (negation)            |           left-to-right  |
    +-------------------------------+--------------------------+
    |  ``*``, ``/``, ``//``, ``%``  |           left-to-right  |
    +-------------------------------+--------------------------+
    |  ``+``, ``-``                 |           left-to-right  |
    +-------------------------------+--------------------------+

* Notice how the negation operator is listed after exponentiation? This can
  lead to some confusing results. Eg.::

    >>> -100 ** 4
    -100000000

This should be a positive number, right? What gives? It's negating the number
after performing exponentiation, instead of exponentiating a negative number.

::
    >>> (-100) ** 4
    100000000

In order to prevent this, you can use parenthesis to evaluate the negation
first.


2.4.3 Operator Associativity
----------------------------
* Operator associativity is the order that operators are applied when having
  the same level of precedence, specific to each operator.


2.4.4 What Is a Data Type?
--------------------------
* A data type is a set of values, and a set of operators that may be applied to
  those values.
* In static typing a variable is declared as a certian type before it is used.
* In dynamic typing, the data type of a variable depends only on the type of
  value the variable is currently holding. Thus, the same variable may be
  assigned values of different type during the execution of a program.


2.4.5 Mixed-Type Expressions
----------------------------
* A mixed-type expressions is an expression that has operands of different type.

Coercion vs. Type Conversion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Coercion is the implicit (automatic) conversion of operands to a common type.
  Type conversion is the explicit conversion of operands to a specific type.

Self-Test Questions
^^^^^^^^^^^^^^^^^^^

1. What value does the following expression evaluate to?

    ::
        2 + 9 * ((3 * 12) – 8) / 10

    a.       ``27``
    **b.**   ``27.2``
    c.       ``30.8``

2. Evaluate the following arithmetic expressions using the rules of operator
   precedence in Python.

    a. ``3 + 2 * 10``::
        OUT: 23

    b. ``2 + 5 * 4 + 3``::
        OUT: 25

    c. ``20 // 2 * 5``::
        OUT: 50

    d. ``2 * 3 ** 2``::
        OUT: 18

3. Evaluate the following arithmetic expressions based on Python’s rules of
   operator associativity.

    a. ``24 // 4 // 2`` ➝  ``6 // 2`` ➝  ``3``
    b. ``2 ** 2 ** 3``  ➝  ``2 ** 8`` ➝  ``256`` *Right to left associativity*

4. Which of the following is a mixed-type expression?

    **a**.   ``2 + 3.0``
    b.       ``2 + 3 * 4``

5. Which of the following would involve coercion when evaluated in Python?

    **a.**   ``4.0 + 3``
    b.       ``3.2 * 4.0``

6. Which of the following expressions use explicit type conversion?

    **a.**   ``4.0 + float(3)``
    b.       ``3.2 * 4.``
    **c.**   ``3.2 + int(4.0)``


2.4.6 Let's Apply It - Temperature Conversion Program
-----------------------------------------------------
* This subsection outlines a celcisus to fahrenheit temperature conversion
  program. It's fairly simple. ``celsius = (fahren - 32) * 5 / 9`` is the bulk
  of the programs logic.

Self-Test Questions
^^^^^^^^^^^^^^^^^^^

1. What value does the following expression evaluate to?
   ::
        2 + 9 * ((3 * 12) – 8) / 10

    a. 27
    **b.** 27.2
    c. 30.8

2. Evaluate the following arithmetic expressions using the rules of operator
   precedence in Python.

    a. 3 + 2 * +0       evaluates to 3
    b. 2 + 5 * 4 + 3    evaluates to 25
    c. 20 // 2 * 5      evaluates to 50
    d. 2 * 3 ** 2       evaluates to 18

3. Evaluate the following arithmetic expressions based on Python’s rules of
   operator associativity.

    a. 24 // 4 // 2     evaluates to 3
    b. 2 ** 2 ** 3      evaluates to 256

4. Which of the following is a mixed-type expression?

    **a.** 2 + 3.0
    b. 2 + 3 * 4

5. Which of the following would involve coercion when evaluated in Python?

    **a.** 4.0 + 3
    b. 3.2 * 4.0

6. Which of the following expressions use explicit type conversion?

    **a.** 4.0 + float(3)
    b. 3.2 * 4.0
    **c.** 3.2 + int(4.0)


