Conway's Game of Life
======

I wrote this program to teach myself python. The program represents an simulator of 
John Conway's Game of Life. You can read about the game in detail here:
http://en.wikipedia.org/wiki/Conway's_Game_of_Life

Simply put, Conway's Game of Life is a cellular automaton. Cells exist in a grid
world, and they have very strict rules that govern if they are going to live or
die.

If a cell has less than 2 neighboring cells, it gets lonely and dies
If a cell has more than 3 neighboring cells, it gets overcrowded and dies
If a cell has exactly 2 or 3 neighboring cells, it is stable and lives
And if an empty grid spot has exactly 3 neighboring cells, a new cell is born
