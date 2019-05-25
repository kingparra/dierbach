***********************
 Chapter 11: Recursion
***********************



Fundamental Concepts
====================

    The power of recursion evidently lies in the possibility of defining an
    infinite set of objects by a finite statement. In the same manner, an
    infinite number of computations can be described by a finite recursive
    program, even if this program contains no explicit repetitions.
    — Niklaus Wirth, Algorithms + Data Structures = Programs, 1976


11.1 Recursive functions
------------------------


11.1.1 What Is a Recursive Function?
------------------------------------
* The notion of a self-referential function is inherently confusing.
* There are two types of entities related to any function - the function
  definition, and any current execution instances of it.
* What is meant by the phrase "a function that calls itself" is a function
  execution instance that creates another execution instance of the same
  function.
* Each caller will wait to terminate until the called child function instance
  has completed it's execution or returned a value.
* A non terminating sequence of self referential function calls is known as
  infinite recursion.
* Properly designed recursive functions always conditionally call another
  execution instance so that eventually the chain of function calls terminates.
* Once the function call chain terminates, the results of each function will
  usually be combined in some way to produce an answer.


11.1.2 The Factorial Function
-----------------------------
* Every properly defined recursive function must have at least one base case,
  and must redefine the problem into subproblems that work towards a base case
  such that the solution of the original problem can be derived from the
  solutons of the recursively solved subproblems.

.. figure 11-4: Requirements of a Properly Designed Recursive Function

The Recursive Definition of the Factorial Function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. figure 11-5: Recursive Factorial Function Implementation

A Recursive Factorial Function Implementation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. figure 11-6: Factorial Recursive Instance Calls

* Although the factorial function is an often-used example of a recursive
  function, the function can be executed more effieciently when implemented to
  use iteration.


11.1.3 Let's Apply It: Fractals (Sierpinski Triangle)
-----------------------------------------------------
* The serpenski triangle is an exmaple of a fractal.
* A fractal is a shape that contains parts that similar to the whol shape, thus
  having the property of self-similarity.


11.2 Recursive Problem solving
------------------------------


11.2.1 Thinking Recursively
---------------------------
* We commonly solve problems by breaking a problem into subproblems, and
  separately solving each subproblem.
* Recursive problem solving is the same, except that a problem is broken
  down into subproblems that are another instance of the original type
  problem.
* The conceptual elegance of recursive algorithms is the symmetry
