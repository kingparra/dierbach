*************************
 Chapter 1: Introduction
*************************



Computational Problem Solving
=============================


1.5 The Process of Computational Problem Solving
------------------------------------------------
Computational problem solving is more than just programming.

* Analysis

  * Clearly understand the problem.
  * Know what constitutes a solution.

* Design

  * Determine what type of data is needed.
  * Determine how data is to be structured.
  * Find and/or design appropriate algorithms.

* Implementation

  * Represent data within the programming language.
  * Implement algorithms in the programming language.

* Testing

  * Test the program on a selected set of problem instances.
  * Correct *and understand* the causes of any errors found.


1.5.1 Problem Analysis
----------------------

Understanding the Problem
^^^^^^^^^^^^^^^^^^^^^^^^^
* Once a problem is clearly understood, the fundamental computational
  issues for solving it can be determined.
* This is the hardest part. Contrary to how the book organizes this I don't
  consider it a single step, but something that continues to evolve while
  working on a problem.

Knowing What Constitutes a Solution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* A program may be stated as finding a solution, an approximate solution,
  a best solution, or all solutions. You choose which one is appropriate
  for your problem.


1.5.2 Program Design
--------------------

Describing the Data Needed
^^^^^^^^^^^^^^^^^^^^^^^^^^
* The appropriate representation of data is a fundamental aspect of computer science.
* Representation of data can affect how you interact with it.

Describing the Needed Algorithms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* First, we identify what the needed logic is, then use psuedocode and diagramming to
  get an idea of what it will look like without worrying about implementation details.
* It's a good idea to search for existing algorithms.


1.5.3 Program Implementation
----------------------------
* In this phase, we express the logic in a language, beholden to all it's quirks and
  limitations.


1.5.4 Program Testing
---------------------
* Testing should be done incrementally as a program is being developed.
* Ideally, you should write a test before implementing a component of your software.
* It is important to not only test, but to test systematically.

Truisms of software development:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Programming errors are pervasive, persistent, and inevitable.
2. Software testing is an essential part of software development.
3. Any changes made in correcting a programming error should be fully
   understood as to why the changes corrected the detected error.


1.6 The Python Programming Language
-----------------------------------


1.6.1 About Python
------------------
* Guido Van Rossum created the language around 1990. He first began it's
  implementation in December 1989 as a hobby programming project to keep him
  occupied around Christmas. It's first release was on 16th of October, 2001.
* It is high-level, interpreted, uses dynamic typing, does not require manual
  memory management (it uses a combination of reference counting and a
  cycle-detecting garbage collector, instead), and is easy to read.
* Python has built-in support for arbitrary precision arithmetic. Integers are
  transparently switched from fixed precision representation to ``long`` type,
  which supports arbitrary precision when needed.
* All string literals are unicode UTF-8 encoded by default. Yay!


1.6.2 The IDLE Python Development Environment
---------------------------------------------
* An Integrated Development Environment, or IDE, is a bundled set of software
  tools for program development.


1.6.3 The Python Standard Library
---------------------------------
* The Python Standard Library is a collection of modules, each providing
  specific functionality beyond what is included in the core part of Python.


1.6.4 A Bit of Python
---------------------

Variables
^^^^^^^^^
* Variables are a name assigned to a value. The value can change, hence the
  name 'variable'.
* Variables are set with the assignment operator, ``=``, like this::

    var_name = 'value'

Some Basic Arithmetic Operators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* The common arithmetic operators in Python are ``+``, ``-``, ``*``, ``/``
  (division), and ``**`` (exponentiation).

Basic Input and Output
^^^^^^^^^^^^^^^^^^^^^^
* In Python, ``input()`` is used to request and get information from the user,
  and ``print()`` is used to display information on the screen.


1.6.5 Learning How to Use IDLE
------------------------------
* Write a script, run it with :kbd:`F5`, then debug. Arrowing up and pressing
  :kbd:`Ctrl`-:kbd:`Enter` will copy that line to the prompt.
* But, let's be serious here; Don't use IDLE, it's terrible. Use vim and xonsh
  instead, or any sane editor.


1.7 A First Program - Calculating the Drake Equation
----------------------------------------------------
* The purpose of the drake equation is to calculate the number of
  civilizations that may exist in our galaxy that we may be able to
  communicate with. It looks like this::

    N = R * p * n * f * i * c * L


1.7.1 The Problem
-----------------
* Develop a program that will allow a user to run the calculation with their
  own values for ``p``, ``n``, ``f``, ``i``, ``c``, and ``L``. It should then
  display the calculated result.


1.7.2 Problem Analysis
----------------------
* In the simplest case, just get the data and multiply everything. For a more
  robust approach, some input checking should be done.


1.7.3 Program Design
--------------------
1. Program greeting
2. Get user input
3. Calculate result
4. Display result


1.7.4 Program Implementation
----------------------------
* Figure 1-34 on page 31 shows an implementation in Python. 1-35 shows the
  command output from running it.


1.7.5 Program Testing
---------------------
* Test Case:

  A set of input values and the expected output for each one.

* Test Plan / Test Suite:

  A number of test cases to verify that a program meets all requirements. A
  good strategy is to include "average" as well as "extreme" or "special"
  cases in a test plan. Another approach is to define unacceptable outputs
  and use a program to send in arbitrary input within certain constraints.

