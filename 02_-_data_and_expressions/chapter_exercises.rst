*********************************
 Chapter 2: Data and Expressions
*********************************



Chapter Exercises
=================


Section 2.1
-----------
1. Based on the information in Figure 2-1, how many novels can be stored in one
   terabyte of storage?

    * A staggering 1,099,511 novels! Probably only if they're stored as plain
      text, however.

2. Give the following values in the exponential notation of Python, such that
   there is only one significant digit to the left of the decimal point.

    a. 4580.5034

        * 4.580503e+03

    b. 0.00000046004

        * 4.600400e-07

    c. 5000402.000000000006

        * 5.000402e+06

3. Which of the floating-point values in question 2 would exceed the
   representation of the precision of floating points typically supported in
   Python, as mentioned in the chapter?

    * Value c, 5000402.000000000006, would lose precision. Actually, in newer
      versions of python it wont.

4. Regarding the built-in format function in Python,

    a. Use the format function to display the floating-point value in a
       variable named result with three decimal digits of precision.

       * ``format(result, '.3f')``

    b. Give a modified version of the format function in a so that commas
       are included in the displayed results.

       * ``format(result, ',')``

5. Give the string of binary digits that represents, in ASCII code,

    a. The string 'Hi!'

        * ``print(*map(ord, "Hi!"))`` --> 72 105 33

    b. The literal string 'I am 24'

        * 73 32 97 109 32 50 52

6. Give a call to print that is provided one string that displays the following
   address on three separate lines

      | John Doe
      | 123 Main Street
      | Anytown, Maryland 21009

    * ``print("John Doe 123\nMain Street Anytown,\nMaryland 21009")``, or I
      could have triple quoted it and used real line breaks, instead.

7. Use the print function in Python to output It's raining today.

   * Done. I just executed ``print("It's raining today")`` at the repl.


Section 2.2
-----------
8. Regarding variable assignment,

    a. What is the value of variables num1 and num2 after the following
        instructions are executed?

        ::
            num = 0
            k = 5
            num1 = num + k * 2
            num2 = num + k * 2

        * Both ``num1`` and ``num2`` reference the value ``10``.

    b. Are the values id(num1) and id(num2) equal after the last statement is
        executed?

        * Yes, they're both pointing to the same object with a value of 10.
          The python interpreter is smart enough not to waste memory by storing
          two copies of the same value in most cases.

9. Regarding the input function in Python,

    a. Give an instruction that prompts the user for their last name and
       stores it in a variable named last_name.

       * ``last_name = input("Enter your last name: ")``

    b. Give an instruction that prompts the user for their age and stores it
       as an integer value named age.

       * ``age = int(input("Enter your age: "))``

    c. Give an instruction that prompts the user for their temperature and
       stores it as a float named current_temperature.

       * ``current_temperature = float(input("Enter your temperature: "))``

10. Regarding keywords and other predefined identifiers in Python, give the
    result for each of the following,

    a. ``'int' in dir(__builtins__)``

        * True

    b. ``'import' in dir(__builtins__)``

        * False (Naniii!??!)


Section 2.3
-----------
11. Which of the following operator symbols can be used as both a unary
    operator and a binary operator?  ``+, -, *, /``

    * ``-`` can be either the uniary ("singulary", if you want to use the Latin
      prefix) negation operator, or the infix subtraction operator.

12. What is the exact result of each of the following when evaluated?

    a. ``12 / 6.0``

        * ``2.0``

    b. ``21 // 10``

        * ``2``

    c. ``25 // 10.0``

        * ``2.0``

13. If variable n contains an initial value of 1, what is the largest value
    that will be assigned to n after the following assignment statement is
    executed an arbitrary number of times?

    ::
        n = (n + 1) % 100

    * 99

14. Which of the following arithmetic expressions could potentially result in
    arithmetic overflow, where n and k are each assigned integer values?

    **a.** ``n * k``
    **b.** ``n ** k``
    c. ``n / k``
    **d.** ``n + k``


Section 2.4
-----------
15. Evaluate the following expressions in Python.

    a. ``10 - (5 * 4)``

        * -10

    b. ``40 % 6``

        * 4

    c. ``- (10 / 3) + 2``

        * -1.3333333333333335

