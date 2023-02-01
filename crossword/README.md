Write an AI to generate crossword puzzles.

Given the structure of a crossword puzzle (i.e., which squares of the grid are meant to be filled in with a letter), and a list of words to use, the problem becomes one of choosing which words should go in each vertical or horizontal sequence of squares. We can model this sort of problem as a constraint satisfaction problem. Each sequence of squares is one variable, for which we need to decide on its value (which word in the domain of possible words will fill in that sequence).

![image](https://user-images.githubusercontent.com/53656355/216117317-38b8034e-38a8-4d5f-9b94-a7eeef699d3e.png)
