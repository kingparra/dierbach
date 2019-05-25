#!/usr/bin/env python3
import pexpect


def run_script(p, n, f, i, c, L):
    child = pexpect.spawn('./1-34_-_drake_equation_program.py')
    child.expect('What percentage of stars do you think have planets?: ')
    child.sendline(p)
    child.expect('How many places per star do you think can support life?: ')
    child.sendline(n)
    child.expect('What percentage do you think actually develop life?: ')
    child.sendline(f)
    child.expect('What percentage of those do you think have intelligent life?: ')
    child.sendline(i)
    child.expect('What percentage of those do you think can communicate with us?: ')
    child.sendline(c)
    child.expect('Number of years you think civilizations last?: ')
    child.sendline(L)
    # child.expect('there are an estimated', round(num_detectable_civilizations), 'potentially detectable civilizations in our galaxy')
    #                                                      ^ how do I get this substring?


def main():
    # Extreme cases (no chance of contacting intelligent life)
    # Zero planets per star
    assert run_script("0", "2", "100", "1", "1", "10000") == "0"
    # Zero percent of planets support life
    assert run_script("50", "2", "100", "1", "1", "10000") == "0"

