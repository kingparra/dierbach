# Floating point values have a range limited from ``10 ** -308`` to ``10 ** 308``.
# They have 16 to 17 digits of precision.
1.2e200 * 2.4e100 # Just at the limit of precision and range.
# OUT: 2.88e+300
1.2e200 * 2.4e200 # This should be an arithemetic overflow.
# OUT: inf
1.2e200 / 2.4e100 # Not too sure, should be OK.
# OUT: 5e+99
1.2e-200 / 2.4e200 # This should result in an artithemetic underflow.
# OUT: 0.0
# An arithemetic underflow, by the way, is a condition that occurs when a
# calculated result is too small in magnititude to be represented.
