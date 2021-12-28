"""
This one didn't use any script so I'll write down my notes instead
"""


"""
The general outline of the program is a password checker

The program has a "stack" (done using * 26, / 26, % 26) to retrieve/add the previous input

There are 14 inputs:
    - 7 to add a digit
    - 7 more to check it with the digits that were added
The goal is to make sure all 7 insertions are valid

An insertion is "valid" if the last digit in the stack's difference to the digit that was just inputted is equal to a hardcoded value

This is the outline/hardcoded values my program/puzzle input had:


store
  store 
    store 
      store + check [diff of -2]
      store + check [diff of +6]
    check [diff of -8]
  store
    store + check [diff of +3]
  check [diff of -3]
  check [diff of -5]
check [diff of +2]

Example: for the maximum, we have:
    [7,
       9,
         9,
           9,7,
           3,9,
         1,
       9,
         6,9,
       6,
       4,
    9]
is the answer (the full number is 79997391969649)

For the minimum you do the same but minimize with 1s instead of 9s
"""