16. Give all the possible evaluated results for the following arithmetic
    expression (assuming no rules of operator precedence).

    ``2 * 4 + 25 – 5``

    * This would amount to writing every possible combination of '*', '+', and
      '-', including cases where two operators have equal precedence, right?
      Then I would have to parenthesize the expression according to those rules
      and evaluate it by hand. That's a lot of typing and number crunching. Let
      me see if I can automate it, instead.

    ::
        #!/usr/bin/env python3
        import itertools
        operators = {'*', '-', '+'}
        combos = itertools.permutations(operators, 2)
        # cases where two operators share the same precedence
        for combo in combos:
            missing_operator = operators - set(combo)
            print(combo, missing_operator)
        # cases where each operator has its own precedence
        combos = itertools.permutations(operators, 3)
        for combo in combos:
            for elem in combo:
                print(set(elem), end='')
            print()

    * OK, so this garbage code generates every possible combination of
      operators for this question. Leftmost operators have higher precedence.
      If operators are grouped together, they are the same precedence.

    * Now to parenthesize the expressions according to our list of operator
      precedences.

       +----------+-----------------------+-----------------------+
       |  Value   |  Expression           |  Operator Precedence  |
       +==========+=======================+=======================+
       |    48    |  2 * (4 + 25 – 5)     |  ('+', '-') {'*'}     |
       +----------+-----------------------+-----------------------+
       |    28    |  (2 * 4 + 25) – 5     |  ('*', '+') {'-'}     |
       +----------+-----------------------+-----------------------+
       |    28    |  (2 * 4 – 5) + 25     |  ('*', '-') {'+'}     |
       +----------+-----------------------+-----------------------+
       |    53    |  (2 * (4 + 25)) – 5   |  {'+'}{'*'}{'-'}      |
       +----------+-----------------------+-----------------------+
       |    48    |  2 * ((4 + 25) – 5)   |  {'+'}{'-'}{'*'}      |
       +----------+-----------------------+-----------------------+
       |    28    |  ((2 * 4) + 25) – 5   |  {'*'}{'+'}{'-'}      |
       +----------+-----------------------+-----------------------+
       |    28    |  ((2 * 4) – 5) + 25   |  {'*'}{'-'}{'+'}      |
       +----------+-----------------------+-----------------------+
       |    48    |  2 * (4 + (25 – 5))   |  {'-'}{'+'}{'*'}      |
       +----------+-----------------------+-----------------------+
       |    28    |  (2 * 4) + (25 – 5)   |  {'-'}{'*'}{'+'}      |
       +----------+-----------------------+-----------------------+

    * And finally, to compute the values, I'll just copy-paste the expressions
      into the repl and add it to the table above.

17. Parenthesize all of the subexpressions in the following expressions
    following operator precedence in Python.

    a. ``var1 * 8 - var2 + 32 / var3``

        * ``(var1 * 8) - var2 + (32 / var3)``

    b. ``var1 - 6 ** 4 * var2 ** 3``

        * ``var1 - ((6 ** 4) * (var2 ** 3))``

18. Evaluate each of the expressions in question 17 above for ``var1 = 10``,
    ``var2 = 30``, and ``var3 = 2``.

19. For each of the following expressions, indicate where operator
    associativity of Python is used to resolve ambiguity in the evaluation of
    each expression.

    a. ``var1 * var2 * var3 - var4``

        * ``(((var1 * var2) * var3) - var4)`` Multiplication is left
          associative.

    b. ``var1 * var2 / var3``

        * ``((var1 * var2) / var3)`` Multiplication and division are left
          associative.

    c. ``var1 ** var2 ** var3``

        * ``(var1 ** (var2 ** var3))`` Exponentiation is right associative.

20. Using the built-in type conversion function float(), alter the following
    arithmetic expressions so that each is evaluated using floating-point
    accuracy. Assume that var1, var2, and var3 are assigned integer values. Use
    the minimum number of calls to function float() needed to produce the
    results.

    >> I guess this is the books way of telling me to review which operators
    perform type casting (convert to a common type). What doesn't make much
    sense, though, is that you can simply make an entire expression the
    argument to ``float()``. Oops. Just for this exercise, I'll pretend I don't
    know that, and ``float()`` can only take one of the variables as an
    argument.

    a. ``var1 + var2 * var3`` -- Take your pick. If any of these are floats,
        the rest will be typecasted to a float.

    b. ``var1 // var2 + var3`` -- Var3 should be passed to float.

    c. ``var1 // var2 / var3`` -- No call to float necessary here. Division `/`
        always returns a float.

