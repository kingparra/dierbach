*************************
 Chapter 1: Introduction
*************************



Fundamental Concepts
====================


1.1 What is Computer Science?
-----------------------------
* Computer science is fundamentally about computational problem solving.


1.1.1 The Essence of Computational Problem Solving
--------------------------------------------------
* In order to solve a problem computationally, two things are needed: a
  representation that captures all the relevant aspects of the problem, and
  an algorithm that solves the problem by use of the representation.
* A representation that leaves out details of what is being represented is a
  form of abstraction.


1.1.2 Limits of Computational Problem Solving
---------------------------------------------
* Any algorithm that correctly solves a given problem must do so in a
  reasonable amount of time, otherwise it's of limited practical use.

Self-Test Questions
^^^^^^^^^^^^^^^^^^^
1. A good definition of computer science is “the science of programming
   computers.”

    (TRUE/**FALSE**)

2. Which of the following areas of study are included within the field of
   computer science?

    a. Software engineering
    b. Database management
    c. Information security
    **d.** All of the above

3. In order to computationally solve a problem, two things are needed: a
   representation of the problem, and an ``__algorithm__`` that solves it.

4. Leaving out detail in a given representation is a form of ``__abstraction__``.

5. A “brute-force” approach for solving a given problem is to:

    a. Try all possible algorithms for solving the problem.
    **b.** Try all possible solutions for solving the problem.
    c. Try various representations of the problem.
    d. All of the above

6. For which of the following problems is a brute-force approach practical to
   use?

    **a.** Man, Cabbage, Goat, Wolf problem
    b. Traveling Salesman problem
    c. Chess-playing program
    d. All of the above


1.2 Computer Algorithms
-----------------------


1.2.1 What is an Algorithm?
---------------------------
* An algorithm is a finite number of clearly described, unambiguous, "doable"
  steps that can be systematically followed to produce a desired result for the
  given input in a finite amount of time. (That is, it eventually terminates.)
* Algorithms solve a class of problem, not just a specific problem instance.
  For example, the expression ``3 + 5`` wouldn't be an algorithm, but ``num +
  num`` would, since it applies to any two input numbers. Algorithms solve
  general problems.


1.2.2 Algorithms and Computers: A Perfect Match
-----------------------------------------------
* Because computers can execute instructions very quickly an reliably without
  error, algorithms and computers are a perfect match.


Self-Test Questions
^^^^^^^^^^^^^^^^^^^
1. Which of the following are true of an algorithm?

    a. Has a finite number of steps
    b. Produces a result in a finite amount of time
    c. Solves a general problem
    **d.** All of the above

2. Algorithms were first developed in the 1930–1940s when the first computing
   machines appeared.

    (TRUE/**FALSE**)

3. Algorithms and computers are a “perfect match” because: (Select all that
   apply.)

    **a.** Computers can execute a large number of instructions very quickly.
    **b.** Computers can execute instructions reliably without error.
    c. Computers can determine which algorithms are the best to use for a given
    problem.

4. Given that the year 2016 is a leap year, what day of the week does April
   15th of that year fall on? Use the algorithm in Figure 1-8 for this.

    * Tuesday ( I miscalculated... It's actually Friday. Also, that algorithm is
    *really* hard for me to read. )

5. Which of the following is an example of an algorithm? (Select all that
   apply.)

    **a.** A means of sorting any list of numbers
    b. Directions for getting from your home to a friend’s house
    c. A means of finding the shortest route from your house to a friend’s house.


1.3 Computer Hardware
---------------------
* Computer hardware is the physical part of a computer system.


1.3.1 Digital Computing: It's All about Switches
------------------------------------------------
* The key to developing reliable systems is to keep the design as simple as
  possible.
* All information within a computer system is represented using only two
  digits, 0 and 1, which known as binary representation.


1.3.2 The Binary Number System
------------------------------
* A radix is the base used for the place values of a number system.
* The term bit stands for binary digit.
* A byte is a group of bits operated on as a single unit in a computer system,
  usually consisting of eight bits.


1.3.3 Fundamental Hardware components
-------------------------------------
* Central Processing unit (CPU):

  The "brain" of a computer, containing digital logic circuitry able to
  interpret and execute instructions.

* Main memory:

  Fast memory where currently executing programs reside.

* Secondary memory:

  Nonvolatile, long-term storage of programs and data.

* Bus:

  The circuitry that transfers data between hardware components of a
  computer system.


1.3.4 Operating Systems - Bridging Software and Hardware
--------------------------------------------------------
* Operating system:

  In a broad sense, this is the system of software that allows you to operate a
  computer. This includes software that talks to hardware, a supervisor to
  delegate resources to running programs, and some sort of interface.

* System software:

  Software designed to provide services to other software.


1.3.5 Limits of Integrated Circuits Technology: Moore's Law
___________________________________________________________
* Moore's Law states that the number of transistors that can be placed on a
  single silicon chip doubles roughly every two years.

Self-Test Questions
^^^^^^^^^^^^^^^^^^^
1. All information in a computer system is in binary representation.

    (**TRUE**/FALSE)

