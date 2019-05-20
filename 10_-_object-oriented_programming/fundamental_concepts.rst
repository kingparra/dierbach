*****************************************
 Chapter 10: Object-Oriented Programming
*****************************************



Fundamental Concepts
====================


10.1 What Is Object-Oriented Programming?
-----------------------------------------


10.1.1 What Is a Class?
-----------------------
* A class specifies the set of instance variables and methods that are bundled
  together for defining a type of object.


10.1.2 Three Fundamental Features of Object-Oriented Programming
----------------------------------------------------------------
* Three fundamental features supporting the design of object-oriented programs
  are referred to as encapsulation, inheritance, and polymorphism.


10.2 Encapsulation
------------------


10.2.1 What Is Encapsulation
----------------------------
* Encapsulation is a means of bundling together instance variables and methods
  to form a given type, as well as a way of restricting access to certain class
  members.
* Private class member names begin with double underscores.
* All private class members are automatically renamed to begin with a single
  underscore followed by the class name. This practice is known as name
  mangling, and is a form of information hiding.
* Name mangling is used to discourage direct or unintentional manipulation of
  instance variables. Instead, methods should be used to set or retrieve them.
  The naming convention for these methods is to start with "get" or "set", so
  they're referred to as "getters" and "setters".


10.2.2 Defining Classes in Python
---------------------------------

Defining a Fraction Class
^^^^^^^^^^^^^^^^^^^^^^^^^
* The ``class`` keyword is used to start a class definition.
* Instance variables are initialized by the ``__init__`` special method of a
  class.

Special Methods in Python
^^^^^^^^^^^^^^^^^^^^^^^^^
* Special methods in Python have names that *begin and end* with two underscore
  characters, and are automatically called in Python.
* They can define things like what logic should be executed when an object is
  used in combination with an operator, how the object should be represented
  on the repl, or as a string, etc. There's a lot of them.
* The special method to define how an object should be represented as a string
  is ``__str__``. The ``__repr__`` special methods defines how it should look
  when evaluated directly from the interpreter.

Adding Arithmetic Operators to the Fraction Class
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* This subsubsection deals with implementing the ``__neg__``, ``__add__``,
  ``__sub__``, and ``__mul__`` special methods for the Fraction class. Nothing
  special here, but check out Figure 10-8 if you want.


10.3 Inheritance
----------------


10.2.1 What Is Inheritance?
---------------------------
* Inheritance is object-oriented programming is the ability of a subclass (also
  "derived class" or "child class") to inherit members of a superclass (also
  "base class" or "parent class" or "ancestor class") as part of its own
  definition.


10.3.2 Subtypes
---------------
* A subtype is something that can be substituted for and behave as its parent
  type (and *its* parent type, etc.).


10.3.3 Defining Subclasses in Python
------------------------------------

Class Names of the Built-In Types in Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


10.5 Object-Oriented Design Using UML
-------------------------------------


10.5.1 What Is UML?
-------------------
* UML ("Unified Modeling Language") is a standardized language-independent,
  graphical modeling language for specifying an object-oriented design.


10.5.2 UML Class Diagrams
-------------------------
* **Class diagrams** in UML are used to express the static aspects of an object
  oriented design, such as the instance variables and methods of individual
  classes.
* Other diagrams, called **interaction diagrams**, are used to represent the
  sequence of methods calls between objects during program execution.

The Representation of Classes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::
    +----------------------------------+
    |  **Class Name**  {type}          | <--- {type} is optional.
    +==================================+
    | -instance variable: integer      | <--- [-|+]identifier:type
    | +instance variable: string       |
    |               ...                |
    +----------------------------------+
    | -method(x:int, y:str)            | <--- [-|+]identifier(identifier:type ...)
    | +method()                        |
    |               ...                |
    +----------------------------------+

* Visibility of members ... ``-`` means private, ``+`` means public.
* Arguments within the methods parenthesis denote the return values of the
  methods, not formal parameters.
* Initialization methods like pythons ``__init__`` are named ``create()`` in UML.

Denoting Associations Between Classes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* An **association** between two classes, denoted by a connecting solid line and
  possible arrow head, indicates that methods of one class call methods of
  another.
* The line can have a number in superscript over either end. This is called the
  **multiplicity**, and denotes how many instances each object correspond to each
  other. (One to one, one to may, etc.)
* A **role name,** which shows up as subscript under the connecting line, is used
  to describe the association between the two classes. What the association
  does.
* The direction the arrow points denotes it's **navigability**, or the direction
  in which methods calls are made.
* Here's what that might look like:

::
  +              (multiplicity: 1 instance maps to 0 or more)
    +----------------+                                 +------------------+
    | GraphicsWindow |  1                        0..*  | Shape {abstract} |
    |                | ------------------------------> |                  |
    |                |  creates                        |                  |
    +----------------+    (role name)                  +------------------+

Denoting Subclass Relationships
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Sublcass relationships in UML are indicated by use of a solid line with a
  closed arrow head from a subclass to a superclass.
* Unicode characters used to represent non-open arrowheads in my notes can be
  found `here <https://en.wikipedia.org/wiki/Geometric_Shapes >`_. Hopefully
  they render correctly on GitHub.

::
    +----------------+
    | Shape          |
    | {abstract}     | <-- Parent/Super Class
    |                |
    +----------------+
            △          <-- Closed arrow head can be thought
            |              of as representing "is a subclass
            |              of" or "is a type of".
            |
    +----------------+
    | Circle         |
    |                |  <-- Subclass
    |                |
    +----------------+

Denoting Composition vs. Aggregation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* **Aggregation** is a "grouping" relationship, denoted by a unfilled diamond
  arrow head. It answers the question: What things does the parent class group
  together?
* **Composition** is a "part-of" relationship between classes, denoted by a
  filled diamond arrow head. It answers the question: What is the parent class
  composed of?

::
   +   Aggregation            Composition
    +-----------------+   +-----------------+
    | ShapeCollection |   | Shape           |
    |                 |   |                 |
    |                 |   |                 |
    +-----------------+   +-----------------+
            ◇                      ◆
            |                      |
            |                      |
            | 0..*                 | 1
    +-----------------+   +-----------------+
    | Shape           |   | XYCoord         |
    |                 |   |                 |
    |                 |   |                 |
    +-----------------+   +-----------------+
       Zero or more           One instance
       instances of            of XYCoord
     Shape are grouped       is an intergral
        together in           part of Shape
      ShapeCollection

An Example Class Diagram
^^^^^^^^^^^^^^^^^^^^^^^^
* UML can describe any set of entities and their relationships, not just
  software objects.
* See Figure 10-30: Passenger Car UML Class Diagram for an example of what a
  diagram of a car would look like.

Self-Test Questions
^^^^^^^^^^^^^^^^^^^
1. Which of the following is true of UML?

    a. UML is a specification language for designing Python programs
    **b.** UML is a specification language that can be used for designing programs
        in various programming languages


2. In UML, class diagrams are used to express the ``__static__`` aspects of a
   design, and ``__interaction_diagrams__`` are used to denote the dynamic aspects


3. In UML, an association between two classes indicates that

    a. The two classes have a common superclass
    b. Objects of each of the two class types are created at the same time
    **c.** Methods of one of the classes make calls to methods of the other

4. Multiplicity in UML indicates

    a. How many objects of a given class type exist
    **b.** How many objects of one given class there are in relation to another
    c. How many subclasses of a given class there may be

5. Composition in UML indicates,

    **a.** A “part of” relationship
    b. A grouping of objects

6. Aggregation in UML indicates,

    a. A “part of” relationship
    **b.** A grouping of objects

