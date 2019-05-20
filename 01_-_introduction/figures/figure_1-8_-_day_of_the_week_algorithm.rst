***************************************
 Figure 1-8: Day of the Week Algorithm
***************************************

To determine the day of the week given a month, day, year, and knowledge of
whether that year is a leap year:


1. Let ``century_digits`` be equal to the first two digits of the year.


2. Let ``year_digits`` be equal to the last two digits of the year.


3. Let ``value`` be equal to ``year_digits`` + ``floor(year_digits / 4)``


4. if ``century_digits`` equals 18, then add 2 to ``value``, else

   if ``century_digits`` equals 20, then add 6 to ``value``.


5. if the ``month`` is equal to January and ``year`` is not a leap year,
   then add 1 to ``value``, else.

   if the ``month`` is equal to February and the ``year`` is a leap year, then
   add 3 to ``value``, if not a leap year, then add 4 to ``value``, else

   if the ``month`` is equal to March or November, then add 4 to ``value``, else

   if the month is equal to May, then add 2 to ``value``, else

   if the month is equal to June, then add 5 to ``value``, else

   if the month is equal to August, then add 3 to ``value``, else

   if the month is equal to October, then add 1 to ``value``, else

   if the month is equal to September or December, then add 6 ``value``


6. Set ``value`` equal to ``(value+ day) mod 7``.


7. If ``value`` is equal to 1, then the day of the week is Sunday, else

   if ``vlaue`` is equal to 2, then the day of the week is Monday, else

   if ``vlaue`` is equal to 3, then the day of the week is Tuesday, else

   if ``vlaue`` is equal to 4, then the day of the week is Wednesday, else

   if ``vlaue`` is equal to 5, then the day of the week is Thursday, else

   if ``value`` is equal to 6, then the day of the week is Friday, else

   if ``value`` is equal to 0, then the day of the week is Saturday.