2. Computer hardware is based on the use of electronic switches called
    ``__transistors__``.

3. How many of these electronic switches can be placed on a single integrated
   circuit, or “chip”?

    a. Thousands
    b. Millions
    **c.** Billions

4. The term “bit” stands for ``__binary digit__``.

5. A bit is generally a group of eight bytes. (**TRUE**/FALSE)

6. What is the value of the binary representation 0110.

    a. 12
    b. 3
    **c.** 6

7. The ``__central processing unit__`` interprets and executes instructions in
   a computer system.

8. An operating system manages the hardware resources of a computer system, as
   well as provides a particular user interface.

    (**TRUE**/FALSE)

9. Moore’s Law predicts that the number of transistors that can fit on a chip
   doubles about every ten years.

    (TRUE/**FALSE**) It's every two years!


1.4 Computer Software
---------------------


1.4.1 What Is Computer Software?
--------------------------------
* Computer software is a set of program instructions, including related data
  and documentation, that can be executed by a computer.


1.4.2 Syntax, Semantics, and Program Translation
------------------------------------------------

What are Syntax and Semantics?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Syntax:
  The set of characters and their acceptable arrangements in a language. You
  can think of this as the spelling and grammar rules of the language.

* Semantics:
  The meaning associated with each syntactically correct sequence of
  characters.

Program Translation
^^^^^^^^^^^^^^^^^^^
* A compiler is a translator program that translates programs directly into
  machine code to be executed by the CPU. An interpreter executes program
  instructions in place on ("running on top of") the CPU.

Program Debugging: Syntax Errors vs. Semantic Errors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Syntax errors are caused by invalid syntax. Semantic (logic) errors are
  caused by errors in program logic


1.4.3 Procedural vs. Object-Oriented Programming
------------------------------------------------
* Procedural programming and object-oriented programming are two major
  programming paradigms in use today.

Self-Test Questions
^^^^^^^^^^^^^^^^^^^
1. Two general types of software are system software and ``__application__``
   software.

2. The syntax of a given language is,

    a. the set of symbols in the language.
    b. the acceptable arrangement of symbols.
    **c.** both of the above

3. The semantics of a given language is the meaning associated with any
   arrangement of symbols in the language.

  (TRUE/**FALSE**) ...it's the meaning associated with a **specific**
   arrangement.

4. CPUs can only execute instructions that are in binary form called
   ``__machine code__``.

5. The two fundamental types of translation programs for the execution of
   computer programs are ``__interpreters__`` and ``__compilers__``.

6. The process of finding and correcting errors in a computer program is called
   ``__debugging__``.

7. Which kinds of errors can a translator program detect?

    **a.** Syntax errors
    b. Semantic errors
    c. Neither of the above

8. Two major programming paradigms in use today are ``__procedural__``
   programming and ``__object oriented__`` programming.

