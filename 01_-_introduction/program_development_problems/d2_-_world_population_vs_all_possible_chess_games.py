#!/usr/bin/env python3
# Based on the information provided about the game of chess in section 1.1.2,
# develop and test a program that determines how many years it would take for
# all possible chess games to be played if everyone in the world (regardless of
# age) played one (unique) chess game a day. Assume the current world
# population to be 7 billion.

# How many possible unique chess games can be played?

world_population = 7_000_000_000
unique_games = 10 ** 120
days_to_solve = unique_games / world_population
years_to_solve = days_to_solve / 365
print("Assuming everyone on earth ({} people) each played a unique game of chess "
      "every day, it would take {} years to solve all possible chess games.".format(
        format(world_population, ','),
        years_to_solve
        )
    )

