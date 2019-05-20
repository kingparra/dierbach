*******************************
 Chapter 3: Control Structures
*******************************


Chapter Exercises
=================


Section 3.1
-----------
1. Which of the three forms of control is an implicit form of control?

    * Sequential control.

2. What is meant by a “straight-line” program?

   * A program without any explicit control structures, just one line of
     instructions after another.

3. What is the difference between a control statement and a control structure?

   * A control statement is just the line at the top of a structure with the
     keyword and boolean expression. It doens't include the body/suite, or any
     alternative clauses.

4. The Boolean data type contains two literal values, denoted as
   __True__ and __False__ in Python.

5. Which of the following relational expressions evaluate to True?

    a. 5 < 8
    c. '10' < '8'
    b. '5' < '8'
    d. 'Jake' < 'Brian'

6. Which of the following relational expressions evaluate to False?

    a. 5 <= 5
    c. 5 == 5
    e. 5 != 10
    b. 5 >= 5
    d. 5 != 5

7. Give an appropriate expression for each of the following.

    a. To determine if the number 24 does not appear in a given list of numbers
       assigned to variable nums.
    b. To determine if the name 'Ellen' appears in a list of names assigned to
       variable names.
    c. To determine if a single last name stored in variable last_name is
       either 'Morris' or 'Morrison'.

8. Evaluate the following Python expressions.

    (a) (12 * 2) 55 (3 * 8)
    (b) (14 * 2) !5 (3 * 8)

9. What value for x makes each of the following Boolean expressions true?

    (a) x or False
    (b) x and True
    (c) not (x or False)
    (d) not (x and True)

10. Evaluate the Boolean expressions below for n 5 10 and k 5 20.

    (a) (n . 10) and (k 55 20)
    (b) (n . 10) or (k 55 20)
    (c) not((n . 10) and (k 55 20))
    (d) not(n . 10) and not(k 55 20)
    (e) (n . 10) or (k 55 10 or k !5 5)

11. Give an appropriate Boolean expression for each of the following.

    (a) Determine if variable num is greater than or equal to 0, and less than 100.
    (b) Determine if variable num is less than 100 and greater than or equal to
        0, or it is equal to 200.
    (c) Determine if either the name 'Thompson' or 'Wu' appears in a list of
        names assigned to variable last_names.
    (d) Determine if the name 'Thomson' appears and the name 'Wu' does not
        appear in a list of last names assigned to variable last_names.

12. Evaluate the following Boolean expressions for num1 5 10 and num2 5 20.

    (a) not (num1 , 1) and num2 , 10
    (b) not (num1 , 1) and num2 , 10 or num1 1 num3 , 100

13. Give a logically equivalent expression for each of the following.

    (a) num !5 25 or num 55 0
    (b) 1 ,5 num and num ,5 50
    (c) not num . 100 and not num , 0
    (d) (num , 0 or num . 100)

14. Give an appropriate if statement for each of the following.

    (a) An if statement that displays 'within range' if num is between 0 and 100, inclusive.
    (b) An if statement that displays 'within range' if num is between 0 and 100, inclusive, and displays 'out of range' otherwise.

15. Rewrite the following if-else statements using a single if statement and elif headers.

    ::

        if temperature .5 85 and humidity . 60:
            print('muggy day today')
        else:
            if temperature .5 85:
                print('warm, but not muggy today')
            else:
                if temperature .5 65:
                    print('pleasant today')
                else:
                    if temperature ,5 45:
                        print('cold today')
                    else:
                        print('cool today')

16. Regarding proper indentation,

    (a) Explain the change in indentation needed in order for the following
        code to be syntactically correct.
    (b) Indicate other changes in the indentation of the code that is not
        strictly needed, but would make the code more readable.

    ::

        if level ,5 1:
            print('Value is well within range')
            print('Recheck in one year')
        elif level ,5 2:
            print('Value is within range')
            print('Recheck within one month')
        elif level ,5 3:
            print('Value is slightly high)
            print('Recheck in one week')
        elif level ,5 4:
            print('Value abnormally high')
            print('Shut down system immediately')

17. Write a program segment that uses a while loop to add up all the even
    numbers between 100 and 200, inclusive.

18. The following while loop is meant to multiply a series of integers input by
    the user, until a sentinel value of 0 is entered. Indicate any errors in
    the code given.

    ::

        product = 1
        num 5 input('Enter first number: ')
        while num !5 0:
        num 5 input('Enter first number: ')
        product 5 product * num
        print('product 5 ', product)

19. For each of the following, indicate which is a definite loop, and which is
    an indefinite loop.

    (a) ::

        num 5 input('Enter a non-zero value: ')
        while num 55 0:
            num 5 input('Enter a non-zero value: ')

    (b) ::

        num 5 0
        while n , 10:
            print 2 ** n
            n 5 n 1 1

